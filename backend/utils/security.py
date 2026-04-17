from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 👉 注册时用：加密密码
def hash_password(password: str):
    # 把明文密码变成加密字符串
    return pwd_context.hash(password)


# 校验密码
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
