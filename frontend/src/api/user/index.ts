import http from "../index";
export const getUserInfo = () => {
    return http.get('/users')
}
