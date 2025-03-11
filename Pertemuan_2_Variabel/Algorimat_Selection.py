nilai_raport = 80
#if
#format 
#if(kondisi):
# apa yang akan kamu lakukan jika kondisi tersebut terpenuhi
print("===========if=========") #header file atau penanda
if(nilai_raport >= 80):
    print("Selamat kamu lulus dalam ujian kali ini!")
    
#if else
#format
#if(kondisi) : 
# apa yang kamu lakukan jika kondisi tersebut terpenuhi
#else:
# apa yang kamu lakukan jika kondisi tidak terpenuhi

print("===========if-else=========") #header file atau penanda
nilai_raport = 90
if(nilai_raport > 80):
    print("Selamat kamu lulus dalam ujian kali ini!")
else:
    print("Kamu tidak lulus silahkan ulang kembali tahun depan !")
    
print("========tenery if else===========")
nilai_raport = 30
hasil = "A" if nilai_raport >= 60 else "C"
print(f"nilai kamu : {hasil}")


# if else-if else
# format
# if(kondisi) :
# apa yang kamu lakukan jika kondisi terpenuhi
# elif (kondisi 2):
# apa yang kamu lakukan jika kondisi pertama tidak terpenuhi
# else :
# apa yang kamu lakukan jika tidak ada yang terpenuhi

# teknik
# whitelist : teknik catat semua syarat yang di butuhkan
# blacklist : teknik catat apa yang salah saja
print("===========if-else=========")
print("===========whitelist=========")
print("===========if-elif (bersarang)")
# whitelist
nilai_raport = 60
if(nilai_raport >= 90):
    print("Selamat kamu memiliki nilai di atas KKM")
elif(nilai_raport >= 70 and nilai_raport <= 80):
    # ini sebutnya teknik if-elif-else bersarang
    if(nilai_raport >= 75):
        print("nilai unik hampir saja kamu tidak lulus")
    else:
        print("Selamat kamu lulus dengan nilai pas-pas san")
else :
    print("Mohon maaf kamu tidak lulus dalam ujian kali ini")

print("===========blacklist=========")
print("===========if-elif (bersarang)")
# whitelist
nilai_raport = 60
if (nilai_raport <= 70):
    print("Mohon maaf kamu tidak lulus dalam ujian kali ini")
if (nilai_raport >= 75):
    print("nilai unik hampir saja kamu tidak lulus")
if (nilai_raport >= 90):
    print("Selamat kamu memiliki nilai di atas KKM")
    
# switch case
print("========Switch case===========")
print("1.Start")
print("2.Exit")
select = input("Selection => ")
match select:
    case "1" : 
        print("Game start")
    case "2" :
        print("Game Over")
    case _ : #default mode atau else
        print("Input not valid")
        
