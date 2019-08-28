#-*-coding:utf-8-*-

squares = [num**2 for num in range(1,11)]
print(squares)

#squares = []

#for num in range(1,11):
#    squares.append(num**2)
#print(squares)

"""
#görev: içteki listelerin son elemanlarıyla yeni bir liste oluştur

angels = [["lucifer","micheal"],["raphael","gabriel"],["castiel","dumah"]]

angels2 = []

#kısa yol:
for angel in angels:
    angels2.append(angel[-1])
print(angels2)

#---------

#angels2.append(angels[0][-1]) UZUN YOL#
#angels2.append(angels[1][-1]) UZUN YOL#
#angels2.append(angels[2][-1]) UZUN YOL#
#print(angels2)


#görev: listeyi arttıracak ve azalacak şekilde sırala:

numbers = [8,4,5,1,6,9,2,7,3,10]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#--------------------------------------------------------------------------------------


#görev 1: kimya dersini 'del' ile kaldır
#görev 2: türkçe dersini 'remove' ile kaldır
dersler = ["matematik","fizik","kimya","ingilizce","türkçe"]

del dersler[2] #1. görev.
print(dersler)

dersler.remove('türkçe') #2. görev.
print(dersler)

#--------------------------------------------------------------------------------------

#görev 1: tarih dersini liste başına ekle insert kullanarak
#görev 2: coğrafya dersini listenin sonuna ekle insert kullanarak:

dersler = ["matematik","fizik","kimya","ingilizce","türkçe"]

dersler.insert(0,"tarih") #görev 1.
dersler.insert(len(dersler),"coğrafya") #görev 2.
print(dersler)
#-----------------------------------------------------------------
"""
#---
"""
print("_"*125)
dersler = ["matematik","fizik","kimya","ingilizce","türkçe"]
print(dersler)
print("_"*125)
print("Listenin uzunluğu:",len(dersler))
dersler.append("tarih")
print(dersler)

dersler[len(dersler):] = ["coğrafya"] #append alternatifi
print(dersler)
"""