#Map Fonskiyonu Kullanımı

liste1 = [1,3,4,7,8]
liste2 = [3,5,9,0,1]
liste3 = [2,5,10]

def toplam(x,y,z):
    return x + y + z
sonuc = list(map(toplam,liste1,liste2,liste3))
print(sonuc)    

sonuc2 = list(map(lambda x,y,z : x + y + z,liste1,liste2,liste3))
print(sonuc2)



urunler = [["Ayakkabı",150],["Pantolon",120],["Gömlek",100],["Ceket",200]]

def indirim(x):
    urun,fiyat = x[0],x[1]
    fiyat = fiyat * 0.9
    return [urun,fiyat]

sonuc3 = list(map(indirim,urunler))
print(sonuc3)



isimler = ["ahMeT","aYşE","oNur","HÜSeyiN"]

isimler2 = list(map(lambda x : x.lower(),isimler))
print(isimler2)

isimler2 = list(map(lambda x : x.capitalize(),isimler))
print(isimler2)
