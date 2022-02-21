'''
Created on Feb 18, 2022

@author: nina vo
project: cloud lab
sorenson impact center
'''
import mysql.connector
from datetime import date, datetime, timedelta

cnx = mysql.connector.connect(user='sev_ad', password='Nhattienvo21!',
                              host='cloud-lab-mysql.mysql.database.azure.com',
                              database='cloud_lab_sys')
cursor = cnx.cursor()
cnx.commit()

date = datetime.now().date + timedelta(days=1)



cursor.close()
cnx.close()
