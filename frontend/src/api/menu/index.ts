// import http from "../index";
// import { type MenuListRes } from "@/api/menu/interface";
import authMenuList from "@/assets/json/authMenuList.json";
import { type Menu } from "@/api/menu/interface"
import authButtonList from "@/assets/json/authButtonList.json";
export interface Response<T> {
    code: number;
    data: T;
    msg: string;
}
export interface PageResult<T> {
    list: T[];
    total: number;
    page: number;
    page_size: number;
}
import http from "@/api/index"
export const getMenuList = () => {
    return authMenuList;
    // return http.get('/menu/list')
};
export const getMenuListAll = (params?: Menu.MenuParams) => {
    // return authMenuList;
    return http.get<Response<PageResult<Menu.MenuListItem>>>('/menu/list', params)
};
export const PostMenuAdd = (params?: Menu.MenuListItem) => {
    // return authMenuList;
    return http.post<Response<PageResult<Menu.MenuListItem>>>('/menu/add', params)
};
