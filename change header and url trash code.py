import requests
print("""
this is just shitty testing
with this script you can select;
<url>,<user-agent's name>.
Why? Idk,fuck life. bye.
---------------------------------------------------------------------------------
Written by Scarlet\n
""")
url = str(input("Enter requestbin.com url(Example: https://eniyuql34986o.x.pipedream.net): "))

useragent_text = input("User-Agent:")

r = requests.post(url,headers={"user-agent":useragent_text})