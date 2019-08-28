#-*-coding:utf-8-*-

name = 'falcai software'

print(len(name))

print(name[0:6]) #0 ile 6 arasını yazdır 6yı saymadan

print(name[:7]) #yine yukarıdaki gibi 0dan 7ye kadar gidiyor (7 dahil olmadan)

print(name.title()) #baş harfleri büyük yap

print(name.upper()) #eğer hepsi küçük harfse hepsini büyük harf yap.

print(name.lower()) #eğer hepsi büyük harfse hepsini küçük harf yap.

print(name.count('c')) #içinde kaç c harfi varsa say

print(name.find('n'))

print(name.replace('falcai','calfai')) # 1. eski 2.yerleştirilecek olan

print(dir(name))

#print(help(str)) //direkt olarak değişkeni değil de değişkenin veri tipini yazıyoruz.

#print(help(str.encode)) #metodlar hakkında bilgi sahibi olma



