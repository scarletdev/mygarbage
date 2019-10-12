#-*-coding:utf-8-*-

xd = str(input("""
0 - Çıkış
1 - Toplama
2 - Çıkarma
3 - Bölme
4 - Çarpma

"""))

sayi1 = float(input("Bir sayı giriniz: "))
sayi2 = float(input("Bir sayı daha giriniz: "))

if xd == "0":
    raise SystemExit()
elif xd == "1":
    result = sayi1+sayi2
    print(f"Sonuç: {result}")
elif xd == "2":
    result = sayi1-sayi2
    print(f"Sonuç: {result}")
elif xd == "3":
    result = sayi1/sayi2
    print(f"Sonuç: {result}")
elif xd == "4":
    result = sayi1*sayi2
    print(f"Sonuç: {result}")