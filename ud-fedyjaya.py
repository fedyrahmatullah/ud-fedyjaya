import os
clear = lambda: os.system('cls')

def main():
    clear()
    print("UD.FEDY JAYA")
    Print("Toko Sparepart Sepeda Motor")
    print("---------------------------")
    print()
    print("Apa yang bisa saya bantu?")
    print()
    print("1 - Tambahkan Barang")
    print("2 - Melihat Daftar Barang")
    print()
    while True:
        opsiUser == input("Tentukan Pilihan Anda: ")
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
                    
                
                        
                
        
    