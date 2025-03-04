x = 3
y = 2
# penjumlahan
hasil = x + y 
print(f"Hasil dari {x} + {y} = {hasil}")
# pengurangan
hasil = x - y 
print(f"Hasil dari {x} - {y} = {hasil}")
# perkalian
hasil = x * y 
print(f"Hasil dari {x} * {y} = {hasil}")
# pembagian
hasil = x / y 
print(f"Hasil dari {x} / {y} = {hasil}")
# pembagian konversi
hasil = int(x / y)
print(f"Hasil dari {x} / {y} = {hasil}")
# Modulus (sisa pembagian)
hasil = x % y
print(f"Hasil dari {x} % {y} = {hasil}")
# Perpangkatan
hasil = x ** y
print(f"Hasil dari {x} ^ {y} = {hasil}")

#increment(penjumlahan) dan decerment (pengurangan)
z = 1000
print("Hasil sebelum di tambahkan : {0}".format(z))
#z = z + 1 #(Cara jadul)
z += 100
print("Hasil setelah di tambahkan : {0}".format(z))
z -= 100
print("Hasil setelah di dikurang : {0}".format(z))