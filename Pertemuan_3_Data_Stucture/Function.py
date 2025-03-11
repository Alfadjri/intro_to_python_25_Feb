def print_data(pesan , data):
    print(f"{pesan},{data}")

print_data("Helo nama saya " , "Alfadjri Dwi Fadhilah")

def persen__rugi(harga_beli , harga_jual):
    kerugian = harga_beli - harga_jual
    nilaiB = kerugian / harga_beli
    hasil = nilaiB * 100
    return hasil

rugi = persen__rugi(15000000,13500000)
print(f"Hasil {rugi}%")
rugi = persen__rugi(400000,360000)
print(f"Hasil {rugi}%")
rugi = persen__rugi(337500,325000)
print(f"Hasil {rugi}%")