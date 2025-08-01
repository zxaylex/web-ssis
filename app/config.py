from dotenv import load_dotenv
from os import getenv
load_dotenv()


class Config:
    SECRET_KEY = getenv("SECRET_KEY", "you-shall-not-pass")
    
    MYSQL_DATABASE_HOST = getenv("MYSQL_DATABASE_HOST", "localhost")
    MYSQL_DATABASE_USER = getenv("MYSQL_DATABASE_USER", "admin")
    MYSQL_DATABASE_PASSWORD = getenv("MYSQL_DATABASE_PASSWORD", "admin123")
    MYSQL_DATABASE_PORT = int(getenv("MYSQL_DATABASE_PORT", 3306))
    MYSQL_DATABASE_DB = getenv("MYSQL_DATABASE_DB", "student_system")
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = getenv("CSRF_SESSION_KEY", "csrf-secret-key")
    