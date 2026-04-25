export { };
declare global {
    namespace Menu {
        interface MenuOptions {
            path: string;
            name: string;
            component?: string | (() => Promise<unknown>);
            redirect?: string;
            meta: MetaProps;
            children?: MenuOptions[];
        }

        interface MetaProps {
            icon: string;
            title: string;
            activeMenu?: string;
            isLink?: string;
            isHide: boolean;
            isFull: boolean;
            isAffix: boolean;
            isKeepAlive: boolean;
        }
        interface MenuItem {
            id: number;
            name?: string;
            routeName?: string;
            path: string;
            component: string | (() => Promise<unknown>);
            routeName: string;
            parentId: number;
            type: number; // 1目录 2菜单 3按钮
            icon?: string;
            isHidden?: number;
            children?: MenuItem[];
            sort?: number;
            perms?: string;



        }

        interface MenuParams {
            name?: string;
            routeName?: string;
            type?: number;
            is_hidden?: number;
            page?: number;
            pageSize?: number;
            id?: number;
        }
        interface CreatMenuPrams {
            name?: string;
            routeName?: string;
            path?: string;
            component?: string | (() => Promise<unknown>);
            routeName?: string;
            parentId?: number;
            type?: number; // 1目录 2菜单 3按钮
            icon?: string;
            isHidden?: number;
            sort?: number;
            perms?: string;

        }
    }
}
