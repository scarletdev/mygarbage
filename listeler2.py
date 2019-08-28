#-*-coding:utf-8-*-

langs = ['turkish','english','russian','chinese',39]

print(langs)
langs.sort() #alfabetik sırala
print(langs)
langs.sort(reverse=True) #alfabenin tersine sırala
print(langs)

print(sorted(langs)) #alfabetik sıralasın ancak veri elimizde olduğu gibi dursun

"""
print(langs)
langs.remove('english') #kaldırma
print(langs)

print(langs)
langs2 = langs.pop() #pop() metodu ile sildiğim liste elemanına ulaşabiliyorum.
print(langs)
print(langs2)
print(type(langs2))


print(langs)
del langs[1]
print(langs)

print(langs)
langs.insert(5,'sadads') # 1-öğenin ekleneceği yer,index,2-listeye eklenecek öğe
print(langs)

print("Önceki hali: ",langs)
#langs.append('spanish')
#langs.append('portuguese')
print("Sonraki hali: ",langs)"""
