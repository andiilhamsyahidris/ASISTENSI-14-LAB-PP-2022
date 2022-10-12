#buat function yg menerima sebuah bilangan bulat 
#kemuadian mengembalikan nilai faktorial bilangan tersebut
print("Andi Muthia Mulia Putri")
print('=======================')

bilangan=int(input("bilangan bulat:"))

def faktorial(bilangan):
    if bilangan >1:
        return bilangan*faktorial(bilangan-1)

    return 1
print(f"{bilangan}!={faktorial(bilangan)}")