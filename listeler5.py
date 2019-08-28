#-*-coding:utf-8-*-
"""
sehirler = ["ankara","izmir","istanbul"]
print(sehirler)

print("-"*127) #ayırma amaçlı listeyle alakası yok!

sehirler2 = sehirler #birinci listenin referansını ikinci listeye atadık
print(sehirler2)
print("-"*127)

sehirsec = input("Şehir ismi giriniz: ") #kullanıcıdan şehir ismi al
sehirler.append("antalya") #sehirler listesine antalyayı ekledik
sehirler.append(sehirsec)        #sehirler listesine kullanıcının şehrini ekledik

print(sehirler)
print(sehirler2)
"""
#---------------------------------------------------------------------------------------
gods = ["yhwh","zeus","ra"]

gods2 = gods[:] #yapılan değişiklerin kopyalanmasını istemiyorsak [:] ekliyoruz (örnek:.append)

print(gods)
print(gods2)

gods.append("atena")

print("-"*127)

print(gods)
print(gods2)