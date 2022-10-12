# Membuat fungsi all_string_rotation

n = list(map(str,input("masukkan kata: ").strip()))
def rotasi(n):
    jumlah = len(n)
    while jumlah !=0:
        n.insert(0,n[-1])
        n.pop()
        jumlah -=1
        print(''.join(n),end=" | ")

rotasi(n)