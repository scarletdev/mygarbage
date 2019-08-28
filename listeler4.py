#-*-coding:utf-8-*-

str_countries = "usa, turkey, england" #string
c_list = str_countries.split(", ") #sep,maxsplit
print(c_list)

str_email = "succer2983@gmail.com"
my_list = str_email.split("@")
print(my_list)

friends = ["john","mary","castiel","dean","sam","chuck"]

for friend in friends:
    print(f"Arkadaş: {friend}")

print(friends.index('castiel')) # "verinin"'in hangi indexde olduğunu öğrenme
print('john' in friends) # listenin içinde olup olmadığını tespit etme
