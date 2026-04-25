
import { type RouteRecordRaw } from "vue-router";
export const flatMenuList = (menuList: Menu.MenuOptions[]): Menu.MenuOptions[] => {
    // 深拷贝：对象 → 转 JSON 字符串 → 再解析成新对象
    let newMenulist: Menu.MenuOptions[] = JSON.parse(JSON.stringify(menuList))
    return newMenulist.flatMap(item => [item, ...(item.children ? flatMenuList(item.children) : [])])


}

// 构建菜单树，用于渲染左侧导航栏
export const makeMenuTree = (menuList: Menu.MenuItem[]) => {
    const map = new Map<number, Menu.MenuItem>();
    const menuTree: Menu.MenuItem[] = []
    menuList.forEach(element => {
        map.set(element.id, { ...element, children: [] })
    });
    menuList.forEach(item => {
        const node = map.get(item.id);
        if (item.parentId) {
            const parent = map.get(item.parentId)
            if (parent && node) {
                console.log(parent, '-parent-', item)
                if (!parent.children) {
                    parent.children = []
                }
                parent.children.push(node)
            } else if (node) {
                menuTree.push(node)
            }

        } else if (node) {
            menuTree.push(node)
        }
    })
    return menuTree
}
