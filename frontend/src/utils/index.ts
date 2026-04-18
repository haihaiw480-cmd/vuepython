
export const flatMenuList = (menuList: Menu.MenuOptions[]): Menu.MenuOptions[] => {
    // 深拷贝：对象 → 转 JSON 字符串 → 再解析成新对象
    let newMenulist: Menu.MenuOptions[] = JSON.parse(JSON.stringify(menuList))
    return newMenulist.flatMap(item => [item, ...(item.children ? flatMenuList(item.children) : [])])


}
