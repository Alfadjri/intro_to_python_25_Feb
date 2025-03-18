from Employee import Employee

class Manager(Employee):
    def __init__(self, nama, umur, pekerjaan, gaji,jumlah_anggota):
        super().__init__(nama, umur, pekerjaan, gaji)
        self._jumlah_anggota = jumlah_anggota
        
    def get_detail(self):
        detail = super().get_detail()
        detail +=f"Jumlah tim : {self._jumlah_anggota}"
        return detail
    
    def get_work(self):
        return f"{self._name} dia bekerja sebagai manager dengan jumlah anggota  : {self._jumlah_anggota}"