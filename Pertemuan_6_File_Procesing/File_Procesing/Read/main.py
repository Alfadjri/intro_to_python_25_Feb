open_file = open("../Write/Contoh_write_text.txt","r")
# Read
read_ = open_file.read()
print("Value file Contoh_write_text.txt : ")
print(read_)

open_file.seek(0) 
print(open_file.readline(3))

open_file.seek(0) 
line_numer = 1
for line in open_file.readlines():
    if(line_numer == 2):
        print(line.strip())
    line_numer += 1
    
open_file.close()