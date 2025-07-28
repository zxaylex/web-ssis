from ..service import mysql

# student model
class Student:
    def __init__(self):
        id_number: str = None
        profile_url: str = None
        first_name: str = None 
        last_name: str = None
        program: str = None
        year_level: int = None
        gender: str = None 
        
    def __init__(self, id_number, profile_usel, first_name, last_name, program, year):
        self.id_number = id_number
        self.profile_usel = profile_usel
        self.first_name = first_name
        self.last_name = last_name
        self.program = program
        self.year_level = year
        
    def insert(self):
        sql = "INSERT INTO students (id_number, profile_url, first_name, last_name, program, year_level, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (self.id_number, self.profile_url, self.first_name, self.last_name, self.program, self.year_level, self.gender)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()
        
    def get(self):
        sql = "SELECT * FROM students WHERE id_number = %s"
        values = (self.id_number,)
        mysql.connect()
        result = mysql.execute(sql, values)
        if result.rowcount == 0:
            return None
        for key, value in result.fetchone().items():
            setattr(self, key, value)
        return self

    def update(self):
        sql = "UPDATE students SET profile_url = %s, first_name = %s, last_name = %s, program = %s, year_level = %s, gender = %s WHERE id_number = %s"
        values = (self.profile_url, self.first_name, self.last_name, self.program, self.year_level, self.gender, self.id_number)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()
    
    def delete(self):
        sql = "DELETE FROM students WHERE id_number = %s"
        values = (self.id_number,)
        mysql.connect()
        mysql.execute(sql, values)
        mysql.commit()