'''
Created on Feb 22, 2022

@author: nhatt
'''
import datetime
from main import user, exception
from database import connector

class register:
    login_name = input("Enter username: ")
    password = input("Enter password: ")
    current_time = datetime.datetime.now()
    
    user = user.user()
    connector = connector.connector()
    exception = exception.nullValue()
    user.setLogin(login_name)
    user.setPassword(password)
    user.setDateCreated(current_time)
    connector.register_user(user)
      
   
        