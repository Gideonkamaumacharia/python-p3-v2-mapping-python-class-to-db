from __init__ import CURSOR, CONN

class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"


    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO departments (name,location) VALUES (?,?)
        """
        params = (self.name,self.location)
        CURSOR.execute(sql,params)
        CONN.commit()

        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls,name,location):
        department = Department(name,location)
        department.save()
        return department
    
    def update(self):
        sql = """
            UPDATE departments 
            SET name = ?, location = ?
            WHERE id = ?
        """
        params = (self.name,self.location,self.id)
        CURSOR.execute(sql,params)
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """

        CURSOR.execute(sql,(self.id,))
        CONN.commit()
