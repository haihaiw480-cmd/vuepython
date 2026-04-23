// 登录模块
export namespace Menu {
    export interface MenuListItem {
        name: string;
        route_name: string;
        path: string;
        component: string;
        parent_id: number;
        sort: number;
        type: number;
        perms: string;
        icon: string;
        is_hidden: number;
        id: number;
        created_at: string;
        updated_at: string;
        is_deleted: false;
    }
    export interface LoginRes {
        code: number;
        msg: string;
        data: {
            access_token: string;
        };
    }
    export interface MenuParams {
        type: number;
    }
}
