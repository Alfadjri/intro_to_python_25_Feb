import random

def random_number(banyak_data):
    
    list_data = [] #tipe list
    for i in range(banyak_data):
        nilai_acak = random.randint(1,100)
        list_data.append(nilai_acak)
    
    return list_data

def bubble_sort(data):
    n = len(data) #len bahasa lain dari length ini gunanya untuk menghitung banyak data yang ada list / array
    
    # logic
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                # temp = data[j]
                # data[j] = data[j+1]
                # data[j+1] = temp
                data[j],data[j+1] = data[j+1],data[j]
def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_value = i
        for j in range(i+1,n):
            if data[j] < data[min_value]:
                min_value = j

        data[i],data[min_value] = data[min_value],data[i]

def main():
    banyak_data = int(input("Banyak data yang akan di shorting : "))
    data = random_number(banyak_data)
    print("List data sebelum di urutkan :")
    print(data)
    # logic shorting
    # bubble_sort(data)  # kemungkinan hanya mentok di 15000 data 
    selection_sort(data) # kemungkinan hanya mentok di 15000 data 
    # end logic
    print("List data setelah di urutkan : ")
    print(data)
    
if __name__ == "__main__":
    main()