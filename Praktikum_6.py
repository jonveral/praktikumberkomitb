# JUDUL PROGRAM
# Program Id Pengguna berdasarkan nomor urut seseorang

# KAMUS
# x : integer
# y : integer
# nomor_urut : integer

# ALGORITMA
nomor_urut = int(input("Masukkan Nomor Urut: "))
x = int(input("Masukkan batas bawah (x): "))
y = int(input("Masukkan batas atas (y): "))

f1 = [0] * nomor_urut  
f2 = 0  
n = nomor_urut

for i in range(2, n + 1):
    while n % i == 0:
        sudah_ada = False
        j = 0
        while j < f2:
            if f1[j] == i:
                sudah_ada = True
            j += 1
        if not sudah_ada:
            f1[f2] = i
            f2 += 1
        n //= i

id1 = [0] * (y - x + 1)
id2 = 0  

for i in range(x, y + 1):
    valid = False
    j = 0
    while j < f2 and not valid:
        if i % f1[j] == 0:
            valid = True
        j += 1
    if valid:
        id1[id2] = i
        id2 += 1

if id2 > 0:
    print("Id Pengguna yang valid =", end=" [")
    for k in range(id2):
        if k > 0:
            print(", ", end="")
        print(id1[k], end="")
    print("]")
else:
    print("Tidak ada Id Pengguna yang valid")
