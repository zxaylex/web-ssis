from ..service import csrf, mysql, execute_query, fetch_one, execute_update

class Program:
    def __init__(self, code: str = None, name: str = None, college: str = None):
        self.code = code
        self.name = name
        self.college = college
        
    def insert(self):
        sql = "INSERT INTO Program (code, name, college) VALUES (%s, %s, %s)"
        values = (self.code, self.name, self.college)
        execute_update(sql, values)
    
    def get(self):
        sql = "SELECT * FROM Program WHERE code = %s"
        values = (self.code,)
        result = fetch_one(sql, values)
        if result is None:
            return None
        for key, value in result.items():
            setattr(self, key, value)
        return self
    
    def update(self):
        sql = "UPDATE Program SET name = %s, college = %s WHERE code = %s"
        values = (self.name, self.college, self.code)
        execute_update(sql, values)
        
    def delete(self):
        sql = "DELETE FROM Program WHERE code = %s"
        values = (self.code,)
        execute_update(sql, values)