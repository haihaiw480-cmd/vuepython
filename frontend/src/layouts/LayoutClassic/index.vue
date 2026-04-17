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
            <el-menu :router="false"> </el-menu>
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
</script>
<style scoped lang="scss">
@import "./index.scss";
</style>
