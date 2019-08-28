#-*-coding:utf-8-*-

"""
Görev:
Değeri sayı olan 3 elemanlı bir dictionary oluştur,
2. sayıyı ve sayıların ortalamasını çıkar.
"""

number_dictionary = {"ahmet":12,"mehmet":15,"nur":47}
print(type(number_dictionary))
print(number_dictionary["mehmet"])
print(sum(number_dictionary.values()) / len(number_dictionary))