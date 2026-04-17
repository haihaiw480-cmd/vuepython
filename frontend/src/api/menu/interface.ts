// 登录模块

export interface MenuListItem {
    path: string;
    name: string;
    redirect?: string;
    component: string;
    meta: {
        icon: string;
        title: string;
        isLink?: string;
        isHide: boolean;
        isFull: boolean;
        isAffix: boolean;
        isKeepAlive: boolean;
    };
    children?: MenuListItem[];
}
export interface MenuListRes {
    code: number;
    msg: string;
    data: MenuListItem[];
}
