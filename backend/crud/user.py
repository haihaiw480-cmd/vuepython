from models.user import User


def create_user(db, data):
    user = User(**data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db, data):
    user = db.query(User).filter_by(**data).first()
    return user


def get_user_by_username(db, username):
    return db.query(User).filter(User.username == username).first()
