#-*-coding:utf-8-*-

#                     nested list mantığı:
#             0.index  [------1.index-----] #2.index
nestedlist = ["chrome",["firefox","yandex"],"opera"]

print("Nested list: ",nestedlist)
print("1. index: ",nestedlist[1])
print("1.indexin 0. indexi: ",nestedlist[1][0])

print("-"*125) #çizgi ile ayır

dersler = ["matematik","edebiyat","fizik","kimya","tarih","biyoloji"]
#görev: ikinci ve son liste elemanının çıktısını al
print(dersler)
print(dersler[2].upper())
print(dersler[-1].upper()) #uzun listelerde -1 daha fonksiyoneldir.

print("-"*125)

dersler = ["matematik","edebiyat","fizik","kimya","tarih","biyoloji"]
print(dersler[2:4]) #fizik ve kimya elemanlarının çıktısını al
print(dersler[:2]) #ilk iki elemanın çıktısını al
print(dersler[-2:]) #son iki elemanın çıktısını al