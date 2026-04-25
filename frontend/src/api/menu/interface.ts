// 登录模块
export namespace Menu {
    export interface MenuListItem {
        name?: string;
        routeName?: string;
        path?: string;
        component?: string;
        parent_id?: number;
        sort?: number;
        type?: number;
        perms?: string;
        icon?: string;
        is_hidden?: number;
        id?: number;

    }
    export interface LoginRes {
        code: number;
        msg: string;
        data: {
            access_token: string;
        };
    }

}
