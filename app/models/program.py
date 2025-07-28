from ..service import csrf, mysql

class Program:
    def __init__(self, code: string, name: string, college: string):
        self.code = code
        self.name = name
        self.college = college

    def __init__(self):
        self.code: str = None
        self.name: str = None
        self.college: str = None
        
    def insert(self):
        sql = "INSERT INTO programs (code, name, college) VALUES (%s, %s, %s)"
        values = (self.code, self.name, self.college)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()
    
    def get(self):
        sql = "SELECT * FROM programs WHERE code = %s"
        values = (self.code,)
        mysql.connect()
        result = mysql.execute(sql, values)
        if result.rowcount == 0:
            return None
        for key, value in result.fetchone().items():
            setattr(self, key, value)
        return self
    
    def update(self):
        sql = "UPDATE programs SET name = %s, college = %s WHERE code = %s"
        values = (self.name, self.college, self.code)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()
        
    def delete(self):
        sql = "DELETE FROM programs WHERE code = %s"
        values = (self.code,)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()