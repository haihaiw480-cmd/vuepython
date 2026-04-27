<script lang="ts" setup>
import { reactive, ref, onMounted } from "vue";
import {
  getMenuListAll,
  PostMenuAdd,
  deletetMenu,
  patchMenu,
} from "@/api/menu/index";
import { type FormInstance, type FormRules, ElMessage } from "element-plus";
import { makeMenuTree, selectMenuTree } from "@/utils/index";

/* ================= 基础状态 ================= */

const tableData = ref<Menu.MenuItem[]>([]);
const dialogFormVisible = ref(false);
/* ================= 表单 ================= */
const defaultForm: Menu.CreatMenuPrams = {
  name: "",
  routeName: "",
  path: "",
  component: "",
  parentId: undefined,
  sort: undefined,
  type: 1,
  perms: "",
  icon: "",
  isHidden: 0,
};
const form = reactive<Menu.CreatMenuPrams>({ ...defaultForm });
const editId = ref<number>();
const menuFormRef = ref<FormInstance>();
const dialogTitle = ref<string>();
const type = ref<string>();
const treeSelect = reactive([]);

/* ================= 校验 ================= */

const rules: FormRules<Menu.CreatMenuPrams> = {
  name: [{ required: true, message: "请输入菜单名称", trigger: "blur" }],
  routeName: [{ required: true, message: "请输入路由名称", trigger: "blur" }],
  path: [{ required: true, message: "请输入路径", trigger: "blur" }],
  type: [{ required: true, message: "请选择类型", trigger: "change" }],
};

/* ================= 工具函数 ================= */

// 统一处理 list / 分页
const getList = (data: any): Menu.MenuItem[] =>
  Array.isArray(data) ? data : data?.list || [];

/* ================= 业务逻辑 ================= */

// 获取菜单列表
const handleMenuList = async () => {
  const { data, code } = await getMenuListAll();
  if (code !== 200) return;
  const list = getList(data);
  tableData.value = makeMenuTree(list);
  Object.assign(treeSelect, selectMenuTree(list));
};

// 编辑
const handleClick = async (row: Menu.MenuItem) => {
  dialogTitle.value = "编辑菜单";
  type.value = "edit";
  editId.value = row.id;
  const { data, code, msg } = await getMenuListAll({ id: row.id });
  if (code !== 200) {
    ElMessage.error(msg);
    return;
  }
  const list = getList(data);
  const item = list[0];
  if (!item) return;
  Object.assign(form, item);
  dialogFormVisible.value = true;
};

// 删除
const handleDelete = async (row: Menu.MenuItem) => {
  await deletetMenu(row.id);
  ElMessage.success("删除成功");
  handleMenuList();
};

// 打开弹窗（新增）
const handleOpen = () => {
  dialogTitle.value = "新增菜单";
  type.value = "add";
  Object.assign(form, defaultForm);
  dialogFormVisible.value = true;
};

// 重置
const resetForm = () => {
  menuFormRef.value?.resetFields();
  dialogFormVisible.value = false;
};

// 提交
const submitForm = async () => {
  await menuFormRef.value?.validate();
  if (type.value == "add") {
    await PostMenuAdd(form);
    ElMessage.success("提交成功");
  } else {
    if (editId.value !== undefined) {
      patchMenu(editId.value, form);
    }
  }
  handleMenuList();
  dialogFormVisible.value = false;
  function leetcode(nums: Array<number>) {
    let i = 0;
    while (i < nums.length) {
      if (2 * i >= nums.length) {
        i++;
      } else {
        return i - 1;
      }
    }
  }
};

onMounted(handleMenuList);
</script>
<template>
  <!-- 查询 -->
  <el-form>
    <el-form-item label="菜单名称">
      <el-input />
    </el-form-item>
  </el-form>

  <el-button @click="handleOpen">添加菜单</el-button>

  <!-- 表格 -->
  <el-table
    :data="tableData"
    row-key="id"
    default-expand-all
    style="width: 100%"
  >
    <el-table-column prop="name" label="菜单名称" width="150" />
    <el-table-column prop="icon" label="图标" width="120" />
    <el-table-column prop="routeName" label="路由 name" />
    <el-table-column prop="path" label="路径" />
    <el-table-column prop="component" label="组件" />
    <el-table-column prop="parentId" label="父级ID" />
    <el-table-column prop="type" label="类型" />

    <el-table-column label="操作">
      <template #default="scope">
        <el-button link type="primary" @click="handleClick(scope.row)">
          编辑
        </el-button>
        <el-button link type="danger" @click="handleDelete(scope.row)">
          删除
        </el-button>
      </template>
    </el-table-column>
  </el-table>

  <!-- 弹窗 -->
  <el-dialog v-model="dialogFormVisible" :title="dialogTitle" width="800">
    <el-form :model="form" :rules="rules" ref="menuFormRef">
      <el-row :gutter="10">
        <el-form-item label="父级菜单" prop="parentId">
          <el-tree-select
            v-model="form.parentId"
            :data="treeSelect"
            :render-after-expand="false"
            style="width: 240px"
          />
        </el-form-item>
      </el-row>
      <el-row :gutter="10">
        <el-form-item label="类型" prop="type">
          <el-radio-group v-model="form.type">
            <el-radio :value="1">目录</el-radio>
            <el-radio :value="2">菜单</el-radio>
            <el-radio :value="3">按钮</el-radio>
          </el-radio-group>
        </el-form-item>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="12">
          <el-form-item label="菜单图标" prop="icon">
            <el-input v-model="form.icon" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="显示排序" prop="icon">
            <el-input v-model="form.icon" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="12">
          <el-form-item label="菜单名称" prop="name">
            <el-input v-model="form.name" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="路由名称" prop="routeName">
            <el-input v-model="form.routeName" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="12">
          <el-form-item label="是否外链" prop="routeName">
            <el-input v-model="form.routeName" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="路由地址" prop="path">
            <el-input v-model="form.path" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="12">
          <el-form-item label="是否缓存" prop="isHidden">
            <el-input v-model="form.isHidden" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="路由参数" prop="isHidden">
            <el-input v-model="form.isHidden" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="12">
          <el-form-item label="是否隐藏" prop="isHidden">
            <el-input v-model="form.isHidden" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="菜单状态" prop="isHidden">
            <el-input v-model="form.isHidden" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="12">
          <el-form-item label="组件路径" prop="component">
            <el-input v-model="form.component" />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="权限" prop="perms">
            <el-input v-model="form.perms" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <template #footer>
      <el-button @click="resetForm">取消</el-button>
      <el-button type="primary" @click="submitForm">提交</el-button>
    </template>
  </el-dialog>
</template>
