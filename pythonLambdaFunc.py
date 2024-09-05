#Lambda ifadeleri(fonksiyonları)

kare_al = lambda x : x * x

kup_al = lambda x : x ** 3

toplam = lambda x,y : x + y

genel_toplam = lambda *args : sum(args)

liste = [("Ali",20),("Veli",19),("Emel",30),("Hakan",24),("Cenk",27)]
liste.sort(key= lambda x : x[1])

liste2 = [{"Ad":"Ahmet","Soyad":"Caliskan","Yas":25},{"Ad":"Mehmet","Soyad":"Uzun","Yas":22},{"Ad":"Duru","Soyad":"Yildiz","Yas":24}]
liste2.sort(key= lambda x : x["Yas"])
print(liste2)
