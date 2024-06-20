from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "https://oauth.vk.com/authorize?client_id=6287487&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1"

ses = HTMLSession()
res = ses.get(url=url)
el = BeautifulSoup(res.text, features="lxml").find_all("a",{"class":"oauth_reg_link"})
login = input("телефон:")
Password = input("пароль: ")