# IZZATA CLARISSA SALSABILA
# H071221065
# Program sederhana dari class diagram 

class Person :
    def __init__ (self, name, umur, gender) :
        self.name = name
        self.age = umur
        self.gender = gender
        
    def getName(self) :
        print(f"Nama : {self.name}")
    
    def getAge(self) :
        print(f"Usia : {self.age}")

    def getGender(self) :
        if self.gender == True :
            print("Gender : Laki-laki")
        else : 
            self.gender == False
            print("Gender : Perempuan")

nama = input('Nama: ')
umur = input ('Umur: ')
gender = input ('gender: ')

biodata = Person(nama , umur , gender)
biodata.getName()
biodata.getAge()
biodata.getGender()