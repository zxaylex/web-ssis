from ..service import mysql, execute_query, fetch_one, execute_update

# student model
class Student:
    

    def __init__(self, id_number = None, profile_url = None, first_name = None, last_name = None, program = None, year_level = None, gender = None):
        self.id_number = id_number
        self.profile_url = profile_url
        self.first_name = first_name
        self.last_name = last_name
        self.program = program
        self.year_level = year_level
        self.gender = gender

    def set(self, id_number):
        self.id_number = id_number
        return self.get()
        
    def insert(self):
        sql = "INSERT INTO Student (id_number, profile_url, first_name, last_name, program, year_level, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (self.id_number, self.profile_url, self.first_name, self.last_name, self.program, self.year_level, self.gender)
        execute_update(sql, values)
        
    def get(self):
        sql = "SELECT * FROM Student WHERE id_number = %s"
        values = (self.id_number,)
        result = fetch_one(sql, values)
        if result is None:
            return None
        for key, value in result.items():
            setattr(self, key, value)
        return self

    def update(self):
        sql = "UPDATE Student SET profile_url = %s, first_name = %s, last_name = %s, program = %s, year_level = %s, gender = %s WHERE id_number = %s"
        values = (self.profile_url, self.first_name, self.last_name, self.program, self.year_level, self.gender, self.id_number)
        execute_update(sql, values)
    
    def delete(self):
        sql = "DELETE FROM Student WHERE id_number = %s"
        values = (self.id_number,)
        execute_update(sql, values)