from abc import ABC, abstractclassmethod

class Ibu:
    panggilan = "ini class punya ibu"
    
    def memanggil(self):
        print("Iya , Ada apa ?")
    
    def setSifat(self,sifat):
        self.__sifat = sifat
    
    def getSifat(self):
        return self.__sifat
    
    @abstractclassmethod
    def suruh(self):
        pass

class Anak(Ibu): 
    # ini teknik namanya overiding
    def suruh(self):
        print("Nanti aja dulu latak di sana !")

class Anak2(Ibu):
    def suruh(self):
        print("Iya saya akan segera ambilkan")


budi = Anak()
budi.panggilan = "budi"
tono = Anak2()
tono.panggilan = "tono"
tini = Ibu()
tini.panggilan = "tini"

# case ibu panggil anak2
print(f"{tini.panggilan} {tono.panggilan} Tolong ambilkan air di dapur")
tono.suruh()
print(f"{budi.panggilan} ibu {tini.panggilan} Tolong ambilkan makan !!!")
tini.suruh()