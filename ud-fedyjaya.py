import os
from sys import path
clear = lambda: os.system('cls')

def main():
    clear()
    print("UD.FEDY JAYA")
    print("Toko Sparepart Sepeda Motor")
    print("---------------------------")
    print()
    print("Apa yang bisa saya bantu?")
    print()
    print("1 - Tambahkan Barang")
    print("2 - Melihat Daftar Barang")
    print()
    while True:
        opsiUser = input("Tentukan Pilihan Anda: ")
        if opsiUser == '1':
            tambahBarang()
            break
        elif opsiUser == '2':
            lihatBarang()
            break

def tambahBarang():
    clear()
    print("UD.FEDY JAYA")
    print("Menambahkan Barang")
    print("------------------")
    print()
    print("Apa yang bisa saya bantu?")
    print()
    print("1 - Tambahkan lebih dari satu barang")
    print("2 - Tambahkan satu Barang")
    print()
    while True:
        opsiUser = input("Tentukan Pilihan Anda: ")
        if opsiUser in ['1', '2']:
            break
    if opsiUser == '1':
        print()
        while True:
            noBarang = input("Masukkan jumlah barang yang Ingin ditambahkan: ")
            if noBarang.isdigit(): #mendeteksi string angka saja
                break
        noBarang = int(noBarang)
        barangUser = {}
        for i in range(1, noBarang+1):
            while True:
                print()
                barangToko = input("Nama Barang: ")
                if barangToko != '':
                    break
            while True:
                jml_Barang = input("Jumlah Barang: ")
                if jml_Barang.isdigit():
                    break
            barangUser.update({barangToko: int(jml_Barang)})

        tambahBarangKeFile(barangUser, clear=False)
        keMenu("Barang telah ditambahkan")

    elif opsiUser == '2':
        print()
        while True:
            barangToko = input("Nama Barang: ")
            if barangToko != '':
                break
        while True:
            jml_Barang = input("Jumlah Barang: ")
            if jml_Barang.isdigit():
                break
        tambahBarangKeFile({barangToko: int(jml_Barang)}, clear=False)
        keMenu("Barang telah ditambahkan")

def lihatBarang():
    clear()
    print("UD.FEDY JAYA")
    print("Lihat Daftar Barang Toko")
    print("------------------------")
    print()
    barangToko = getbarangToko()
    print("BARANG")
    print("------")
    print()
    for barang in barangToko:
        print(f"{barang}: {barangToko[barang]}")

    print()
    print("UD.FEDY JAYA")
    print("Opsi yang tersedia: ")
    print()
    print("1- Edit Barang")
    print("2 - Hapus Barang")
    print()
    while True:
        opsiUser = input("Tentukan Pilihan Anda: ")
        if opsiUser == '1':
            editBarangToko()
            break
        elif opsiUser == '2':
            hapusBarangToko()
            break

def editBarangToko():
    clear()
    print("UD.FEDY JAYA")
    print("Edit Barang Toko")
    print("----------------")
    print("Tekan (K) untuk Kembali")
    print()
    print("Opsi yang tersedia: ")
    print()
    print("1 - Edit Nama Barang")
    print("2 - Edit Jumlah Barang")
    print()
    while True:
        opsiUser = input("Tentukan Pilihan Anda: ").lower()
        if opsiUser in ['1', '2', 'k']:
            break
    if opsiUser == 'k':
        main()

    barangToko = getbarangToko()
    if opsiUser == '1':
        print()
        while True:
            barangDiedit = input("Masukkan Nama Barang yang akan diedit: ")
            if barangDiedit in barangToko:
                break
            else:
                print("Barang Tidak Ada")
                print()

        while True:
            newNamaBarang = input("Masukkan Nama Baru untuk Barang: ")
            if newNamaBarang != '':
                break
        barangToko.update({newNamaBarang: barangToko[barangDiedit]})
        del barangToko[barangDiedit]

        tambahBarangKeFile(barangToko, clear=True)
        keMenu("Nama barang telah diubah")

    elif opsiUser == '2':
        print()
        while True:
            barangDiedit = input("Masukkan Nama Barang yang akan diedit: ")
            if barangDiedit in barangToko:
                break
            else:
                print("Barang Tidak Ada")
                print()

        while True:
            newJumlahBarang = input("Masukkan Jumlah Baru untuk Barang: ")
            if newJumlahBarang != '':
                break
        barangToko.update({barangDiedit: newJumlahBarang})
        tambahBarangKeFile(barangToko, clear=True)
        keMenu("Jumlah barang telah diubah")

def hapusBarangToko():
    print("UD.FEDY JAYA")
    print("Hapus Barang Toko")
    print("-----------------")
    print()
    barangToko = getbarangToko()
    while True:
        barangDihapus = input("Masukkan Nama Barang yang akan dihapus: ")
        if barangDihapus in barangToko:
            break
        else:
            print("Barang Tidak Ada")
            print()

    while True:
       konfirmasi = input("KONFIRMASI: Apakah Anda Yakin Ingin Menghapus Barang ini?(y/n): ").lower()
       if konfirmasi in ['y', 'n']:
           break
    if konfirmasi == 'y':
        del barangToko[barangDihapus]
        tambahBarangKeFile(barangToko, clear=True)
        keMenu("Barang telah dihapus")
    else:
        main()

def tambahBarangKeFile(barangUser: dict, clear: bool): #mendefinisikan tambah barang ke file
    if clear:
        f = open('dbarang-udfedyjaya.txt', 'w')
        f.close()
        with open('dbarang-udfedyjaya.txt', 'a') as file:
            for barang in barangUser:
                file.write(f"{barang}: {barangUser[barang]}")
                file.write('\n')
        return
    barangToko = getbarangToko()
    for barang in barangUser:
        if barang in barangToko: #mengecek barang apakah sudah ditambahkan
            barangToko[barang] += barangUser[barang]
    with open('dbarang-udfedyjaya.txt', 'a') as file:
        for barang in barangToko:
            file.write(f"{barang}: {barangToko[barang]}")
            file.write('\n')

def getbarangToko():
    barangToko = {}
    with open('dbarang-udfedyjaya.txt', 'r') as file:
        for line in file:
            line = line.replace('\n','').split(':')
            namaBarang, jumlahBarang = line[0], line[1].strip()
            barangToko.update({namaBarang: int(jumlahBarang)})

    return barangToko

def keMenu(pesan):
    while True:
        print()
        kembali = input(f"{pesan}. Tekan (M) untuk kembali ke Menu: ").lower() if pesan != None else input("Tekan (M) untuk kembali ke Menu: ").lower()
        if kembali == 'm':
            main()
            break


main()
