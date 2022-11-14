class person :
    def __init__(self, nama, umur, laki_laki) :
        self.nama = nama 
        self.umur = umur
        self.laki_laki = laki_laki
    def setAge (self, umur) :
        self.umur = umur
    def getAge (self) :
        print(f"Umur   : {self.umur} Tahun")
    def setName (self, nama) :
        self.nama = nama
    def getName (self) :
        print(f"Nama   : {self.nama}")
    def setGender (self, laki_laki) :
        self.laki_laki = laki_laki
    def getGender (self) :
        if self.laki_laki == 'True' or self.laki_laki == 'true':
            self.laki_laki = True
            if self.laki_laki == True :
                print("Gender : Laki-laki")
        elif self.laki_laki == 'False' or self.laki_laki == 'false':
            self.laki_laki = False
            if self.laki_laki == False :
                print("Gender : Perempuan")
        else :
            print("inputan tidak falid")
    



name = input()
age = int(input())
isMale = input()
human = person(name, age, isMale)

human.getName()
human.getAge()
human.getGender()
