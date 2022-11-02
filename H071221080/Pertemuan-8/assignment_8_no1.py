# Program class diagram Person
# nama, umur dan apakah pria?

class Person:
    def __init__(self, nama, umur, pria):
        self.name = nama
        self.age = int(umur)
        self.isMale = bool(pria)
        
    def setAge(self, umur):
        self.age = int(umur)

    def getAge(self):
        print(self.age)

    def setName(self, nama):
        self.name = nama

    def getName(self):
        print(self.name)

    def setGender(self, gender):
        if gender == 'Male':
            self.isMale = True
        else:
            self.isMale = False

    def getGender(self):
        if self.isMale == True:
            self.gender = 'Male'
            print(self.gender)
        else:
            self.gender = 'Female'
            print(self.gender)

name = input('Name = ')
age = int(input('Age = '))
input_isMale = input('Is Male? (True or False) = ')
if input_isMale == 'True':
    isMale = bool(True)
else:
    isMale = bool(False)

person1 = Person(name, age, isMale)
print()
person1.getName()
person1.getAge()
person1.getGender()