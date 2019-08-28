#-*-coding:utf-8-*-

"""
Görev:
2 okul arkadaşı ve numaralardan oluşan bir dictionary oluştur,
başka bir arkadaşı ekle, ekli olan arkadaşı sil.
Update ile bir arkadaşın numarasını değiştir ve yeni arkadaş ekle.
"""

school_friends = {"mehmet":107,"ebru":482} #
print(school_friends)
school_friends["alper"] = 32 #başka bir arkadaşı ekleme
print(school_friends)
del school_friends["ebru"] #ekli olan arkadaşı sil
print(school_friends)
school_friends.update( {"alper":283,"alex":610} )#update ile  arkadaşın numarasını değiş 
#                                                                 ...ve yeni arkadaş ekle
print(school_friends)
