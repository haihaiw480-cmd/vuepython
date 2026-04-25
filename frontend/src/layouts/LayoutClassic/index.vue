<template>
  <el-container>
    <el-header>
      <div class="hh-header-left">
        <div class="logo">
          <img class="logo-img" src="@/assets/images/hero.png" alt="" />
        </div>
      </div>
      <div class="hh-header-right"><ToolBarRight /></div>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <div class="aside-box" :style="{ width: '210px' }">
          <el-scrollbar>
            <!-- {{ menuList }} -->
            <el-menu :router="false" :collapse-transition="false">
              <MenuItem :menu-list="menuList" />
            </el-menu>
          </el-scrollbar>
        </div>
      </el-aside>
      <el-main>
        <div><router-view /></div>
      </el-main>
    </el-container>
  </el-container>
</template>
<script setup lang="ts" name="LayoutClassic">
import ToolBarRight from "@/layouts/components/header/ToolBarRight.vue";
import { useAuthStore } from "@/stores/auth";
import MenuItem from "../components/MenuItem/index.vue";
import { computed } from "vue";
const authStore = useAuthStore();
const menuList = authStore.authMenuListAllTree;
</script>
<style scoped lang="scss">
@import "./index.scss";
</style>
