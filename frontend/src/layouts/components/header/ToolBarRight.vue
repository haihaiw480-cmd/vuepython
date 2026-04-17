<script lang="ts" setup name="ToolBarRight"></script>
<template>
  <div>
    <ul>
      <li>语言</li>
      <li>搜索</li>
      <li>布局设置</li>
      <li>消息通知</li>
      <li>全屏</li>
      <li>用户名</li>
    </ul>
  </div>
</template>
<style scoped lang="scss">
ul {
  display: flex;
  align-items: center;
  gap: 20px;
  list-style: none;
  li {
    cursor: pointer;
  }
}
</style>
