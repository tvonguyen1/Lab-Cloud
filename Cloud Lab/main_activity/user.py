from django.contrib.auth.password_validation import password_changed
class user:
    def __init__ (self,id, loginname, password, dateCreated):
        self.id = id
        self.loginname = loginname
        self.password = password
        self.dateCreated = dateCreated
    
    def setId (self, id):
        self.id = id
    
    def getId (self):
        return self.id
    
    def setLogin (self, loginname):
        self.loginname = loginname
    
    def getLogin (self):
        return self.loginname
    
    def setPassword (self,password):
        self.password = password
    
    def getPassword (self):
        return self.password
    
    def getDateCreated (self):
        return self.dateCreated
    
    def setDateCreated (self, dateCreated):
        self.dateCreated = dateCreated