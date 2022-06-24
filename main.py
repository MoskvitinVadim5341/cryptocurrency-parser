
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


ua = UserAgent()

user_agent = ua.random
print(f"User agent: {user_agent}")


heder = {
    "User-Agent":user_agent,
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
responose = requests.get("https://minfin.com.ua/currency/crypto/", headers=heder)
soupe = BeautifulSoup(responose.text, "lxml")
criptos = soupe.find("div", class_="sc-1fj68h4-0 gsaTdv").find_all("div", class_="sc-18qu8it-0 ifYZrl")
criptos = criptos[0:26]
names = soupe.find_all("div", class_="sc-18qu8it-10 eMjHIh")
names = names[0:19]
z = 0
for i in range(len(criptos)):
    if i % 2 == 0:
        
        print(names[z].text + ": " + criptos[i].text)
        z += 1
    else:
        continue
