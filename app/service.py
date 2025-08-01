from flask_wtf.csrf import CSRFProtect
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

csrf = CSRFProtect()
mysql = MySQL()

# Helper function to get cursor and execute queries
def execute_query(sql, values=None):
    """Execute a SQL query and return the cursor"""
    cursor = mysql.connect().cursor(cursor=DictCursor)
    if values:
        cursor.execute(sql, values)
    else:
        cursor.execute(sql)
    return cursor

def fetch_all(sql, values=None):
    """Execute a query and return all results"""
    cursor = execute_query(sql, values)
    results = cursor.fetchall()
    cursor.close()
    return results

def fetch_one(sql, values=None):
    """Execute a query and return one result"""
    cursor = execute_query(sql, values)
    result = cursor.fetchone()
    cursor.close()
    return result

def execute_update(sql, values=None):
    """Execute an INSERT, UPDATE, or DELETE query"""
    cursor = execute_query(sql, values)
    mysql.connection.commit()
    cursor.close()
    return cursor.rowcount