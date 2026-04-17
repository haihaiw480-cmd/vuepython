import axios, { AxiosError, type AxiosInstance, type AxiosRequestConfig, type AxiosResponse, type InternalAxiosRequestConfig } from 'axios';
import { ResultEnum } from '@/enums/httpEnum';
import { ElMessage } from "element-plus";
import { checkStatus } from "@/utils/checkStatus";
import { useUserStore } from "@/stores/user";
// 创建一个 Axios 实例，设置基础 URL 和超时时间

export interface CustomAxiosRequestConfig extends InternalAxiosRequestConfig {
    loading?: boolean;
    cancel?: boolean;
}
const config = {
    // 跨域时候允许携带凭证
    withCredentials: true,
    baseURL: '/api',
    timeout: ResultEnum.TIMEOUT as number,
}
class RequestHttp {
    service: AxiosInstance
    public constructor(config: AxiosRequestConfig) {
        this.service = axios.create(config)
        // 添加请求拦截器
        this.service.interceptors.request.use(
            (config: CustomAxiosRequestConfig) => {
                // axios 拦截器自动带 token
                const userStore = useUserStore();
                const token = userStore.access_token;
                if (token) {
                    config.headers['Authorization'] = 'Bearer ' + token
                }
                // 在发送请求之前可以添加一些公共的请求头或参数
                // 例如：config.headers['Authorization'] = 'Bearer ' + token
                return config
            }
        )

        // 添加响应拦截器
        this.service.interceptors.response.use(
            (response: AxiosResponse) => {
                const { data, config } = response
                console.log('响应拦截器', response)
                // 处理响应数据
                // 登录失效
                if (data.code == ResultEnum.OVERDUE) {
                    // todo 返回登陆页面
                    return Promise.reject(data);
                }
                // 全局错误信息拦截（防止下载文件的时候返回数据流，没有 code 直接报错）
                if (data.code && data.code !== ResultEnum.SUCCESS) {
                    console.log('全局错误信息拦截', data)
                    ElMessage.error(data.msg);
                    return Promise.reject(data);
                }
                return data
            },
            (error: AxiosError) => {
                const { response } = error;
                console.log('响应错误', error)
                // tryHideFullScreenLoading();
                // 请求超时 && 网络错误单独判断，没有 response
                if (error.message.indexOf("timeout") !== -1) ElMessage.error("请求超时！请您稍后重试");
                if (error.message.indexOf("Network Error") !== -1) ElMessage.error("网络错误！请您稍后重试");
                // 根据服务器响应的错误状态码，做不同的处理
                if (response) checkStatus(response.status);
                // todo 服务器结果都没有返回(可能服务器错误可能客户端断网)，断网处理:可以跳转到断网页面
                // if (!window.navigator.onLine) router.replace("/500");
                return Promise.reject(error);

            }
        )


    }
    get<T>(url: string, params?: object): Promise<T> {
        return this.service.get(url, { params })
    }
    post<T>(url: string, data?: object): Promise<T> {
        return this.service.post(url, data)
    }
    put<T>(url: string, data?: object): Promise<T> {
        return this.service.put(url, data)
    }
    delete<T>(url: string, params?: object): Promise<T> {
        return this.service.delete(url, { params })
    }
}




export default new RequestHttp(config)
