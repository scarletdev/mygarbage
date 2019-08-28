#-*-coding:utf-8-*-

#------------------------------------------------------------------------------------
#set:
cities = {"antalya","istanbul","izmir","ankara","burdur"} #set = {"data1","data2"}
#print(type(cities))
print(cities)
cities.add("gaziantep")
print(cities)
cities.update(["edirne","kars"])
print(cities)
cities.remove("ankara") #setten öğe kaldır, öğe zaten yoksa hata verir.
print(cities)
cities.discard("izmir") #remove ile aynı ancak eğer öğe sette yoksa bir şey yapma.
print(cities)
cities.clear() #setin tamamını temizle
print(cities)

del cities #tamamen kaldırma
#print (cities) #del ile setimizi sildiğimiz için setimizin tanımlı olmadığını söyleyecek

#------------------------------------------------------------------------------------

"""
capitals = ("paris","madrid","ankara","washington d.c") #tuple = ("data","data2")
for capital in capitals:
    print(capital)
"""
# Demetler birden fazla veri türünü bir arada bulundurabilen
# virgüllerle veya parantez ile gösterilen
# immutable(değiştirilemeyen) veri tipleridir.

# demet = tuple
#------------------------------------------------------------------------------------