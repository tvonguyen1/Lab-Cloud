'''
Created on Feb 22, 2022

@author: nhatt
'''
from datetime import date
import mysql.connector
from mysql.connector import Error
import traceback


def register():
    try:
        cnx = mysql.connector.connect(host='cloud-lab-mysql.mysql.database.azure.com',
                                      user='sev_ad',
                                      passwd='Nhattienvo21!',
                                      db='cloud_lab_sys')

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

    statement = "INSERT INTO cloud_lab_sys.user_login (login_name,password) VALUES (%s, %s)"

    vals = (username, passwd)

    try:
        cursor.execute(statement, vals)
        cnx.commit()

    except Error:
        print("Username already taken")

    finally:
        cursor.close()
        cnx.close()

register()
