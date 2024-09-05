#reduce fonksiyonu
from functools import reduce
from math import gcd    #ebob'u kullanmak için import edildi.


liste = [2,4,6,9,10]  #ebob(a,b) * ekok(a,b) = a*b  ==>   ekok(a,b) = (a*b) / ebob(a,b)  

def ekok(x,y):
    return int((x*y) / gcd(x,y))

ekok1 = reduce(ekok,liste)
print(ekok1) 

# Second Examples , TAŞ-KAĞIT-MAKAS UYGULAMASI REDUCE FONKSİYONU KULLANILARAK

def tas_kagit_makas(x,y):
    ikili = {x,y}
    if x == y:
        return y
    if ikili == {"tas","makas"}:
        return "tas"
    if ikili == {"tas","kagit"}:
        return "kagit"
    if ikili == {"kagit","makas"}:
        return "makas"

liste1 = ["tas","kagit","tas","makas","kagit","tas","kagit"]
sonuc = reduce(tas_kagit_makas,liste1)

print(sonuc)    