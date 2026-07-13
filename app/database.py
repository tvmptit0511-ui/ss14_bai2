import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ==============================
# Cấu hình kết nối MySQL
# ==============================
# Có thể chỉnh sửa thông tin kết nối trực tiếp tại đây,
# hoặc set biến môi trường DATABASE_URL trước khi chạy chương trình.
#
# Định dạng chuỗi kết nối MySQL:
# mysql+pymysql://<user>:<password>@<host>:<port>/<database_name>

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "student_management")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# echo=True giúp in ra các câu lệnh SQL để debug, có thể tắt khi deploy
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Dependency dùng cho FastAPI để lấy một session làm việc với database.
    Đảm bảo session luôn được đóng lại sau khi request kết thúc.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
