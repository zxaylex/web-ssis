from ..service import csrf, mysql, fetch_all
from flask import Blueprint, render_template, jsonify, request
from ..models.student import Student

student_bp = Blueprint('student', __name__, url_prefix='/student')


@student_bp.route('/<string:student_id>')
def get_student(student_id: str):
    """Get a specific student by ID"""
    student = Student(student_id)
    result = student.get()
    
    if result is None:
        return jsonify({"error": "Student not found"}), 404
    
    return jsonify({
        "id_number": student.id_number,
        "profile_url": student.profile_url,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "program": student.program,
        "year_level": student.year_level,
        "gender": student.gender
    })


@student_bp.route('/')
def index():
    """Render the student management page"""
    return render_template('student.jinja2')


@student_bp.route('/api/')
def get_all_students():
    """Get all students"""
    sql = "SELECT * FROM Student"
    results = fetch_all(sql)
    
    students = []
    for row in results:
        student = Student()
        for key, value in row.items():
            setattr(student, key, value)
        students.append({
            "id_number": student.id_number,
            "profile_url": student.profile_url,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "program": student.program,
            "year_level": student.year_level,
            "gender": student.gender
        })
    
    return jsonify(students)


@student_bp.route('/create', methods=['POST'])
def create_student():
    """Create a new student"""
    data = request.get_json()
    
    student = Student()
    student.id_number = data.get('id_number')
    student.profile_url = data.get('profile_url')
    student.first_name = data.get('first_name')
    student.last_name = data.get('last_name')
    student.program = data.get('program')
    student.year_level = data.get('year_level')
    student.gender = data.get('gender')
    
    try:
        student.insert()
        return jsonify({"message": "Student created successfully", "student": {
            "id_number": student.id_number,
            "profile_url": student.profile_url,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "program": student.program,
            "year_level": student.year_level,
            "gender": student.gender
        }}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@student_bp.route('/<string:student_id>', methods=['PUT'])
def update_student(student_id: str):
    """Update a student"""
    data = request.get_json()
    
    student = Student(student_id)
    result = student.get()
    
    if result is None:
        return jsonify({"error": "Student not found"}), 404
    
    # Update fields if provided
    if 'profile_url' in data:
        student.profile_url = data['profile_url']
    if 'first_name' in data:
        student.first_name = data['first_name']
    if 'last_name' in data:
        student.last_name = data['last_name']
    if 'program' in data:
        student.program = data['program']
    if 'year_level' in data:
        student.year_level = data['year_level']
    if 'gender' in data:
        student.gender = data['gender']
    
    try:
        student.update()
        return jsonify({"message": "Student updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@student_bp.route('/<string:student_id>', methods=['DELETE'])
def delete_student(student_id: str):
    """Delete a student"""
    student = Student(student_id)
    result = student.get()
    
    if result is None:
        return jsonify({"error": "Student not found"}), 404
    
    try:
        student.delete()
        return jsonify({"message": "Student deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@student_bp.route('/program/<string:program_code>')
def get_students_by_program(program_code: str):
    """Get all students in a specific program"""
    sql = "SELECT * FROM Student WHERE program = %s"
    values = (program_code,)
    results = fetch_all(sql, values)
    
    students = []
    for row in results:
        student = Student()
        for key, value in row.items():
            setattr(student, key, value)
        students.append({
            "id_number": student.id_number,
            "profile_url": student.profile_url,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "program": student.program,
            "year_level": student.year_level,
            "gender": student.gender
        })
    
    return jsonify(students)


@student_bp.route('/year/<string:year_level>')
def get_students_by_year(year_level: str):
    """Get all students in a specific year level"""
    sql = "SELECT * FROM Student WHERE year_level = %s"
    values = (year_level,)
    results = fetch_all(sql, values)
    
    students = []
    for row in results:
        student = Student()
        for key, value in row.items():
            setattr(student, key, value)
        students.append({
            "id_number": student.id_number,
            "profile_url": student.profile_url,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "program": student.program,
            "year_level": student.year_level,
            "gender": student.gender
        })
    
    return jsonify(students)