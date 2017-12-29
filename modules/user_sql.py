'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from MySQLdb import connect


class SQLUserDatabase(object):
    """ Connection to user db """

    def __init__(self):
        self.sql_connect = connect('localhost', 'root', '', 'userdb')
        if self.sql_connect:
            print "You are conected to Database: userdb"
        else:
            print "Conection error"
        self.cursor = self.sql_connect.cursor()

    def creat_user_db(self):
        """ Creating user db """
        sql_connect = connect('localhost', 'root', '')
        cursor = sql_connect.cursor()
        cursor.execute('CREATE DATABASE UserDB')

    def create_users_table(self):
        """ Creating user table """
        self.cursor.execute(
            """CREATE TABLE users (
                                  id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                  name_user VARCHAR(100),
                                  password_user VARCHAR(100)
                                );"""
        )

    def select_user_with_id(self, user_id):
        """ Selecting user with user_id """
        self.cursor.execute(
            "SELECT * FROM users WHERE id_user='" + str(user_id) + "'")
        return self.cursor.fetchone()

    def select_user_with_name(self, user_name):
        """ Selects user with user_name """
        self.cursor.execute(
            "SELECT * FROM users WHERE name_user='" + str(user_name) + "'")
        return self.cursor.fetchone()

    def select_users(self):
        """ Selects all users """
        self.cursor.execute("SELECT * FROM users")
        return [element for element in self.cursor.fetchall()]

    def insert_user(self, user_name, user_password):
        """ Inserts a user with user_name and user_password """
        #worldName, worldHight, worldWidth = self.safe(worldName), (worldHight), (worldWidth)
        user_name_bd = self.select_user_with_name(user_name)
        if user_name_bd is not None:
            self.cursor.execute(
                """INSERT INTO users (name_user , password_user)
                                      VALUES (%s, %s)""",
                (str(user_name), str(user_password))
            )
            self.sql_connect.commit()
            print "New User Created Called" + user_name
        else:
            print "UserName do already exist"

    def update_user(self):
        """ dont know """
        pass

# SQLUserDatabase().creat_user_db()
#SQLUserDatabase = SQLUserDatabase()
# SQLUserDatabase.create_users_table()
#SQLUserDatabase.insertUser('Test2', 'test')
