#-*-coding:utf-8-*-

# görev: asdasdjhkdasdsad kelimesindeki tüm harfleri teke indir ve set olarak yazdır

new_string = "asdasdjhkdasdsad"
new_set = { harf for harf in new_string }
print(new_set)

# -----------------------------------
"""
#görev: ismini ekleyip liste yapısına çevir:

new_set = {"sychron","sh@d0w","n1bbabyte","enoec_gt"}
new_set.add("scarlet")
new_list = list(new_set)

print(new_list)
"""
#-----------------------------------------------------------
"""
#görev: aynı değerleri teke indirelim,
#       set veya tuple               :

tuple1 = (5, "izmir", 28, "ankara", 5, "izmir")
#new_set = set(tuple1) #bir demet(tuple)i set'e çevirmek
#tuple2 = tuple(new_set) #bir seti tuple'a çevirmek
tuple2 = tuple(set(tuple1)) #Tek satırlık kod
print(tuple2)

#-----------------------------------------------------------
"""
"""
#görev: izmir ve balıkesir'in tuple elemanı olup olmadığını if olmadan kontrol et

cities = ("istanbul","ankara","izmir")
print("izmir" in cities)
print("balıkesir" in cities)

#-----------------------------------------------------------
"""
"""
#görev: 4 değerini 50'ye, 1 değerini 100'e çevir:
our_tuple = (4,8,[1,20])
print(type(our_tuple))
#our_tuple[0] = 50 #işe yaramaz çünkü demet elemanı değiştirilemez.
our_tuple[-1][0] = 100 #işe yaradı çünkü demetin içinde olsa da '1' bir liste elemanı
print(our_tuple)
"""
"""
yanlis_tuple = ("tekeleman") #eğer demette tek elemansa sonuna "," yoksa str algılar.
print(type(yanlis_tuple))
dogru_tuple = ("tekeleman",) #dogru_tuple örneğindeki gibi yaparsak tuple olur.
print(type(dogru_tuple))
"""
"""
#görev: print mahmut, print 6:

new_tuple = ("izmir",[28,"mahmut"],(2,4,6),100)
print(new_tuple[1][1])  # print mahmut
print(new_tuple[2][-1]) # print 6

#-----------------------------------------------------------
"""
"""
#görev: print type,izmir,ağrı,ilk iki şehri ve son iki şehri

cities = ("izmir","ankara","istanbul","ağrı")
print(type(cities))
print(cities[:2]) #ilk iki şehir
print(cities[-2:]) #son iki şehir

#-----------------------------------------------------------
"""