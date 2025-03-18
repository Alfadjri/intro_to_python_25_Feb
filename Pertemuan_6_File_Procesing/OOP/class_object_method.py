# kasus
# kita pakai Hewan

class Hewan: # hewan ini disebut dengan nama dari kelas
    nama = "default" # nama_hewan di sebut obejct 
    jenis = "default" # 
    # usia hewan sifatnya private
    _umur_hewan = 10 # _ ini sebutanya property private umur_hewan ini masuknya ke nama object
    
    def __init__(self, nama_hewan , jenis_hewan):
        self.nama = nama_hewan
        self.jenis = jenis_hewan
    
    def makan(self): # makan di sebut method (void)
        print("Hewan sedang makan")
    

#cara memanggil 
kucing = Hewan("Tom","kucing kampung")
#cara implementasi
print(f"Nama Kucing : {kucing.nama}") # pemanggilan object nama pada kelas kucing
print(f"Jenis Kucing : {kucing.jenis}")
# cara memanggil method
print("Kucing saat ini sedang apa ?")
kucing.makan() #ini cara memanggil method atau function