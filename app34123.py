#-*-coding:utf-8-*-

"""
boş liste,tuple,set ve dictionary oluştur
"""

bosliste = []      # Liste
bosliste2 = list() # boş liste oluşturmanın farklı bir yolu
print(bosliste)
print(type(bosliste))

my_tuple = ("lahmacun","iskender",39,"ekler",91) # Tuple / Demet
my_tuple2 = tuple() #boş tuple oluşturmanın 2. yolu
print(my_tuple)  
print(type(my_tuple))

my_set = {"b","a","c",2,23,8,1} # Set
my_set2 = set() #boş set oluşturma
dict1 = {} #Boş set böyle OLUŞTURULAMAZ! Type = dictionary olur
print(my_set)
print(type(my_set))
print(type(my_set2))
print(type(dict1)) #output: type = dictionary {} olsa bile boş bırakılırsa dict olur!

my_dictionary = {"language":"python","difficulty":"easy"} # Dictionary / Sözlük
my_dictionary2 = {}
my_dictionary3 = dict()
print(my_dictionary)
print(type(my_dictionary))

listdictionary = [
{"name":"saitama","age":"25","power":"one punch"},
{"name":"genos","age":"19","power":70}
]
print(listdictionary)
print(type(listdictionary))
print(type(listdictionary[0]))
#----------------------------------------