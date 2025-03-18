# case 

class Ibu:
    panggilan = "ini class punya ibu"
    
    def memanggil(self):
        print("Iya , Ada apa ?")
    
    def setSifat(self,sifat):
        self.__sifat = sifat
    
    def getSifat(self):
        return self.__sifat
    

class Anak(Ibu): # inheritance atau pewarisan sifat
    def suruh(self):
        print("Nanti aja dulu latak di sana !")


# real case
sekolah = Anak()
sekolah.panggilan = "budi"
print(f"Siapa panggilan anak ini : {sekolah.panggilan}")
print(f"Tolong panggilkan {sekolah.panggilan}")
sekolah.memanggil()
sekolah.setSifat("Anak baik !")
print(f"Sifat {sekolah.panggilan} : {sekolah.getSifat()}")
print(f"{sekolah.panggilan} Tolong ambilkan Air di meja ")
sekolah.suruh()

# class ibu
ibu = Ibu()
ibu.panggilan = "Tini"
print(f"Apakah ibu {ibu.panggilan} bisa di suruh ? ")
ibu.suruh()