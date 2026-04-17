from models.user import User
from sqlalchemy.exc import IntegrityError


# todo: 密码加密存储
def create_user(db, data):
    try:
        user = User(**data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        return {"code": 400, "msg": "用户名已存在"}


def get_user_all(db):
    user = db.query(User).all()
    return user


def get_user_by_username(db, username):
    return db.query(User).filter(User.username == username).first()
