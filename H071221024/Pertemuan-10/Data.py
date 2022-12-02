from abc import ABC,abstractmethod
class Data(ABC) :
    def __init__(self,name,email,password) :
        self._name=name
        self._email=email
        self._password=password
    @abstractmethod
    def SetName(self,NewName) :
        pass
    @abstractmethod
    def GetName(self) :
        pass
    @abstractmethod
    def GetEmail(self) :
        pass
    def GetPassword(self) :
        pass

class Person(Data) :
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    def SetName(self,NewName):
        self._name=NewName
    def GetName(self) :
        return self._name
    def GetEmail(self):
        return self._email
    def GetPassword(self) :
        return self._password