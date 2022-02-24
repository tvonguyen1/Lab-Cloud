'''
Created on Feb 23, 2022

@author: nhatt
'''
import mysql.connector
import exception
from mysql.connector import Error
import traceback

def login():
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

    statement = "SELECT * FROM cloud_lab_sys.user_login WHERE login_name = %s AND password = %s"

    vals = (username, passwd)

    try:
        cursor.execute(statement, vals)
        account = cursor.fetchone()

        if account:
            print("Successfully login")
        else:
            raise exception.valueError

    except exception.valueError:
        print("username or password is incorrect")
    finally:
        cnx.close()


login()
