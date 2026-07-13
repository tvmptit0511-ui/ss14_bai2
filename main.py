from fastapi import FastAPI

from app.database import Base, engine
from app.models import student as student_model  # noqa: F401  (import để Base biết bảng students)
from app.routers import student as student_router

# Tạo bảng trong MySQL nếu bảng chưa tồn tại
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="API quản lý sinh viên (CRUD) sử dụng FastAPI + SQLAlchemy + MySQL",
    version="1.0.0",
)

# Gắn router quản lý sinh viên vào app
app.include_router(student_router.router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Student Management API đang chạy. Truy cập /docs để xem tài liệu API."}
