#-*-coding:utf-8-*-

"""
Görev: key'lerden liste oluştur,
value'lardan liste oluştur,
valuelar toplamını çıkar.
"""
my_friends = {"ali":23,"ömer":53,"elif":38}
my_key_list = []
my_value_list = []

for k, v in my_friends.items():
    my_key_list.append(k)
    my_value_list.append(v)
print(my_key_list)
print(my_value_list)
print(sum(my_value_list))

