from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from database import Base, session


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)

    def __init__(self, username):
        self.username = username

    @classmethod
    @session
    def get_user(cls, id, db: Session = None):
        u = db.query(User).first()
        print(u.id, u.username)
