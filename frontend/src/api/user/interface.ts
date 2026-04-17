// 登录模块
export namespace Login {
    export interface ReqLoginForm {
        username: string;
        password: string;
    }
    export interface LoginRes {
        code: number
        msg: string
        data: {
            access_token: string
        }
    }
    export interface ResAuthButtons {
        [key: string]: string[];
    }
}
