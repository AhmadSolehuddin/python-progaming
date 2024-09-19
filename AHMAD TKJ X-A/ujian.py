jumlah_pembeli = int(input("masukan jumlah pembeli: "))

for i in range(jumlah_pembeli):
    usia_pembeli = int(input("masukan usia pembeli: "))
    jumlah_tiket = int(input("masukan jumlah tiket yang ingin dibeli: "))

    harga_anak = 30000
    harga_dewasa = 50000
    harga_lansia = 35000

    if usia < 12:
        harga_tiket = harga_anak
    elif 12 <= usia <= 60:
        harga_tiket = harga_dewasa
    else:
        harga_tiket = harga_lansia

    total_harga += harga_tiket * jumlah_tiket
        print(f"\nTotal harga untuk semua  tiket yang dibeli: Rp{total_harga_semua_tiket}")