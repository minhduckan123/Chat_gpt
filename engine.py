import requests
from bs4 import BeautifulSoup
from time import sleep



proxy = {'https': 'http://user22630:DDDky@ipv6sv10.proxyapp.vn:22630/'}
cookies = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681741045247%2C%22v%22%3A1%7D;fr=0zKcILjib3BigrtQQ.AWVhGa_58slkmiyH8kpZXCv2QSE.BkPVTz.Zx.AAA.0.0.BkPVTz.AWU3Seaj2_g;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021%3A%3AAcXMTTyF0xa3EkxyMZ0LEhkIFFamR7AEODSac-b3jA;datr=e1k7ZOv6CRBR1_aQgIgigvvY;wd=929x887;c_user=100082496852554;locale=en_GB;sb=7qIqY270Jc2jg9i7A5dkid5x'
id_fb = 100018590648536

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
def engine_nhan_tin(content):
    r = s.get(f'https://mbasic.facebook.com/messages/read/?tid=cid.c.{id_fb}%3A100082496852554', headers=headers)
    with open('html.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
    page = r.content
    soup = BeautifulSoup(page, 'html.parser')
    fb_dtsg = soup.find_all("input", {"name":"fb_dtsg"})[-1]['value']
    jazoest = soup.find_all("input", {"name":"jazoest"})[-1]['value']
    tids = soup.find_all("input", {"name":"tids"})[-1]['value']
    csid = soup.find_all("input", {"name":"csid"})[-1]['value']
    payload = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'body': content,
        'send': "Send",
        'tids': tids,
        'wwwupp': 'C3',
        f'ids[{id_fb}]': id_fb,
        'cver': 'legacy',
        'csid': csid,
    }

    send_message = s.post("https://mbasic.facebook.com/messages/send/", headers= headers, data= payload)
    # print(content, "\nTrạng thái:", send_message.status_code)

