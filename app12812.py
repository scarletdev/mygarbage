#-*-coding:utf-8-*-

my_dict = {"odd_numbers": [1,2,3]}

my_dict["odd_numbers"] = [ my_dict["odd_numbers"][0] ** 2, my_dict["odd_numbers"][1] ** 2, my_dict["odd_numbers"][2] ** 2 ]
#elemanların listeden olduğunu belirtmek için başa ve sona [ ] koyduk.
print(my_dict)

"""
Görev:
my_dict = {"odd_numbers": [1,2,3]}

Yukardaki dictionary yapısında bulunan tüm elemanların karesini alalım,
aynı dictionary yapısını update edelim.
"""