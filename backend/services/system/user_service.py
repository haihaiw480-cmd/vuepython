from repositories.user_repository import UserRepository
from core.exceptions import BizException
from fastapi import HTTPException
from utils.jwt import verify_token, create_access_token
from utils.security import hash_password, verify_password
from schemas.user import UserLogin


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    async def create_user(self, db, data):
        date_dict = data.model_dump()
        hasname = await self.get_user(db, data.username)
        if hasname:
            raise HTTPException(status_code=400, detail="用户名已存在")
        # 可以加业务逻辑（比如密码加密）
        hashPassword = hash_password(date_dict['password'])
        date_dict['password'] = hashPassword
        return await self.repo.create(db, date_dict)

    async def update_user(self, db, user_id: int, data: dict):
        hasId = await self.get_user(db, user_id)
        if not hasId:
            raise HTTPException(status_code=400, detail="该用户不存在")
        return await self.repo.update(db, user_id, data)

    async def get_user(self, db, username=None, user_id=None):
        return await self.repo.get(db, id=user_id, username=username)

    async def get_user_by_name(self, db, user_name):
        return await self.repo.get(db, username=user_name)

    async def login_by_password(
        self,
        db,
        params: UserLogin,
    ):
        username = params.username
        password = params.password
        if not password:
            raise HTTPException(status_code=400, detail="密码不能为空")
        userInfo = await self.get_user(db, user_id=None, username=username)

        if not userInfo:
            raise HTTPException(status_code=400, detail="该用户不存在")

        is_ture_password = verify_password(password, userInfo[0].password)
        if is_ture_password:
            token = create_access_token(params.model_dump())
            return {'token': token}
        # 生成token

        # verify_password(password,userInfo.password)
