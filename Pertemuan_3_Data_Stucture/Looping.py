#while
#di mana kalau tau kapan ini akan di mulai 
#format
# while(kondisi):
#   apa yang akan di ulang

count = 2000
while( count <= 2000):
    print(f"{count}.Saya tidak akan mengulangi kesalahan ini")
    count +=1
    
# for
# kalau kita tau kapan harus berhenti dan nilai fix gak terganti atau tahu rentangnya  
for value in range(0,1):
    print(f"{value}.Saya tidak akan mengulangi kesalahan ini")
    
buah = ['Kurma']
#foreach
# jika kamu tidak tau berapa banyak data tapi kamu tau tipe datanya
for value in buah : 
    print(f"Buah yang ada saat ini : {value}")
    
# break sama continue
bilangan = 1
while(bilangan <= 100):
    if(bilangan % 2 == 0):
        bilangan +=1
        continue # code untuk skip 1 putaran
    print(bilangan)
    bilangan += 1
    if(bilangan >= 40):
        break # code untuk memaksa while itu berhenti