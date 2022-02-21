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

cnx = mysql.connector.connect(user='sev_ad', password='Nhattienvo21!',
                                  host='cloud-lab-mysql.mysql.database.azure.com',
                                  database='cloud_lab_sys')

def register_user(user):
    
    statement = "INSERT INTO 'cloud_lab_sys'.'user_login' ('login_name', 'password','dateCreated') VALUES (?, ?, ?)"
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
