from flask_login import login_user
from sqlalchemy import Select

from models.test2 import User
from models.test3 import UserInfo
from routes import db


class UserService:
    def do_login(self, username: str, password: str) -> bool:
        query = Select(User).where(User.userid == username)
        attempted_user = db.session.scalar(query)
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=password
        ):
            login_user(attempted_user)
            return True

        return False
    def do_adduser(self, user:UserInfo):
        query = Select(UserInfo).where(UserInfo.userid == user.userid)
        exist_user = db.session.scalars(query).all()
        if exist_user:
            return user, 'user is exits!!'
        db.session.add(user)
        db.session.add(user)
        db.session.commit
        return user,None