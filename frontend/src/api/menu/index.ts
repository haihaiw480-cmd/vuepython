// import http from "../index";
// import { type MenuListRes } from "@/api/menu/interface";
import authMenuList from "@/assets/json/authMenuList.json";
// import { type Menu } from "@/api/menu/interface"
import authButtonList from "@/assets/json/authButtonList.json";
export interface Response<T> {
    code: number;
    data: T;
    msg: string;
}
export interface PageResult<T> {
    list: T;
    total: number;
    page: number;
    page_size: number;
}
export interface DataRusult<T> {
    list: T;
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
    return http.get<Response<PageResult<Menu.MenuItem[]> | Menu.MenuItem[]>>('/menu/list', params)
};
export const PostMenuAdd = (params?: Menu.CreatMenuPrams) => {
    // return authMenuList;
    return http.post<Response<PageResult<Menu.MenuItem>>>('/menu/add', params)
};
// 编辑菜单
export const patchMenu = (id: number, params?: Menu.UpdataMenuPrams,) => {
    return http.patch<Response<PageResult<Menu.MenuItem>>>(`/menu/updata/${id}`, params)

}
// 删除菜单
export const deletetMenu = (id: number) => {
    // return authMenuList;
    return http.delete<Response<PageResult<Menu.MenuItem>>>(`/menu/delete/${id}`)
};
