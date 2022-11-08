class person:
    def __init__(self, nama, umur, laki_laki):
        self.nama = nama
        self.umur = umur
        self.isMale = laki_laki
    def getAge (self):
        print(f"umur: {self.umur} Tahun")
    def getName (self):
        print (f"nama: {self.nama}")
    def getGender (self):
        if self.isMale == 'true':
            self.isMale = True
            if self.isMale == True:
                print ("Gender: laki laki") 
        elif self.isMale == 'false':
            self.isMale = False
            if self.isMale == False:
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