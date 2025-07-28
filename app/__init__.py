from flask import Flask
from config import Config
from .service import csrf, mysql

from .routes.student import student_bp
from .routes.program import program_bp
from .routes.college import college_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    csrf.init_app(app)
    mysql.init_app(app)
    
    app.register_blueprint(student_bp)
    app.register_blueprint(program_bp)
    app.register_blueprint(college_bp)
    
    return app
