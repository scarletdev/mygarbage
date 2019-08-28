#-*-coding:utf-8-*-

my_dict2 = {"even_numbers": [2,4,6,8,10,12,14,16,18,20] }

for v in my_dict2.values():
    mylist = [] #değerlerin karesini alıp koyacağımız boş bir liste oluşturduk
    for y in v:
        mylist.append(y**2)
my_dict2["even:numbers"] = mylist
print(my_dict2)

"""
my_dict = {"odd_numbers": [1,2,3] }
my_dict["odd_numbers"] = [ my_dict["odd_numbers"][0] ** 2, my_dict["odd_numbers"][1] ** 2, my_dict["odd_numbers"][2] ** 2,  ]

print(my_dict)
"""