'''
Created on Feb 21, 2022

@author: nhatt
'''

class queries():
    def __init__(self):
        self.LOGIN = "SELECT count(*) FROM cloud_lab_sys.user_login WHERE login_name = ? AND password =?"
        self.REGISTER = "INSERT INTO cloud_lab_sys.user_login (login_name, password,dateCreated) VALUES (%s, %s, %s)"
        self.RETRIEVE_PASSWORD = "SELECT password FROM cloud_lab_user.user_login WHERE login_name = ? AND answer =?"
        self.RETRIEVE_USER_ID = "SELECT id FROM cloud_lab_user.user_login WHERE login_name = ?"
    

