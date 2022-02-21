'''
Created on Feb 21, 2022

@author: nhatt
'''

class queries:
    LOGIN = "SELECT count(*) FROM cloud_lab_sys.user_login WHERE login_name = ? AND password =?"
    REGISTER = "INSERT INTO 'cloud_lab_sys'.'user_login' ('login_name', 'password','dateCreated') VALUES (?, ?, ?)"
    RETRIEVE_PASSWORD = "SELECT password FROM cloud_lab_user.user_login WHERE login_name = ? AND answer =?"
    RETRIEVE_USER_ID = "SELECT id FROM cloud_lab_user.user_login WHERE login_name = ?";
    
