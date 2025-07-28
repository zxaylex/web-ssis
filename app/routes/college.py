from ..service import csrf, mysql
from flask import Blueprint

college_bp = Blueprint('college', __name__, url_prefix='/college')


@college_bp.route('/')
def index():
    return "Welcome to college Portal"