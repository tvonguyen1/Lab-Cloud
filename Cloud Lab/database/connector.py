'''
Created on Feb 18, 2022

@author: nina vo
project: cloud lab
sorenson impact center
'''
import mysql.connector
from mysql.connector import MySQLConnection, Error
from datetime import date, datetime, timedelta

def update_user(id,login,password,dateCreated):
    date = datetime.now().date + timedelta(days=1)
    
    
    
    
try:
    cnx = mysql.connector.connect(user='sev_ad', password='Nhattienvo21!',
                                  host='cloud-lab-mysql.mysql.database.azure.com',
                                  database='cloud_lab_sys')
    cursor = cnx.cursor()
    cnx.commit()

    

except Error as error:
    print(error)
    
finally:
    cursor.close()
    cnx.close()
