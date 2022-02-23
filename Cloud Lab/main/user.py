
from pickle import NONE

class user():
    __id = None
    __loginname = None
    __password = None
    __dateCreated = None
    def __init__(self):
        pass
    
    def setId (self, id):
        self.__id = id
    
    def getId (self):
        return self.__id
    
    def setLogin (self, loginname):
        self.__loginname = loginname
    
    def getLogin (self):
        return self.__loginname
    
    def setPassword (self,password):
        self.__password = password
    
    def getPassword (self):
        return self.__password
    
    def getDateCreated (self):
        return self.__dateCreated
    
    def setDateCreated (self, dateCreated):
        self.__dateCreated = dateCreated