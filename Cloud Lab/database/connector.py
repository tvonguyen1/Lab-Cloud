'''
Created on Feb 18, 2022

@author: nina vo
project: cloud lab
sorenson impact center
'''
import mysql.connector
from mysql.connector import Error
from database import queries
import traceback



class connector:
    queries = queries.queries()

    def register_user(self,user):
        cnx = mysql.connector.connect(user='sev_ad', password='Nhattienvo21!',
                                    host='cloud-lab-mysql.mysql.database.azure.com',
                                    database='cloud_lab_sys')
        
    
        statement = cnx._prepared_statements(queries.REGISTER)
        statement.setString(1, user.getLogin())
        statement.setString(2,user.getPassword())
        statement.setString(3,user.getDateCreated())
    
        try:
            cursor = cnx.cursor(prepared = True)
            cursor.execute(statement)
            cnx.commit()
    
        except Error:
            traceback.format_exc()
            print("The specified username already exists.")
         
        finally:
            cursor.close()
            cnx.close()

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
    


