import os
import platform
# kalau di C  dan html ini sebutanya header
# kalau di java ini panggilanya pakage

def clear_terminal():
    os_name = platform.system()
    if(os_name == "Windows"):
        os.system("cls")
    else:
        os.system("clear") 
def pause_terminal(pesan = "Tekan enter untuk kembali ke menu utama"):
    input(pesan)
# Case saya mau bikin kotak 3 x 3
def persegi():
    panjang = int ( input("Panjang dari Persegi : "))
    lebar = int (input("Lebar dari persegi : "))
    for i in range(panjang):
        for j in range(lebar):
            print("*",end="")
        print()
    print()
    pause_terminal()


def segitiga_siku_siku(kebalik = False):
    tinggi = int(input("Tinggi dari segitiga : "))
    panjang = int(input("panjang dari segitiga : "))
    if(panjang > tinggi):
        print("Panjang tidak boleh lebih besar dari tinggi")
        pause_terminal()
        clear_terminal()
        segitiga_siku_siku()
        
    for i in range(1,tinggi+1):
        for j in range(panjang):
            if(kebalik == True): # kebalik 
                if  j < panjang -  i :
                    print("*",end="")
                else:
                    print(" ",end="")
            else : 
                if  j < i :
                    print("*",end="")
                else:
                    print(" ",end="")
        print()
    print()
    pause_terminal()

def fibonaci(jumlah_data,segitiga = False):
    # formula dasar
    # 0 + 1 = 1 + 1 = 2 + 1 = 3 + 2 = 5 + 3 = 8 + 5 = ....... 
    # (0 + 0 = 0) index 1
    # (0 + 1 = 1) index 2
    # (1 + 1 = 1) index 3
    # (1 + 1 = 2) index 4
    # (2 + 1 = 3) index 5
    # (3 + 2 = 5) deret ke 6
    
    if jumlah_data <= 0 :
        print("Masukan angka lebih dari 0")
        pause_terminal()
        clear_terminal()
        jumlah_data = int(input("Masukan jumlah data"))
        fibonaci(jumlah_data)
        
    awal_fibonaci = [0,1]
    for i in range(2,jumlah_data):
        next_fibonaci = awal_fibonaci[-1] +  awal_fibonaci[-2]
        awal_fibonaci.append(next_fibonaci)
    if(segitiga == False):
        print("Deret Fibonci value : ", awal_fibonaci[:jumlah_data])
        pause_terminal()
    else:
        return awal_fibonaci

def fibonaci_segitiga(jumlah_data):
    bilangan_fibonaci = fibonaci(jumlah_data,True)
    index = 0
    row = 1 
    
    while index < len(bilangan_fibonaci):
        for _ in range(row):
            if index < len(bilangan_fibonaci):
                print(bilangan_fibonaci[index], end=" ")
                index +=1
        print()
        row +=1
    
    pause_terminal()
    
def main():
    while(True):
        clear_terminal()
        print("=====Selamat Datang Di program Test Looping======")
        print("1. Persegi")
        print("2. Segitiga siku-siku")
        print("3. Segitiga siku-siku kebalik")
        print("4. Fibonaci code")
        print("5. Fibonaci Segitiga siku-siku")
        print("q. Quit")
        select = input("Selection ===> ")
        clear_terminal()
        match(select):
            case "1" : 
                persegi()
            case "2":
                segitiga_siku_siku()
            case "3":
                segitiga_siku_siku(True)
            case "4":
                jumlah_data = int(input("Masukan jumlah data : "))
                fibonaci(jumlah_data)
            case "5":
                jumlah_data = int(input("Masukan jumlah data : "))
                fibonaci_segitiga(jumlah_data)
            case "q":
                print("Selamat tinggal program")
                pause_terminal("Tekan apapun untuk melanjutkan program")# di sini input bukan untuk mengambil nilai keyboard tapi untuk mendeteksi kalau kalau dia sudah tekan tombol apapun
                return 0
    


if __name__ == "__main__":
    main()