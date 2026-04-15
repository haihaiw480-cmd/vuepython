import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse, type InternalAxiosRequestConfig } from 'axios';

// 创建一个 Axios 实例，设置基础 URL 和超时时间

export interface CustomAxiosRequestConfig extends InternalAxiosRequestConfig {
    loading?: boolean;
    cancel?: boolean;
}
const config = {
    // 跨域时候允许携带凭证
    withCredentials: true,
    baseURL: '/api',
    timeout: 5000
}
class RequestHttp {
    service: AxiosInstance
    public constructor(config: AxiosRequestConfig) {
        this.service = axios.create(config)
        // 添加请求拦截器
        this.service.interceptors.request.use(
            (config: CustomAxiosRequestConfig) => {
                const token = localStorage.getItem('token')
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
                console.log('响应拦截器', response)
                // 处理响应数据
                return response
            },
            error => {
                // 处理响应错误
                return Promise.reject(error)
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
