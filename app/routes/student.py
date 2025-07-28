from ..service import csrf, mysql
from flask import Blueprint

student_bp = Blueprint('student', __name__, url_prefix='/student')


@student_bp.route('/<string:student_id>')
def get_student(student_id: str):
    return f"Details for student with ID: {student_id}"

@student_bp.route('/')
def index():
    return "Welcome to Student Portal"