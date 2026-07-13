from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


def get_students(db: Session):
    """Lấy toàn bộ danh sách sinh viên."""
    return db.query(Student).all()


def get_student_by_id(db: Session, student_id: int):
    """Lấy một sinh viên theo id. Trả về None nếu không tìm thấy."""
    return db.query(Student).filter(Student.id == student_id).first()


def create_student(db: Session, student_data: StudentCreate):
    """Thêm mới một sinh viên vào database."""
    new_student = Student(
        full_name=student_data.full_name,
        email=student_data.email,
        major=student_data.major,
        gpa=student_data.gpa,
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def update_student(db: Session, student_id: int, student_data: StudentUpdate):
    """
    Cập nhật thông tin sinh viên theo id.
    Trả về None nếu không tìm thấy sinh viên.
    """
    student = get_student_by_id(db, student_id)
    if not student:
        return None

    student.full_name = student_data.full_name
    student.email = student_data.email
    student.major = student_data.major
    student.gpa = student_data.gpa

    db.commit()
    db.refresh(student)
    return student


def delete_student(db: Session, student_id: int):
    """
    Xóa sinh viên theo id.
    Trả về True nếu xóa thành công, False nếu không tìm thấy sinh viên.
    """
    student = get_student_by_id(db, student_id)
    if not student:
        return False

    db.delete(student)
    db.commit()
    return True
