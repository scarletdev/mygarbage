#-*-coding:utf-8-*-

#liste şeklinde dictionary:

arkadaslarim = [

{"name":"alper","age":35,"gender":"male"}, #listenin 0. elemanı
{"name":"mehmet","age":22,"gender":"male",}, #listenin 1. elemanı
{"name":"elif","age":67,"gender":"female"} #listenin 2. elemanı
]
print(arkadaslarim[1]["age"])
print(arkadaslarim)
"""
#---------------------------------------------------------------------------------
#her dict elemanı ikili eleman olarak yazılır.
#             key   value
monster_1 = {"name":"guru","power":10,"color":"red"}
print(monster_1)
print(monster_1["name"])
monster_1["name"] = "satan"
print(monster_1)

monster_1["hp"] = 50 #sözlüğe değer ekleme
print(monster_1.get("name"))

#var olan sözlük elemanını güncelle:
monster_1.update({"name":"Lucifer","color":"magenta"})
print(monster_1)

#del monster_1["power"]
print(monster_1)

popm = monster_1.pop("color")

# monster_1.clear() dictionary'nin içi boşsa sadece {} yazdıracaktır
# print(monster_1)

print(len(monster_1))

print(monster_1.keys())
print(monster_1.values())
print(monster_1.items())

for x in monster_1.keys(): #default olarak key değerlerini dönüyor ancak kesin sonuç için dict.keys()
    print(x)

for xx in monster_1.values(): #default olarak key değerlerini dönüyor ancak kesin sonuç için dict.keys()
    print(xx)

#print(popm) #pop ile silinen şeyi atanan değişkende sonradan kullanabiliriz

#my_Friend = {"name":"deniz", "age":25, "gender":"woman"}
"""