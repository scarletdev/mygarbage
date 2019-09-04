#-*-coding:utf-8-*-

# youtube.com/Scarlet
# Written by Scarlet
# discord.me/Scarlet

import socket
import webbrowser
import platform

def osfind():
    osname = platform.platform()
    print(osname)

def m_addition(x,y,z):
    result = x+y+z
    print(result)

def m_multiplication(x,y,z):
    result = x*y*z
    print(result)

def m_division(x,y,z):
    result = x/y/z
    print(result)

def m_subtraction(x,y,z):
    result = x-y-z
    print(result)

def m_getmod(x,y):
    result = x%y
    print(result)

def m_exponent(x,y):
    result = x**y
    print(result)

def m_aliquat(x,y):
    result = x//y
    print(result)

def hellouserwIP(wMessage):
    pcname = socket.gethostname()
    ipadress = socket.gethostbyname(pcname)
    print(wMessage," ",pcname,"({})".format(ipadress))

def hellouser(wMessage):
    pcname = socket.gethostname()
    print(wMessage," ",pcname)

def sayanything(message):
    my_string = str(input(message))
    return sayanything(message)
def calculator():
    print("""
    + for addition
    * for multiplication
    / for division
    - for subtraction
    """)

    x = int(input("1st number: "))
    y = int(input("2nd number: "))
    z = int(input("3nd number: "))

    choice = input("Write the action you want to perform: ")

    if choice == "0":
        raise SystemExit
    elif (choice == "+"):
        result = x+y+z
        print("{} + {} + {} = {}".format(x,y,z,result))
    elif choice == "*":
        result = x*y*z
        print("{} x {} x {} = {}".format(x,y,z,result))
    elif choice == "/":
        result = x/y/z
        print("{} / {} / {} = {}".format(x,y,z,result))
    elif choice == "-":
        result = x-y-z
        print("{} - {} - {} = {}".format(x,y,z,result))

def vkihesapla(message):
    boy = float(input("Vücut Uzunluğunuz(cm): "))
    kilo = float(input("Vücut Ağırlığınız(kg): "))
    sonuc = kilo / (boy**2)
    print(message," ",sonuc)

def openwebsite(url,msg=True):
    bool(msg)
    webbrowser.open_new_tab(url)
    if msg == True:
        print("Opening {}...".format(url))
#openwebsite("https://www.google.com/",False)

def openAwebsite(msg=True):
    bool(msg)
    askUrl = str(input("Url: "))
    webbrowser.open_new_tab(askUrl)
    if msg == True:
        print("Opening {}...".format(askUrl))
#openAwebsite(True) #openAwebsite(False)

m_exponent(14,14)
