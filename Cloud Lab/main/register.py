'''
Created on Feb 22, 2022

@author: nhatt
'''
from datetime import date
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import traceback


def register():
    try:
        cnx = mysql.connector.connect(host='35.196.243.170',
                                      user='root',
                                      passwd='Nhattienvo21!',
                                      db='cloud_schema')

    except mysql.connector.Error as e:
        if e.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with username or Password")
        elif e.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database Does not exist")
        else:
            print(e)

    cursor = cnx.cursor()

    username = input("Enter username: ")
    passwd = input("Enter password: ")

    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    statement = "INSERT INTO cloud_schema.user_login (login_name,password,date_create) VALUES (%s, %s, %s)"

    vals = (username, passwd, formatted_date)

    try:
        cursor.execute(statement, vals)
        cnx.commit()

    except Error:
        print("Username already taken")

    finally:
        cursor.close()
        cnx.close()


register()
