# IZZATA CLARISSA SALSBILA
# H071221065

# Membuat program yang mengalikan dua matriks 2x2 

math1 = [int(input("nilai matriks pertama indeks 1,1:")),
int(input("nilai matriks pertama indeks 1,2:")),
int(input("nilai matriks pertama indeks 2,1:")),
int(input("nilai matriks pertama indeks 2,2:"))]

math2 = [int(input("nilai matriks kedua indeks 1,1:")),
int(input("nilai matriks kedua indeks 1,2:")),
int(input("nilai matriks kedua indeks 2,1:")),
int(input("nilai matriks kedua indeks 2,2:")),]

a = math1[0] * math2[0] + math1[1] * math2[2]
b = math1[1] * math2[1] + math1[1] * math2[3]
c = math1[2] * math2[0] + math1[3] * math2[2]
d = math1[2] * math2[1] + math1[3] * math2[3]

print("hasil perkalian matriks:")
print("|%d, %d| x |%d, %d| = |%d, %d|" %(math1[0], math1[1], math2[0], math2[1], a, b))
print("|%d, %d| x |%d, %d| = |%d, %d|" %(math1[2], math1[3], math2[2], math2[3], c, d))
