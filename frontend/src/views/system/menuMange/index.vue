<script lang="ts" setup>
import { reactive, ref, onMounted } from "vue";
import { getMenuListAll, PostMenuAdd } from "@/api/menu/index";
import { type Menu } from "@/api/menu/interface";
import { type FormInstance, type FormRules } from "element-plus";
const currentPage4 = ref(4);
const pageSize4 = ref(100);
// ref<数组类型>(初始值)
const catalogue = ref<Menu.MenuListItem[]>([]);
const dialogFormVisible = ref(false);
const rules = reactive<FormRules<Menu.MenuListItem>>({
  name: [
    { required: true, message: "Please input Activity name", trigger: "blur" },
  ],
  routeName: [
    { required: true, message: "Please input Activity name", trigger: "blur" },
  ],
  path: [
    { required: true, message: "Please input Activity name", trigger: "blur" },
  ],
  type: [
    { required: true, message: "Please input Activity name", trigger: "blur" },
  ],
});
const menuFormRef = ref<FormInstance>();
const handleClick = () => {
  console.log("click");
};
const serchFrom = reactive<Menu.MenuParams>({});
const form = reactive<Menu.MenuListItem>({});
const tableData = ref<any[]>([]);
const handleMenuList = async () => {
  const res = await getMenuListAll();
  tableData.value = res.data.list;
};
// 获取全部目录
const getAllCatalogue = async () => {
  const { data } = await getMenuListAll({ type: 1 });
  catalogue.value = data.list;
  console.log(data, "data00000");
};
const handleOpen = async () => {
  //  获取目录
  await getAllCatalogue();
  dialogFormVisible.value = true;
};
const resetForm = async (menuFormRef: FormInstance | undefined) => {
  if (!menuFormRef) return;
  menuFormRef.resetFields();
  dialogFormVisible.value = false;
};

const submitForm = async (menuFormRef: FormInstance | undefined) => {
  if (!menuFormRef) return;
  console.log(
    menuFormRef.validate(async (value) => {
      if (value) {
        const data = await PostMenuAdd(form);
        console.log(data);
      }
    }),
    "menuFormRef",
  );
};
onMounted(() => {
  handleMenuList();
});
</script>

<template>
  <el-form :model="serchFrom" ref="menuSerchFormRef">
    <el-form-item label="菜单名称" prop="name">
      <el-input v-model="serchFrom.name" autocomplete="off" />
    </el-form-item>
    <el-form-item label="路由名称" prop="name">
      <el-input v-model="serchFrom.routeName" autocomplete="off" />
    </el-form-item>

    <el-form-item label="类型" prop="type">
      <el-select v-model="serchFrom.type" autocomplete="off">
        <el-option label="目录" :value="1" />
        <el-option label="菜单" :value="2" />
        <el-option label="按钮" :value="3" />
      </el-select>
    </el-form-item>
    <el-form-item label="是否隐藏" prop="is_hidden">
      <el-input v-model="serchFrom.is_hidden" autocomplete="off"> </el-input>
    </el-form-item>
  </el-form>
  <el-button @click="handleOpen"> 添加菜单 </el-button>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column fixed prop="name" label="菜单名称" width="150" />
    <el-table-column prop="icon" label="菜单图标" width="120" />
    <el-table-column prop="route_name" label="菜单 name" width="120" />
    <el-table-column prop="path" label="菜单路径" width="120" />
    <el-table-column prop="component" label="组件路径" width="100" />
    <el-table-column prop="parent_id" label="父级id" width="100" />
    <el-table-column prop="type" label="类型" width="100" />

    <el-table-column fixed="right" label="操作" min-width="120">
      <template #default>
        <el-button link type="primary" size="small" @click="handleClick">
          Detail
        </el-button>
        <el-button link type="primary" size="small">Edit</el-button>
      </template>
    </el-table-column>
  </el-table>
  {{ currentPage4 }}{{ pageSize4 }}
  <el-pagination
    v-model:current-page="currentPage4"
    v-model:page-size="pageSize4"
    layout="prev, pager, next"
    :total="1000"
  />
  <el-dialog v-model="dialogFormVisible" title="添加菜单" width="500">
    <el-form :model="form" :rules="rules" ref="menuFormRef">
      <el-form-item label="父级菜单" prop="parent_id">
        <el-select v-model="form.parent_id">
          <el-option
            v-for="item in catalogue"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="菜单名称" prop="name">
        <el-input v-model="form.name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="路由名称" prop="name">
        <el-input v-model="form.routeName" autocomplete="off" />
      </el-form-item>
      <el-form-item label="菜单图标" prop="icon">
        <el-input v-model="form.icon" autocomplete="off" />
      </el-form-item>
      <el-form-item label="路由路径" prop="path">
        <el-input v-model="form.path" autocomplete="off" />
      </el-form-item>
      <el-form-item label="组件路径" prop="component">
        <el-input v-model="form.component" autocomplete="off" />
      </el-form-item>
      <el-form-item label="类型" prop="type">
        <el-select v-model="form.type" autocomplete="off">
          <el-option label="目录" :value="1" />
          <el-option label="菜单" :value="2" />
          <el-option label="按钮" :value="3" />
        </el-select>
      </el-form-item>
      <el-form-item label="权限标识" prop="perms">
        <el-input v-model="form.perms" autocomplete="off"> </el-input>
      </el-form-item>
      <el-form-item label="是否隐藏" prop="is_hidden">
        <el-input v-model="form.is_hidden" autocomplete="off"> </el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="resetForm(menuFormRef)">Cancel</el-button>
        <el-button type="primary" @click="submitForm(menuFormRef)">
          Confirm
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>
