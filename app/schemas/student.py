from pydantic import BaseModel, EmailStr, Field


class StudentBase(BaseModel):
    """Các trường dữ liệu chung cho sinh viên."""
    full_name: str = Field(..., min_length=1, max_length=255, description="Họ và tên sinh viên")
    email: EmailStr = Field(..., description="Email sinh viên")
    major: str = Field(..., min_length=1, max_length=255, description="Ngành học")
    gpa: float = Field(..., ge=0, le=4, description="Điểm trung bình (0 - 4)")


class StudentCreate(StudentBase):
    """Schema dùng khi thêm mới sinh viên (POST /students)."""
    pass


class StudentUpdate(StudentBase):
    """Schema dùng khi cập nhật sinh viên (PUT /students/{student_id})."""
    pass


class StudentResponse(StudentBase):
    """Schema dùng khi trả dữ liệu sinh viên về cho client."""
    id: int

    class Config:
        from_attributes = True  # Cho phép đọc dữ liệu trực tiếp từ SQLAlchemy model
