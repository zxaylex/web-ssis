from ..service import csrf, mysql, execute_query, fetch_one, fetch_all, execute_update

class College:
    def __init__(self, code: str = None, name: str = None):
        self.code = code
        self.name = name
        
    def insert(self):
        sql = "INSERT INTO College (code, name) VALUES (%s, %s)"
        values = (self.code, self.name)
        execute_update(sql, values)
        
    def get(self):
        sql = "SELECT * FROM College WHERE code = %s"
        values = (self.code,)
        result = fetch_one(sql, values)
        if result is None:
            return None
        for key, value in result.items():
            setattr(self, key, value)
        return self
    
    def update(self):
        sql = "UPDATE College SET name = %s WHERE code = %s"
        values = (self.name, self.code)
        execute_update(sql, values)
        
    def delete(self):
        sql = "DELETE FROM College WHERE code = %s"
        values = (self.code,)
        execute_update(sql, values)
        
    def get_all(self):
        sql = "SELECT * FROM College"
        results = fetch_all(sql)
        colleges = []
        for row in results:
            college = College()
            for key, value in row.items():
                setattr(college, key, value)
            colleges.append(college)
        return colleges