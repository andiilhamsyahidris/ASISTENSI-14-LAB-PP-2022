class person:
    def __init__(self, nama, umur, laki_laki):
        self.nama = nama
        self.umur = umur
        self.laki_laki = laki_laki
    
    def getAge (self):
        print(f"umur: {self.umur} Tahun")
    
    def getName (self):
        print (f"nama: {self.nama}")
    
    def getGender (self):
        if self.laki_laki == 'true':
            self.laki_laki = True
            if self.laki_laki == True:
                print ("Gender: laki laki") 
        elif self.laki_laki == 'false':
            self.laki_laki = False
            if self.laki_laki == False:
                print ("Gender: perempuan") 
        else: 
            print("inputan salah")

name = input('masukkan nama: ')
age = int(input("masukkan umur: "))
isMale = input ()

human = person(name, age, isMale)

human.getName()
human.getAge()
human.getGender()