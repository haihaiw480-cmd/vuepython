
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
export const selectMenuTree = (menuList: Menu.MenuItem[]) => {
    const menuTreeMap = new Map()
    const menuAll: Array<object> = []
    const menuTree: Array<object> = []
    menuList.forEach(item => {
        menuTreeMap.set(item.id, { ...item, children: [] })
    })
    menuList.forEach(item => {
        const node = menuTreeMap.get(item.id)
        const nodeOpthon = {
            label: node.name,
            value: node.id,
            children: node.children
        }
        if (item.parentId) {
            const parentNode = menuTreeMap.get(item.parentId)
            parentNode.children.push(nodeOpthon)
        } else {
            menuTree.push(nodeOpthon)
        }
    })
    menuAll.push({
        label: "主目录",
        value: undefined,
        children: menuTree
    })

    return menuAll
}
