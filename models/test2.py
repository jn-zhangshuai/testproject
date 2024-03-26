from datetime import datetime


from flask_login import UserMixin

from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from flask_sqlalchemy import SQLAlchemy

from routes import db,login_manager

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userid: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    userpwd: Mapped[str] = mapped_column(String(45), nullable=False)


    def check_password_correction(self, attempted_password):
        
        return attempted_password == self.userpwd
