#case 

class Mobil:
    nama = "default"
    _semau_saya_aja_kasih_variabel = "default" #sifatnya private
    
    def __init__(self,nama_mobil):
        self.nama = nama_mobil
        
    def getInfo(self):
        print(f"Nama mobil : {self.nama}")
        self.getMerek()
        
    # cara membuat dia public tapi sembarangan di ganti
    # set untuk menetapkan nilai
    def setMerek(self,merek_mobil):
        self._semau_saya_aja_kasih_variabel = merek_mobil
    # get ubtuk mengambil nilai
    def getMerek(self):
        print(f"Merek Mobil : {self._semau_saya_aja_kasih_variabel}")
        

toyota = Mobil("Supra")
toyota.setMerek("Toyota")
toyota.getInfo()
