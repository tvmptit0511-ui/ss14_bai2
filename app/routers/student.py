from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse
from app.services import student as student_service

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.get("", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    """Lấy danh sách toàn bộ sinh viên."""
    return student_service.get_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    """Lấy chi tiết một sinh viên theo id."""
    student = student_service.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Không tìm thấy sinh viên có id = {student_id}",
        )
    return student


@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student_data: StudentCreate, db: Session = Depends(get_db)):
    """Thêm mới một sinh viên."""
    return student_service.create_student(db, student_data)


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student_data: StudentUpdate, db: Session = Depends(get_db)):
    """Cập nhật thông tin sinh viên theo id."""
    student = student_service.update_student(db, student_id, student_data)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Không tìm thấy sinh viên có id = {student_id}",
        )
    return student


@router.delete("/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """Xóa sinh viên theo id."""
    deleted = student_service.delete_student(db, student_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Không tìm thấy sinh viên có id = {student_id}",
        )
    return {"message": f"Đã xóa sinh viên có id = {student_id}"}
