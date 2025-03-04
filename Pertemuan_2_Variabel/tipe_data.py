# Numeric
# int (Interger atau bilangan bulat)
x = 32767
print("ini contoh bilangan bulat integer : {0}".format(x))
# float atau double nilai desimal
# float di tambahi belakangnya f bisanya untuk format desimal
f = 9.8
print("ini contoh bilangan desimal float : {0}".format(f))
#complex
z = 2 + 3j
print(f"ini contoh bilangan complex  : {z}")
#squence type
a = [1,2,3,4,5] # tipe data list
a[0] = 2
print("contoh tipe data list : {0}".format(a))
b = (4,5,6)
print("contoh tipe data truplet : {0}".format(b))
# nomer urut
c = range(1,5)
print("contoh tipe data rage : {0}".format(c))

#tipe text
# kalau pakek ' (petik satu ini di sebut karakter atau char atau varchar)
nama_depan = "Alfadjri Dwi Fadhilah"
print("contoh tipe data text : {0}".format(nama_depan))

# mapping type
biodata = {
    "nama" : "Alfadjri Dwi Fadhilah",
    "age" : 24,
}


# \n ini di sebut new line (enter)
# \t ini di sebut tab (tab itu secara default memberikan 4 kali sepasi)
# \i ini untuk membuat tulisan mode italic
# \b ini untuk membuat tulisan mode bold

print("contoh biodata\nnama: {nama},\nusia : {age}".format(age =biodata['age'],nama = biodata["nama"]))

# set type
f = {1,2,3}
print("Contoh tipe data set :{0}".format(f))
g = frozenset({4,5,6,7})
print("Contoh tipe data frozenset :{0}".format(g))


# kondisi atau boolean  nilainya True (1) atau False (0)
kondisi = True
print("Contoh tipe data boolean :{0}".format(kondisi))

# binary type
i = 0b01000001
# cara panjang
# desimal = int(i)
# karakter = chr(desimal)
karakter = chr(int(i)) # cara singkat
print("Contoh tipe data binary type : {0}".format(karakter))
# tipe data arraytype
# array ini sama dengan list 
j = bytearray(a)
print("Contoh tipe data bytearray {0}".format(j))
# memoryview
k = memoryview(j)
print("Contoh tipe data memoryview {0}".format(k))