
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
        return "Nanti aja dulu latak di sana !"

class Anak2(Ibu):
    def suruh(self):
        return "Iya saya akan segera ambilkan"
    

def Suruh(Ibu): #polymorhism teknik memanggil function atau nilai tampa perlu tau metode apa yang ada di dalamnya 
    return Ibu.suruh()
    

budi = Anak()
tono = Anak2()

print("tono tolong ambilkan makan di atas meja")
print(Suruh(tono))