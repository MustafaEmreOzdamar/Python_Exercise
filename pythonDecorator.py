import time

def decorate(fonk):
    def wrapper():
        print("fonksiyon çalışmadan önceki işlemler")
        fonk()
        print("fonksiyon çalıştıktan sonraki işlemler")
    return wrapper
@decorate
def fonksiyon():
    print("fonksiyon çalışıyor")
fonksiyon()



def zaman_hesapla(fonk):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        fonk(*args,**kwargs)
        bitis = time.time()
        print(f"işlem {bitis - baslangic} saniye sürdü")
    return wrapper    

@zaman_hesapla
def kare_al(liste):
    for x in liste:
        print (x * x)

@zaman_hesapla         
def kup_al(liste):
    for x in liste:
        print (x * 3)

@zaman_hesapla
def topla(a,b):
    time.sleep(1)
    print(a + b)
  
#topla(15,35)
kup_al(range(88))
            


def zaman_hesapla(fonk):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonk(*args,**kwargs)
        bitis = time.time()
        print(f"işlem {bitis - baslangic} saniye sürdü")
        return sonuc
    return wrapper    

@zaman_hesapla
def kare_al(liste):
    sonuc = []
    for x in liste:
        sonuc.append(x * x)
    return sonuc

@zaman_hesapla         
def kup_al(liste):
    sonuc = []
    for x in liste:
        sonuc.append(x ** 3)
    return sonuc    

@zaman_hesapla
def topla(*args):
    time.sleep(1)
    return sum(args)
    
print(kup_al(range(100000))) 



# @property , @setter , @deleter

class Kisi:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
        #self.adsoyad = ad + " " + soyad 
        
    @property           #methodların aynı initteki özellikler gibi çağrılmasını sağlar. () işareti olmadan
    def ad_soyad(self):
        return f"{self.ad} {self.soyad}"
    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"
    
    @ad_soyad.setter #methoddaki veya initteki özelliklerin değerlerini değiştirmek için kullanılır.
    def ad_soyad(self,isim):
        ad,soyad = isim.split(" ")
        self.ad = ad
        self.soyad = soyad
    
    @ad_soyad.deleter   #methoddaki veya initteki özellikleri silmek için kullanılır.
    def ad_soyad(self):
        print("silindi")
        self.ad = None
        self.soyad = None
    
kisi1 = Kisi("Emre","Ozdamar")

del kisi1.ad_soyad

print(kisi1.ad)
print(kisi1.ad_soyad)
print(kisi1.email)    
               
        