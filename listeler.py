#-*-coding:utf-8-*-
    #    Başlangıç 0      1         2          3       4      Bitiş 5 /// 0:5 Kısaca
cities = ['barcelona','florenca','belgrad','tahran','paris','seattle']



cities[1] = 'istanbul'

cities.append('tiflis') #append = eklemek / listeye eleman ekleme
print(cities)

print(cities[-1]) #-1 <= sağdan başlıyor

print(cities[0]) #liste 0dan başlar yani ilk eleman

print(cities[1]) #listenin 1. elemanı / 0. elemandan sonra gelir

print(type(cities)) #listenin tipini yazdır#

print(len(cities)) #listenin uzunluğu

print(max(cities[:3])) # 0:5 yerine :5 de 0dan başlar

print(cities[1:4])

print("\n")

print(cities[0:5])
