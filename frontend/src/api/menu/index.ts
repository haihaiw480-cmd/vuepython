import http from "../index";
import { type MenuListRes } from "@/api/menu/interface";

export const getMenuList = () => {
    return http.get<MenuListRes>('/menu')
}

