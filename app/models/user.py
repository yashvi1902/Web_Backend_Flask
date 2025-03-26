
from .. import mysql
from werkzeug.security import check_password_hash


class User:
    def __init__(self, username, password,id=None):
        self.id = id
        self.username = username
        self.password = password
    
        

    @classmethod
    def get_user_by_username(cls, username):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cur.fetchone()
        cur.close()
        if user_data:
            return cls(user_data[1], user_data[2])  
        return None
    
    @classmethod
    def create_user(cls, username, password):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()

    @classmethod
    def check_password(cls, password, stored_password):
        # This method should implement password hashing comparison in production
        return password == stored_password  # This is just a simple comparison for now
