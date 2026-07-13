from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Student(Base):
    """
    Model đại diện cho bảng 'students' trong MySQL.
    """
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    major = Column(String(255), nullable=False)
    gpa = Column(Float, nullable=False)
