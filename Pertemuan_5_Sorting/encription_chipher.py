def cesar_chiper(pesan , kata_sandi):
    hasil = ""
    for char in pesan:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            hasil += chr((ord(char)- shift_base + kata_sandi) % 255 + shift_base)
        else:
            hasil += char
    return hasil

def main():
    pesan = input("Masukan pesan yang akan di rahasiakan :\n")
    kata_sandi = int(input("Pergeseran huruf yang di inginkan (Kata sandi) : "))
    #chipertext = pesan yang sudah di encrip
    pesan_enkrip = cesar_chiper(pesan,kata_sandi)
    print("Teks setelah di encript :")
    print(pesan_enkrip)
    
if __name__ == "__main__":
    main()