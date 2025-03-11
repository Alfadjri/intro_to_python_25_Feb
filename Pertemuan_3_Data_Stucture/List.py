# misal 
# punya data makanan
# inisialisasai teknik menyebutkan terlebih dahulu
# C = Create => add value
makanan = ["Rendang","Kurma","Ayam","Appel"]

# CRUD 
# C = Create => add value
# R = Read
# U = Update
# D = Delete

# R = Read 
print(f"list makanan yang ada saat ini : {makanan}")
print(f"Ambilkan saya nilai Ayam dari list makanan : {makanan[2]}")

# U = Update
makanan[2] = "Ayam Cabe hijau"
print(f"list makanan yang ada saat ini : {makanan}")

# C = Create => Add value atau bahasa lain append
makanan.append("Pisang")
print(f"list makanan yang ada saat ini : {makanan}")
# D = Delete
makanan.remove("Rendang")
makanan.remove("Ayam Cabe hijau")
print(f"list makanan yang ada saat ini : {makanan}")


keranjang_buah = ["melon","semangka"]
makanan_baru = makanan + keranjang_buah
print(f"list makanan yang ada saat ini : {makanan_baru}")