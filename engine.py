import requests#Nhập thư viện requests, được sử dụng để thực hiện các yêu cầu HTTP.
from bs4 import BeautifulSoup#Nhập thư viện BeautifulSoup, được sử dụng để phân tích cú pháp (parse) các trang web HTML.



proxy = {'https': 'http://user22630:DDDky@ipv6sv10.proxyapp.vn:22630/'}#Khai báo biến proxy để đặt proxy khi gửi yêu cầu HTTP. Proxy được sử dụng để ẩn địa chỉ IP thực của máy gửi yêu cầu.
cookies = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681741045247%2C%22v%22%3A1%7D;fr=0zKcILjib3BigrtQQ.AWVhGa_58slkmiyH8kpZXCv2QSE.BkPVTz.Zx.AAA.0.0.BkPVTz.AWU3Seaj2_g;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021%3A%3AAcXMTTyF0xa3EkxyMZ0LEhkIFFamR7AEODSac-b3jA;datr=e1k7ZOv6CRBR1_aQgIgigvvY;wd=929x887;c_user=100082496852554;locale=en_GB;sb=7qIqY270Jc2jg9i7A5dkid5x'
#Khai báo biến cookies để đặt giá trị cookie. Cookie là các dữ liệu được lưu trữ trên máy tính của người dùng và được sử dụng để theo dõi trạng thái đăng nhập và lưu trữ dữ liệu liên quan đến phiên làm việc.
id_fb = 100018590648536#Khai báo biến id_fb để đặt giá trị ID Facebook người nhận tin nhắn.

headers = {
    #Khai báo biến headers để đặt các tiêu đề (headers) cho yêu cầu HTTP. Tiêu đề (headers) là các thông tin bổ sung được gửi cùng với yêu cầu HTTP để điều khiển cách thức hoạt động của yêu cầu.
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

s = requests.Session()#Khai báo biến s là một đối tượng session của requests, được sử dụng để duy trì trạng thái của phiên làm việc, bao gồm cả cookie và proxy.
s.proxies.update(proxy)
def engine_nhan_tin(content):#Định nghĩa hàm engine_nhan_tin(content) để gửi tin nhắn với nội dung được truyền vào.
    r = s.get(f'https://mbasic.facebook.com/messages/read/?tid=cid.c.{id_fb}%3A100082496852554', headers=headers)
    #Sử dụng đối tượng session s để gửi yêu cầu GET đến trang web Messenger của Facebook.
    with open('html.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
    page = r.content
    soup = BeautifulSoup(page, 'html.parser')
    fb_dtsg = soup.find_all("input", {"name":"fb_dtsg"})[-1]['value']
    jazoest = soup.find_all("input", {"name":"jazoest"})[-1]['value']
    tids = soup.find_all("input", {"name":"tids"})[-1]['value']
    csid = soup.find_all("input", {"name":"csid"})[-1]['value']
    #Sử dụng BeautifulSoup để phân tích cú pháp trang web trả về từ yêu cầu GET. Lấy các giá trị cần thiết từ trang web, bao gồm fb_dtsg, jazoest, tids, và csid.
    payload = {#Định nghĩa payload (dữ liệu gửi đi) cho yêu cầu POST để gửi tin nhắn, bao gồm các giá trị đã lấy từ trang web và nội dung tin nhắn được truyền vào.
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

    send_message = s.post("https://mbasic.facebook.com/messages/send/", headers= headers, data= payload)#là dùng để gửi yêu cầu POST đến đường dẫn url_send với dữ liệu (payload) được truyền vào là nội dung tin nhắn cần gửi, và tiêu đề (headers) được đặt trong biến headers.
    # print(content, "\nTrạng thái:", send_message.status_code)

