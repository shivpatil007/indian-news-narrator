from bs4 import BeautifulSoup
import requests
import re
from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language='en'
a=[]
source= requests.get("https://www.ndtv.com/india").text
soup = BeautifulSoup(source,"lxml")
divs = soup.find("div",{"class":"new_storylising","id":"ins_storylist"})
uls=divs.ul
for lis in uls.find_all("li"):
    x=re.findall('img alt="(.+?)"',str(lis.a))
    a.append(x)
l="Todays news are "
for i in range(16):
    l+=str(a[i])   
sp=gTTS(text = l ,lang = language ,slow=False)
sp.save(audio)
playsound(audio)
    