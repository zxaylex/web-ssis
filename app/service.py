from flask_wtf.csrf import CSRFProtect
from flaskext.mysql import MySQL

csrf = CSRFProtect()
mysql = MySQL()