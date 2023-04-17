import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from time import sleep
from engine import engine_nhan_tin
from engine_v2 import engine_gui_anh
from main_ai import hoi_thoai, ve_tranh



proxy = {'https': 'http://user22630:DDDky@ipv6sv10.proxyapp.vn:22630/'}
cookies = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681741045247%2C%22v%22%3A1%7D;fr=0zKcILjib3BigrtQQ.AWVhGa_58slkmiyH8kpZXCv2QSE.BkPVTz.Zx.AAA.0.0.BkPVTz.AWU3Seaj2_g;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021%3A%3AAcXMTTyF0xa3EkxyMZ0LEhkIFFamR7AEODSac-b3jA;datr=e1k7ZOv6CRBR1_aQgIgigvvY;wd=929x887;c_user=100082496852554;locale=en_GB;sb=7qIqY270Jc2jg9i7A5dkid5x'

id_fb = 100018590648536
name_fb = "Trịnh Minh Đức"

path_chromedriver = f'{os.getcwd()}/chromedriver.exe'


caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(path_chromedriver, options=chrome_options)
    
driver.get(f"https://www.facebook.com/messages/t/{id_fb}/")
sleep(5)
cookies_fb = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681741045247%2C%22v%22%3A1%7D;fr=0zKcILjib3BigrtQQ.AWVhGa_58slkmiyH8kpZXCv2QSE.BkPVTz.Zx.AAA.0.0.BkPVTz.AWU3Seaj2_g;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021%3A%3AAcXMTTyF0xa3EkxyMZ0LEhkIFFamR7AEODSac-b3jA;datr=e1k7ZOv6CRBR1_aQgIgigvvY;wd=929x887;c_user=100082496852554;locale=en_GB;sb=7qIqY270Jc2jg9i7A5dkid5x'
cookie_fb = [i.strip() for i in cookies_fb.split(";") if i != "" and i != "\n"]
for ck in cookie_fb:
    name, value = ck.split("=",1)
    driver.add_cookie({"name":name, "value":value})
driver.refresh()
sleep(5)
driver.get(f"https://mbasic.facebook.com/messages/t/{id_fb}/")
sleep(5)
cookies_fb = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681741045247%2C%22v%22%3A1%7D;fr=0zKcILjib3BigrtQQ.AWVhGa_58slkmiyH8kpZXCv2QSE.BkPVTz.Zx.AAA.0.0.BkPVTz.AWU3Seaj2_g;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021%3A%3AAcXMTTyF0xa3EkxyMZ0LEhkIFFamR7AEODSac-b3jA;datr=e1k7ZOv6CRBR1_aQgIgigvvY;wd=929x887;c_user=100082496852554;locale=en_GB;sb=7qIqY270Jc2jg9i7A5dkid5x'
cookie_fb = [i.strip() for i in cookies_fb.split(";") if i != "" and i != "\n"]
for ck in cookie_fb:
    name, value = ck.split("=",1)
    driver.add_cookie({"name":name, "value":value})
driver.refresh()

headers = {
        'cookie': cookies,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

s = requests.Session()
s.proxies.update(proxy)

def chat_bot(mode= 0):
    while True:
        link = s.get(f'https://mbasic.facebook.com/messages/read/?tid=cid.c.{id_fb}%3A100082496852554', headers=headers)
        page = link.content
        soup = BeautifulSoup(page, 'html.parser')

        last_guy = soup.find("div", {"id":"messageGroup"}).select("div > div > div > a > strong")[-1].get_text()
        last_message = soup.find("div", {"id":"messageGroup"}).find_all("div", recursive=False)[-1].find_all("div", recursive=False)[-1].find("span").get_text()
        if last_guy == name_fb:
            # print(last_message)
            if mode == 0:
                if "vẽ" in last_message.lower():
                    engine_nhan_tin(hoi_thoai("Hãy viết lại câu sau với nghĩa không đổi:\nBạn muốn vẽ tranh về điều gì?", mode= 1, role_system= "AI viết lại câu."))
                    mode = 1
                else:
                    engine_nhan_tin(hoi_thoai(last_message))
            else:
                if "dừng" in last_message.lower():
                    mode = 0
                    engine_nhan_tin(hoi_thoai("Bạn không những là một nhân viên tốt mà còn là một họa sĩ đại tài."))
                else:
                    ve_tranh(last_message)
                    engine_gui_anh(driver)
        else:
            sleep(10)

chat_bot()