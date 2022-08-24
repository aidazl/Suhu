print("Indeks Satuan Suhu")
print ("====================")


print ("pilihan suhu")
print("1 : celcius")
print("2 : kelvin")

suhu = int(input("masukkan pilihan suhu (1 / 2) : "))

if suhu == 1 :
    x = int (input("masukkan derajat suhu : "))
    y = 273
    z = x + y
    print ("suhunya adalah :", x, "+", y, "=", z, "derajat kelvin")


elif suhu == 2 :
    x = int (input("masukkan derajat suhu : "))
    y = 273
    z = x - y
    print("suhunya adalah :", x, "-", y, "=", z, "celcius")


print("====================")