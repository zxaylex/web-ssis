from ..service import mysql

# student model
class Student:
    def __init__(self):
        self.id_number: str = None
        self.profile_url: str = None
        self.first_name: str = None 
        self.last_name: str = None
        self.program: str = None
        self.year_level: int = None
        self.gender: str = None 

    def __init__(self, id_number: str):
        self.id_number = id_number
        self.profile_url = None
        self.first_name = None
        self.last_name = None
        self.program = None
        self.year_level = None
        self.gender = None

    def __init__(self, id_number, profile_url, first_name, last_name, program, year_level, gender):
        self.id_number = id_number
        self.profile_usel = profile_url
        self.first_name = first_name
        self.last_name = last_name
        self.program = program
        self.year_level = year_level
        self.gender = gender

    def fetch(self):
        return self.get()
        
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