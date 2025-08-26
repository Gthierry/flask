from sqlalchemy import Column, Integer, String
from app import db


class Users(db.Model):
    __tablename__ = "users"

    id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    name = Column("user_name", String(50))
    first_name = Column("user_firstname", String(50))
    email = Column("user_email", String(60), nullable=False, unique=True)
