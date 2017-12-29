'''
Created on 13 nov 2013

@author: Yoieh
'''
import MySQLdb
from MySQLdb import *


class SQLUserDatabase():
    def __init__(self):
        self.sqlConnect = MySQLdb.connect('localhost', 'root', '', 'userdb')
        if self.sqlConnect:
            print "You are conected to Database: userdb"
        else:
            print "Conection error"
        self.cursor = self.sqlConnect.cursor()

    def creatUserDB(self):
        sqlConnect = MySQLdb.connect('localhost', 'root', '')
        cursor = sqlConnect.cursor()
        cursor.execute('CREATE DATABASE UserDB')

    def createUsersTable(self):
        self.cursor.execute(
            """CREATE TABLE users (
                                  id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                  name_user VARCHAR(100),
                                  password_user VARCHAR(100)
                                );"""
        )

    def selectUserWith_id(self, userId):
        self.cursor.execute(
            "SELECT * FROM users WHERE id_user='" + str(userId) + "'")
        self.userIdDB = self.cursor.fetchone()
        return self.userIdDB

    def selectUserWith_name(self, userName):
        self.cursor.execute(
            "SELECT * FROM users WHERE name_user='" + str(userName) + "'")
        self.userNameDB = self.cursor.fetchone()
        return self.userNameDB

    def selectUsers(self):
        self.cursor.execute("SELECT * FROM users")
        self.userDB = [element for element in self.cursor.fetchall()]
        return self.userDB

    def insertUser(self, userName, userPassword):
        #worldName, worldHight, worldWidth = self.safe(worldName), (worldHight), (worldWidth)
        self.selectUserWith_name(userName)
        if self.userNameDB == None:
            self.cursor.execute(
                """INSERT INTO users (name_user , password_user)
                                      VALUES (%s, %s)""",
                (str(userName), str(userPassword))
            )
            self.sqlConnect.commit()
            print "New User Created Called" + userName
        else:
            print "UserName do already exist"

    def updateUser(self):
        pass

# SQLUserDatabase().creatUserDB()
#SQLUserDatabase = SQLUserDatabase()
# SQLUserDatabase.createUsersTable()
#SQLUserDatabase.insertUser('Test2', 'test')
