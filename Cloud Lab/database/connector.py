'''
Created on Feb 18, 2022

@author: nina vo
project: cloud lab
sorenson impact center
'''
'''
import mysql.connector
from mysql.connector import Error
from database import queries
import traceback
from main.__main__ import register




    def login (self,user):
        cnx = mysql.connector.connect(user='sev_ad', password='Nhattienvo21!',
                                    host='cloud-lab-mysql.mysql.database.azure.com',
                                    database='cloud_lab_sys')
        queries = queries.queries()
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
    
'''

