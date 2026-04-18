<template>
  <!--左侧 -->
  <component :is="layoutComponent" />
  <!--右侧 -->
  <!-- <div><router-view /></div> -->
</template>
<script setup lang="ts">
import LayoutClassic from "@/layouts/LayoutClassic/index.vue";
defineOptions({ name: "layout" });
const layoutComponent = LayoutClassic;
</script>
