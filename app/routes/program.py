from ..service import csrf, mysql, fetch_all
from flask import Blueprint, jsonify, request, render_template
from ..models.program import Program

program_bp = Blueprint('program', __name__, url_prefix='/program')


@program_bp.route('/')
def index():
    """Render the program management page"""
    return render_template('program.jinja2')


@program_bp.route('/api/')
def get_all_programs():
    """Get all programs"""
    sql = "SELECT * FROM Program"
    results = fetch_all(sql)
    
    programs = []
    for row in results:
        program = Program()
        for key, value in row.items():
            setattr(program, key, value)
        programs.append({
            "code": program.code,
            "name": program.name,
            "college": program.college
        })
    
    return jsonify(programs)


@program_bp.route('/<string:program_code>')
def get_program(program_code: str):
    """Get a specific program by code"""
    program = Program()
    program.code = program_code
    result = program.get()
    
    if result is None:
        return jsonify({"error": "Program not found"}), 404
    
    return jsonify({
        "code": program.code,
        "name": program.name,
        "college": program.college
    })


@program_bp.route('/create', methods=['POST'])
def create_program():
    """Create a new program"""
    data = request.get_json()
    
    program = Program()
    program.code = data.get('code')
    program.name = data.get('name')
    program.college = data.get('college')
    
    try:
        program.insert()
        return jsonify({"message": "Program created successfully", "program": {
            "code": program.code,
            "name": program.name,
            "college": program.college
        }}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@program_bp.route('/<string:program_code>', methods=['PUT'])
def update_program(program_code: str):
    """Update a program"""
    data = request.get_json()
    
    program = Program()
    program.code = program_code
    result = program.get()
    
    if result is None:
        return jsonify({"error": "Program not found"}), 404
    
    # Update fields if provided
    if 'name' in data:
        program.name = data['name']
    if 'college' in data:
        program.college = data['college']
    
    try:
        program.update()
        return jsonify({"message": "Program updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@program_bp.route('/<string:program_code>', methods=['DELETE'])
def delete_program(program_code: str):
    """Delete a program"""
    program = Program()
    program.code = program_code
    result = program.get()
    
    if result is None:
        return jsonify({"error": "Program not found"}), 404
    
    try:
        program.delete()
        return jsonify({"message": "Program deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@program_bp.route('/college/<string:college_code>')
def get_programs_by_college(college_code: str):
    """Get all programs for a specific college"""
    sql = "SELECT * FROM Program WHERE college = %s"
    values = (college_code,)
    results = fetch_all(sql, values)
    
    programs = []
    for row in results:
        program = Program()
        for key, value in row.items():
            setattr(program, key, value)
        programs.append({
            "code": program.code,
            "name": program.name,
            "college": program.college
        })
    
    return jsonify(programs)