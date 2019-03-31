import json
import os 
from bs4 import BeautifulSoup

def replace(msg):
    markup = open("/home/pi/bhargavbhegde7.github.io/utils.html")
    soup = BeautifulSoup(markup.read(), 'html5lib')
    pTag = soup.find("p", {"id": "tunnel_url"})
    pTag.string.replaceWith(msg)
    print(pTag.string)

    html = soup.prettify("utf-8")
    with open("/home/pi/bhargavbhegde7.github.io/utils.html", "wb") as file:
        file.write(html)

os.system("curl  localhost:4040/api/tunnels > /home/pi/personal_helper_service/tunnels.json")

with open('/home/pi/personal_helper_service/tunnels.json') as data_file:
    datajson = json.load(data_file)

msg = ""
for i in datajson['tunnels']: 
    if "https" in i['public_url']:
        msg = msg + i['public_url'] +"\n"    
        break
print (msg)
replace(msg)
