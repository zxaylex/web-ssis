from ..service import csrf, mysql, fetch_all
from flask import Blueprint, jsonify, request, render_template
from ..models.college import College

college_bp = Blueprint('college', __name__, url_prefix='/college')


@college_bp.route('/')
def index():
    """Render the college management page"""
    return render_template('college.jinja2')


@college_bp.route('/api/')
def get_all_colleges():
    """Get all colleges"""
    sql = "SELECT * FROM College"
    results = fetch_all(sql)
    
    colleges = []
    for row in results:
        college = College()
        for key, value in row.items():
            setattr(college, key, value)
        colleges.append({
            "code": college.code,
            "name": college.name
        })
    
    return jsonify(colleges)


@college_bp.route('/<string:college_code>')
def get_college(college_code: str):
    """Get a specific college by code"""
    college = College()
    college.code = college_code
    result = college.get()
    
    if result is None:
        return jsonify({"error": "College not found"}), 404
    
    return jsonify({
        "code": college.code,
        "name": college.name
    })


@college_bp.route('/create', methods=['POST'])
def create_college():
    """Create a new college"""
    data = request.get_json()
    
    college = College()
    college.code = data.get('code')
    college.name = data.get('name')
    
    try:
        college.insert()
        return jsonify({"message": "College created successfully", "college": {
            "code": college.code,
            "name": college.name
        }}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@college_bp.route('/<string:college_code>', methods=['PUT'])
def update_college(college_code: str):
    """Update a college"""
    data = request.get_json()
    
    college = College()
    college.code = college_code
    result = college.get()
    
    if result is None:
        return jsonify({"error": "College not found"}), 404
    
    # Update fields if provided
    if 'name' in data:
        college.name = data['name']
    
    try:
        college.update()
        return jsonify({"message": "College updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@college_bp.route('/<string:college_code>', methods=['DELETE'])
def delete_college(college_code: str):
    """Delete a college"""
    college = College()
    college.code = college_code
    result = college.get()
    
    if result is None:
        return jsonify({"error": "College not found"}), 404
    
    try:
        college.delete()
        return jsonify({"message": "College deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400