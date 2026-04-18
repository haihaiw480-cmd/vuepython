// import http from "../index";
// import { type MenuListRes } from "@/api/menu/interface";
import authMenuList from "@/assets/json/authMenuList.json";
import authButtonList from "@/assets/json/authButtonList.json";
export const getMenuList = () => {
    return authMenuList;
    // return http.get<MenuListRes>('/menu')
};
