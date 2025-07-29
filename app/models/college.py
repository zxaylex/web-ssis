from ..service import mysql


class College:
    def __init__(self, code: str = None, name: str = None):
        self.code = code
        self.name = name

    def __init__(self, code: str):
        self.code = code
        self.get()

    def fetch(self):
        return self.get()
    
    def insert(self):
        sql = "INSERT INTO colleges (code, name) VALUES (%s, %s)"
        values = (self.code, self.name)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()

    def get(self):
        sql = "SELECT * FROM colleges WHERE code = %s"
        values = (self.code,)
        mysql.connect()
        result = mysql.execute(sql, values)
        if result.rowcount == 0:
            return None
        for key, value in result.fetchone().items():
            setattr(self, key, value)
        return self

    def update(self):
        sql = "UPDATE colleges SET name = %s WHERE code = %s"
        values = (self.name, self.code)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()

    def delete(self):
        sql = "DELETE FROM colleges WHERE code = %s"
        values = (self.code,)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()