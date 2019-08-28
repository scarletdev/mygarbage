from alive_progress import alive_bar
uzunluk = input("1-1000000000 arası bir sayı girin: ")
items = range(int(uzunluk))
#items = range(1000000000)
with alive_bar(len(items)) as bar:
    for item in items:
         bar()

#ETA of 140000000000 is 370~390 Days