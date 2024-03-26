

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from routes import db



class UserInfo(db.Model):
    __tablename__ = 'userinfo'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userid: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    userpwd: Mapped[str] = mapped_column(String(45), nullable=False)



