'''
Created on Feb 22, 2022

@author: nhatt
'''
from datetime import date
from main import user, exception
import mysql.connector
from mysql.connector import Error
import traceback

try:
    cnx = mysql.connector.connect(host='cloud-lab-mysql.mysql.database.azure.com',
                                  port=3306 ,user='sev_ad', passwd='Nhattienvo21!',
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
current_time = date.today()
    
statement = "INSERT INTO cloud_lab_sys.user_login (login_name,password,date_created) VALUES (%s, %s, %s)"
    
vals = (username, passwd, current_time)
    
try:
    cursor.execute(statement,vals)
    cnx.commit()
    
except Error:
        traceback.format_exc()
        
         
finally:
    cursor.close()
    cnx.close()
    
    
    
    
      
   
        