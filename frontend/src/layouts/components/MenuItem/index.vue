<script setup lang="ts" name="MenuItem">
import { useRouter } from "vue-router";

const modules = import.meta.glob("@/views/**/*.vue");
const router = useRouter();
// import * as Icons from "@element-plus/icons-vue";
// name="MenuItem" 不等于组件注册名👉 Vue 不会自动把 MenuItem 这个名字用于递归引用
defineOptions({
  name: "MenuItem",
});

defineProps<{ menuList: Menu.MenuItem[] }>();
// 路由跳转
const handleClickMenu = (subItem: Menu.MenuItem) => {
  console.log(
    subItem,
    `/src/views${subItem.component}.vue`,
    modules[`/src/views${subItem.component}.vue`],
  );
  console.log(router);
  router.push(subItem.path);
};
</script>

<template>
  <template v-for="subItem in menuList" :key="subItem.path">
    <el-sub-menu v-if="subItem.children?.length" :index="subItem.path">
      <template #title>
        <el-icon v-if="subItem.icon"> </el-icon>
        <span class="sle">{{ subItem.name }}</span>
      </template>

      <MenuItem :menu-list="subItem.children" />
    </el-sub-menu>
    <el-menu-item
      v-else
      :index="subItem.path"
      @click="handleClickMenu(subItem)"
    >
      <template #title>
        <el-icon v-if="subItem.icon"> </el-icon>
        <span class="sle">{{ subItem.name }}</span>
      </template>
    </el-menu-item>
  </template>
</template>
