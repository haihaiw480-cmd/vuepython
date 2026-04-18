<template>
  <div>
    <div @click="submitForm(ruleFormRef)">注册</div>
    <el-form
      ref="ruleFormRef"
      style="max-width: 600px"
      :model="ruleForm"
      status-icon
      :rules="rules"
      label-width="auto"
      class="demo-ruleForm"
    >
      <el-form-item label="用户名" prop="username">
        <el-input v-model="ruleForm.username" autocomplete="off" />
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input
          v-model="ruleForm.password"
          type="password"
          autocomplete="off"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="loginHandle(ruleFormRef)">
          Submit
        </el-button>
        <el-button @click="resetForm(ruleFormRef)">Reset</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script setup lang="ts" name="login">
import { HOME_URL } from "@/config/index";
import type { FormInstance, FormRules } from "element-plus";
import { getUserInfo, createUser, login, register } from "@/api/user";
import { ref, reactive } from "vue";
import { useUserStore } from "@/stores/user";
import { useAuthStore } from "@/stores/auth";
import { dynamicRouter } from "@/routers/modules/dynamicRouting";
import router from "@/routers";
const ruleFormRef = ref<FormInstance>();
const userStore = useUserStore();
const username = (rule: any, value: any, callback: any) => {
  if (!value) {
    return callback(new Error("Please input the age"));
  } else {
    callback();
  }
};
const validatePass = (rule: any, value: any, callback: any) => {
  console.log(value);
  if (!value) {
    callback(new Error("Please input the password"));
  } else {
    callback();
  }
};

const ruleForm = reactive({
  password: "",
  username: "",
});

const rules = reactive<FormRules<typeof ruleForm>>({
  password: [
    { validator: validatePass, trigger: "blur" },
    { required: true, message: "Please input Activity name", trigger: "blur" },
  ],
  username: [
    { validator: username, trigger: "blur" },
    { required: true, message: "Please input Activity name", trigger: "blur" },
  ],
});

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      // 注册账号
      handleRegister(ruleForm);
    } else {
      console.log("error submit!");
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.resetFields();
};

const handleRegister = (data: any) => {
  register({ ...data, password: data.password }).then(
    (res: { data: any } | any) => {
      console.log(res.data);
    },
  );
};
const loginHandle = (ruleFormRef: FormInstance | undefined) => {
  if (!ruleFormRef) return;
  ruleFormRef.validate(async (valid) => {
    if (valid) {
      // 登录账号
      const { data } = await login({ ...ruleForm });
      // pinia存储token
      userStore.setToken(data.access_token);
      // 获取动态路由 并添加到路由中
      await dynamicRouter();
      // 路由跳转到首页
      router.push(HOME_URL);
    } else {
      console.log("error submit!");
    }
  });
};
</script>
