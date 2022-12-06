class Data :
    def __init__(self, nama, email, password):
        self.nama = nama
        self.email = email
        self.password = password
    def getname (self) :
        return self.nama
    def getemail (self) :
        return self.email
    def getpassword (self) :
        return self.password

class Person(Data) :
    def __init__(self, nama, email, password):
        super().__init__(nama, email, password)
    def setname (self, newname) :
        self.nama = newname
    def getname (self) :
        return self.nama