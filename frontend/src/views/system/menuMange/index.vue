<script lang="ts" setup>
import { ref } from "vue";
const currentPage4 = ref(4);
const pageSize4 = ref(100);
const handleClick = () => {
  console.log("click");
};

const tableData = [
  {
    date: "2016-05-03",
    name: "Tom",
    state: "California",
    city: "Los Angeles",
    address: "No. 189, Grove St, Los Angeles",
    zip: "CA 90036",
    tag: "Home",
  },
  {
    date: "2016-05-02",
    name: "Tom",
    state: "California",
    city: "Los Angeles",
    address: "No. 189, Grove St, Los Angeles",
    zip: "CA 90036",
    tag: "Office",
  },
  {
    date: "2016-05-04",
    name: "Tom",
    state: "California",
    city: "Los Angeles",
    address: "No. 189, Grove St, Los Angeles",
    zip: "CA 90036",
    tag: "Home",
  },
  {
    date: "2016-05-01",
    name: "Tom",
    state: "California",
    city: "Los Angeles",
    address: "No. 189, Grove St, Los Angeles",
    zip: "CA 90036",
    tag: "Office",
  },
];
</script>

<template>
  <el-button> 添加菜单 </el-button>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column fixed prop="date" label="菜单名称" width="150" />
    <el-table-column prop="name" label="菜单图标" width="120" />
    <el-table-column prop="state" label="菜单 name" width="120" />
    <el-table-column prop="city" label="菜单路径" width="120" />
    <el-table-column prop="address" label="组件路径" width="600" />
    <el-table-column fixed="right" label="操作" min-width="120">
      <template #default>
        <el-button link type="primary" size="small" @click="handleClick">
          Detail
        </el-button>
        <el-button link type="primary" size="small">Edit</el-button>
      </template>
    </el-table-column>
  </el-table>
  <el-pagination
    v-model:current-page="currentPage4"
    v-model:page-size="pageSize4"
    layout="prev, pager, next"
    :total="1000"
  />
</template>
