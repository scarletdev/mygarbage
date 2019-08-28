#-*-coding:utf-8-*-

numbers = [number for number in range(1,11)] #daha kısa hali
print(numbers)

print("-"*110) #ayırmak için

numlist = [23,8,3,12,67,99,5,1,4]

print(numlist)
print(min(numlist)) #min = değerlerin aralarından en küçük olanı.
print(max(numlist)) #max = değerlerin aralarından en büyük olanı.
print(sum(numlist)) #sum = değerlerin toplamı.
print("-"*110) #ayırmak için

for number in range(1,11): #1,2,3,4,5,6,7,8,9,10
    print(number)

print("-"*110) #ayırmak için

for number in range(2,21,2): #çift sayılarla 2 arttırarak 20'ye kadar git
    print(number)

print("-"*110) #ayırmak için

numbers = list(range(1,11))

print(numbers)
print(type(numbers))