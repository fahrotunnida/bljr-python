# def hitung(angka1, angka2) :
#     return angka1 * angka2

# print(hitung(2, 4 ))


# def hitung(angka1, angka2) :
#     return angka1 + angka2

# print(hitung(4, 5)) 

# def hitung(angka1, angka2) :
#     return angka1 - angka2

# print(hitung(10, 5))


def hitung (angka1, angka2, operasi) :
    
    if type(angka1) == str : 
        print ("data yang dimasukkan harus berupa angka")
        return

    if operasi == "*" :
        return angka1 * angka2
    elif operasi == "+" :
        return angka1 + angka2
    elif operasi == "-" :
        return angka1 - angka2

print(hitung("dua", 4, "*"))
print(hitung("empat",5, "+"))
print(hitung("sepuluh",5, "-"))


