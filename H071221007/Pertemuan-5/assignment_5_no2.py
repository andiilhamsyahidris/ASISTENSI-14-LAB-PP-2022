#Program mengubah detail data diri

print ("Selamat datang untuk memulai silahkan input data anda")
dict_data = {
    "nama"   : input ("Input nama   :"),
    "umur"   : input ("Input umur   :"),
    "alamat" : input ("Input alamat :")}

print ("=" * 60)

def satu () :
    print ("Data anda adalah")
    print ("Nama   :", dict_data["nama"])
    print ("Umur   :", dict_data["umur"])
    print ("Alamat :", dict_data["alamat"])
    print ("=" * 60)

def dua () :
    a = input("Silahkan Input nama baru :")
    dict_data ["nama"] = a 
    print ("Data anda sukses diperbarui")
    print ("=" * 60)

def tiga () :
    b = input("Silahkan Input umur baru :")
    dict_data ["umur"] = b
    print ("Data anda sukses diperbarui")
    print ("=" * 60)

def empat () :
    c = input("Silahkan Input alamat baru :")
    dict_data ["alamat"] = c
    print ("Data anda sukses diperbarui")
    print ("=" * 60)

def lima () :
    return

def menu () :
    print ("Selamat datang %s silahkan pilih opsi" %(dict_data["nama"]))
    print ("=" * 60)
    print ("1. Detail anda")
    print ("2. Ubah Nama")
    print ("3. Ubah Umur")
    print ("4. Ubah Alamat")
    print ("5. Keluar")
    print ("=" * 60)
    opsi = input ("Input opsi :")
    print ("=" * 60)
    if opsi == "1" :
        satu () 
        menu ()
    elif opsi == "2" :
        dua ()
        menu ()
    elif opsi == "3" :
        tiga ()
        menu ()
    elif opsi == "4" :
        empat ()
        menu ()
    elif opsi == "5" :  
        print ("Selamat Tinggal %s" %(dict_data["nama"]))
        return
    else :
        menu ()        

menu ()
