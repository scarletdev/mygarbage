#-*-coding:utf-8-*-

giris = """
  (1) Topla
  (2) Çıkar
  (3) Çarp
  (4) Böl
  (5) Kare Hesapla
  (6) Karekök Hesapla
  (7) Üs Hesapla
"""

print(giris)

a = 1

while a == 1:
    soru = input("İşlem: ")

if soru == "quit":
    print("Çıkılıyor...")
    a = 0
elif soru == 1: #toplama
    sayi1 = int(input("Toplanacak sayıları giriniz: "))
    sayi2 = int(input("Toplanacak sayıları giriniz: "))
    print("{} + {} = {}").format(sayi1,sayi2,sayi1+sayi2)
elif soru == "2": #çıkarma
    sayi1 = int(input("Çıkarılacak sayıları giriniz: "))
    sayi2 = int(input("Çıkarılacak sayıları giriniz: "))
    print("{} + {} = {}").format(sayi1,sayi2,sayi1+sayi2)
elif soru == "3": #çarpma
    sayi1 = int(input("Çarpılacak sayıları giriniz: "))
    sayi2 = int(input("Çarpılacak sayıları giriniz: "))
    print("{} + {} = {}").format(sayi1,sayi2,sayi1*sayi2) 
elif soru == "4": #bölme
    sayi1 = int(input("Bölünecek sayıları giriniz: "))
    sayi2 = int(input("Bölünecek sayıları giriniz: "))
    #I DONT KNOW WHY BUT I DIDNT CONTINUE THAT
