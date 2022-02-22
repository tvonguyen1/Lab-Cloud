'''
Created on Feb 18, 2022

@author: nina vo
project: cloud lab
sorenson impact center
'''
import mysql.connector
from mysql.connector import MySQLConnection, Error
from datetime import date, datetime, timedelta
import main_activity
from database.queries import queries
from mysqlx import statement

cnx = mysql.connector.connect(user='sev_ad', password='Nhattienvo21!',
                                  host='cloud-lab-mysql.mysql.database.azure.com',
                                  database='cloud_lab_sys')

def register_user(user):
    
    statement = cnx._prepared_statements(queries.REGISTER)
    statement.setString(1, user.getLogin())
    statement.setString(2,user.getPassword())
    statement.setString(3,user.getDateCreated())
    
    try:
        cursor = cnx.cursor(prepared = True)
        cursor.execute(statement)
        cnx.commit()
    
    except Error as error:
        print(error)
    
    finally:
        cursor.close()
        cnx.close()

def login (user):
    statement = cnx._prepared_statements(queries.LOGIN)
    statement.setString(1,user.getLogin())
    statement.setString(2,user.getPassword())
    
    resultSet = statement.executeQuery
    
    count = 0
    
    while resultSet.next():
        print("Number of Users: " + resultSet.getInt(1))
        count = resultSet.getInt(1)
        
    if count == 0:
        raise ValueError(statement.setString(2,user.getPassword()))
    


