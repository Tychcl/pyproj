from vk_api.audio import VkAudio
from vk_api import VkApi as VK
from selenium import webdriver
from selenium.webdriver.common.by import By
import browsercookie

url = "https://oauth.vk.com/authorize?client_id=6287487&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1"
brov = ["Edge","Chrome","Firefox"]

class music:
    creator = "unknown"
    Name = "NoName"
    len = 0

def gettoken(int):
    cookies = eval(f'browsercookie.{brov[int]}().cookie_files[0]') + ".txt"
    head = eval(f'webdriver.{brov[int]}Options()')
    head.add_argument("--headless")
    with eval(f'webdriver.{brov[int]}(options=head)') as web:
        web.add_cookie(cookies)
        web.get(url)
        print(web.current_url,web.title)
        el = web.find_element(By.CLASS_NAME,"oauth_reg_link")
        print(el.text)

gettoken(int(input("0, 1, 2\n")))
#token="vk1.a.eHQIx_cEmXPpsUTWjBBhZ5wmdIcmRdzPMMcLt5YXqOjZ4TTBjgAGdNzUx203PpL-I1PPCDJ2iJ3dGwJGYaQ65e1N-cS2Dv7DerBAfNk0Zed_12gYJ-mrU5QRDKQH2BPeALENKIHoW1Hfez6Vu5z7p-mzg-B_DDvLCb1q043oMtgupBU6EP0ZW_mfSjV3ratZHEIbl4-9c4BcrQIuExL9pA"
#ses = VK(token=token)
#vkU = ses.get_api()
#audio = VkAudio(ses)
#print(ses.method(method='users.get'))
#vk.method('users.get')[0]['id']
#print(audio.get_iter())