import time

a = int(input("masukan jumlah siswa: "))

for i in range(a):
    namna = (input("masukan nama siswa / siswi: "))
    t1 = float(input("masukan nilai tugas ke 1 anda: "))
    t2 = float(input("masukan nilai tugas ke 2 anda: "))
    t3 = float(input("masukan nilai tugas ke 3 anda: "))

    b = 3

    all = t1 + t2 + t3

    avv = all // b

    if avv >=70:
        print("kamu lulus")
    elif avv >= 50 and avv <= 69:
        print("harus ada perbaikan")
    elif avv >= 50:
        print("anda tidak lulus")
    else:
        print("anda tidak naik kelas")