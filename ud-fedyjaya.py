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
            
        
    