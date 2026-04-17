import http from "../index";
import { type Login } from "@/api/user/interface";
export const getUserInfo = () => {
    return http.get('/user')
}

export const createUser = (data: any) => {
    return http.post('/user', data)
}

export const login = (data: object) => {
    return http.post<Login.LoginRes>(`/login`, data)
}

export const register = (data: object) => {
    return http.post(`/register`, data)
}
