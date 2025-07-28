from ..service import csrf, mysql
from flask import Blueprint

program_bp = Blueprint('program', __name__, url_prefix='/program')


@program_bp.route('/')
def index():
    return "Welcome to program Portal"