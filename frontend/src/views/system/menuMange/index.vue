<script lang="ts" setup>
import { reactive, ref, onMounted } from "vue";
import { getMenuListAll, PostMenuAdd, deletetMenu } from "@/api/menu/index";
import { type FormInstance, type FormRules, ElMessage } from "element-plus";
import { makeMenuTree } from "@/utils/index";

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

const menuFormRef = ref<FormInstance>();

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
};

// 编辑
const handleClick = async (row: Menu.MenuItem) => {
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

  await PostMenuAdd(form);
  ElMessage.success("提交成功");

  dialogFormVisible.value = false;
  handleMenuList();
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
  <el-dialog v-model="dialogFormVisible" title="菜单" width="500">
    <el-form :model="form" :rules="rules" ref="menuFormRef">
      <el-form-item label="父级菜单" prop="parentId">
        <el-input v-model="form.parentId" />
      </el-form-item>

      <el-form-item label="菜单名称" prop="name">
        <el-input v-model="form.name" />
      </el-form-item>

      <el-form-item label="路由名称" prop="routeName">
        <el-input v-model="form.routeName" />
      </el-form-item>

      <el-form-item label="图标" prop="icon">
        <el-input v-model="form.icon" />
      </el-form-item>

      <el-form-item label="路径" prop="path">
        <el-input v-model="form.path" />
      </el-form-item>

      <el-form-item label="组件" prop="component">
        <el-input v-model="form.component" />
      </el-form-item>

      <el-form-item label="类型" prop="type">
        <el-select v-model="form.type">
          <el-option label="目录" :value="1" />
          <el-option label="菜单" :value="2" />
          <el-option label="按钮" :value="3" />
        </el-select>
      </el-form-item>

      <el-form-item label="权限" prop="perms">
        <el-input v-model="form.perms" />
      </el-form-item>

      <el-form-item label="是否隐藏" prop="isHidden">
        <el-input v-model="form.isHidden" />
      </el-form-item>
    </el-form>

    <template #footer>
      <el-button @click="resetForm">取消</el-button>
      <el-button type="primary" @click="submitForm">提交</el-button>
    </template>
  </el-dialog>
</template>
