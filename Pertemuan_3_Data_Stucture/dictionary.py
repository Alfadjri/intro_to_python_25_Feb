siswa = {
    "kelas" : 12,
    "jurusan" : ["ipa","ips"],
    "nama_ketua" : "udin"
}

# read
print("Data metah : {0}".format(siswa))
# read spesifk
print(f"Jurusan apa ini ? {siswa['jurusan'][0]}")
# C => Append
siswa["nilai_kelas"] = 90
print("Data metah : {0}".format(siswa))
# update 
siswa["nilai_kelas"] = 60
print("Data metah : {0}".format(siswa))
# delete
del siswa["nilai_kelas"]
print("Data metah : {0}".format(siswa))