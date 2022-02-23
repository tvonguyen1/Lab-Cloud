'''
Created on Feb 23, 2022

@author: nhatt
'''
import mysql.connector
from mysql.connector import Error
from main import user, exception
import traceback

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

statement = "SELECT count(*) FROM cloud_lab_sys.user_login WHERE login_name = %s AND password = %s"

vals = (username,passwd)



try:
    count = cursor.execute(statement,vals)
    cnx.commit()
    
    
    
    if count == 0:
        raise exception.valueError(Error)
    
    print("Succesfully login!")

except exception.valueError:
    print("Username or password is incorrect")
    
    
finally:
    cursor.close()
    cnx.close()
    
    
    