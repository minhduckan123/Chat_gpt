import requests
from bs4 import BeautifulSoup #Nhập lớp BeautifulSoup từ thư viện bs4, được sử dụng để phân tích cú pháp HTML và XML.
from selenium import webdriver #Nhập lớp webdriver từ thư viện selenium, được sử dụng để tự động hóa trình duyệt web.
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #Nhập lớp DesiredCapabilities từ module selenium.webdriver.common.desired_capabilities, được sử dụng để cấu hình các khả năng mong muốn cho các trình điều khiển web.
import os #Nhập module os, cung cấp các hàm để tương tác với hệ điều hành.
from time import sleep #Nhập hàm sleep từ module time, được sử dụng để thêm độ trễ vào mã nguồn.
from engine import engine_nhan_tin #Nhập hàm có tên engine_nhan_tin từ module có tên engine.
from engine_v2 import engine_gui_anh#Nhập hàm có tên engine_gui_anh từ module có tên engine_v2.
from main_ai import hoi_thoai, ve_tranh #Nhập hai hàm có tên hoi_thoai và ve_tranh từ module có tên main_ai.



proxy = {'https': 'http://user22630:DDDky@ipv6sv10.proxyapp.vn:22630/'} #Định nghĩa một proxy để gửi các yêu cầu HTTP.
cookies = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681741045247%2C%22v%22%3A1%7D;fr=0zKcILjib3BigrtQQ.AWVhGa_58slkmiyH8kpZXCv2QSE.BkPVTz.Zx.AAA.0.0.BkPVTz.AWU3Seaj2_g;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021%3A%3AAcXMTTyF0xa3EkxyMZ0LEhkIFFamR7AEODSac-b3jA;datr=e1k7ZOv6CRBR1_aQgIgigvvY;wd=929x887;c_user=100082496852554;locale=en_GB;sb=7qIqY270Jc2jg9i7A5dkid5x'
# Định nghĩa một chuỗi chứa giá trị của cookie để xác thực.
id_fb = 100018590648536#Định nghĩa một biến id_fb có giá trị là một số nguyên.
name_fb = "Trịnh Minh Đức"#Định nghĩa một biến name_fb có giá trị là một chuỗi ký tự.

path_chromedriver = f'{os.getcwd()}/chromedriver.exe'# Định nghĩa một biến path_chromedriver chứa đường dẫn đến tệp chromedriver.exe trong thư mục làm việc hiện tại.


caps = DesiredCapabilities().CHROME#Tạo một đối tượng của lớp DesiredCapabilities cho trình duyệt Chrome.
caps["pageLoadStrategy"] = "eager"# Thiết lập chiến lược tải trang là "eager".
chrome_options = webdriver.ChromeOptions()#Khởi tạo đối tượng chrome_options từ lớp webdriver.ChromeOptions() trong thư viện selenium.webdriver.
chrome_options.add_argument('--log-level=3')#Thêm đối số --log-level=3 vào chrome_options, cho phép đặt mức độ ghi log của trình duyệt Chrome là 3, tức là chỉ ghi lại các thông báo lỗi.
chrome_options.add_argument('--headless')#Thêm đối số --headless vào chrome_options, cho phép chạy trình duyệt ở chế độ "headless", tức là không hiển thị giao diện đồ họa của trình duyệt.
chrome_options.add_argument('--blink-settings=imagesEnabled=false')#Thêm đối số --blink-settings=imagesEnabled=false vào chrome_options, cho phép tắt tải hình ảnh trong trang web để giảm tải băng thông và tăng tốc độ tải trang.
chrome_options.add_argument("--disable-notifications")#Thêm đối số --disable-notifications vào chrome_options, cho phép vô hiệu hóa thông báo của trình duyệt.
chrome_options.add_argument("--mute-audio")#Thêm đối số --mute-audio vào chrome_options, cho phép tắt âm thanh của trình duyệt.
driver = webdriver.Chrome(path_chromedriver, options=chrome_options)# Khởi tạo đối tượng driver từ lớp webdriver.Chrome() trong thư viện selenium.webdriver, với đường dẫn đến file chromedriver và các tùy chọn được định nghĩa trong chrome_options.
    
driver.get(f"https://www.facebook.com/messages/t/{id_fb}/")# Mở trang web Facebook Messenger với URL được định dạng dựa trên id_fb, sử dụng phương thức get() của đối tượng driver.
sleep(5)#Dừng thực thi chương trình trong 5 giây, cho phép trang web được tải hoàn chỉnh trước khi tiếp tục thực thi.
cookies_fb = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681741045247%2C%22v%22%3A1%7D;fr=0zKcILjib3BigrtQQ.AWVhGa_58slkmiyH8kpZXCv2QSE.BkPVTz.Zx.AAA.0.0.BkPVTz.AWU3Seaj2_g;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021%3A%3AAcXMTTyF0xa3EkxyMZ0LEhkIFFamR7AEODSac-b3jA;datr=e1k7ZOv6CRBR1_aQgIgigvvY;wd=929x887;c_user=100082496852554;locale=en_GB;sb=7qIqY270Jc2jg9i7A5dkid5x'
#Định nghĩa chuỗi chứa các cookie của tài khoản Facebook, được lưu trữ trong biến cookies_fb.
cookie_fb = [i.strip() for i in cookies_fb.split(";") if i != "" and i != "\n"]#Tách các cookie trong chuỗi cookies_fb thành danh sách các phần tử, loại bỏ khoảng trắng và ký tự xuống dòng không cần thiết.
for ck in cookie_fb:#Duyệt qua từng cookie trong danh sách cookie_fb.
    name, value = ck.split("=",1)#Đây là một phép gán đồng thời (multiple assignment) để tách chuỗi ck thành hai phần tử name và value bằng cách cắt chuỗi dựa trên dấu "=" và giới hạn số lần cắt là 1.
    driver.add_cookie({"name":name, "value":value})# Đây là lệnh để thêm cookie vào trình duyệt web đang được điều khiển bởi driver. Cookie được đóng gói trong một từ điển (dictionary) với hai cặp giá trị "name" và "value" tương ứng với tên và giá trị của cookie.
driver.refresh()# Đây là lệnh để làm mới trang web đang được điều khiển bởi driver.
sleep(5)
driver.get(f"https://mbasic.facebook.com/messages/t/{id_fb}/")#Điều hướng đến trang web của Facebook Messenger với URL được tạo ra từ chuỗi định dạng (f-string) và giá trị của biến id_fb.
sleep(5)
cookies_fb = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681741045247%2C%22v%22%3A1%7D;fr=0zKcILjib3BigrtQQ.AWVhGa_58slkmiyH8kpZXCv2QSE.BkPVTz.Zx.AAA.0.0.BkPVTz.AWU3Seaj2_g;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021%3A%3AAcXMTTyF0xa3EkxyMZ0LEhkIFFamR7AEODSac-b3jA;datr=e1k7ZOv6CRBR1_aQgIgigvvY;wd=929x887;c_user=100082496852554;locale=en_GB;sb=7qIqY270Jc2jg9i7A5dkid5x'
cookie_fb = [i.strip() for i in cookies_fb.split(";") if i != "" and i != "\n"]
for ck in cookie_fb:
    name, value = ck.split("=",1)
    driver.add_cookie({"name":name, "value":value})
driver.refresh()

headers = {#Đây là một từ điển (dictionary) chứa các thông tin đầu vào (headers) để được gửi kèm với các yêu cầu HTTP. Các thông tin này bao gồm cookie, user-agent, sec-ch-ua, sec-ch-ua-mobile, sec-ch-ua-platform, sec-fetch-dest, sec-fetch-mode, sec-fetch-site, sec-fetch-user, upgrade-insecure-requests.
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


s = requests.Session()#Đây là đối tượng Session của thư viện requests, được sử dụng để duy trì trạng thái phiên làm việc giữa các yêu cầu HTTP, bao gồm cả cookie và thông tin đăng nhập.
s.proxies.update(proxy)# Đây là lệnh để cập nhật địa chỉ proxy mà Session sẽ sử dụng để gửi yêu cầu HTTP. Biến proxy được định nghĩa trước đó nhưng không được đưa ra trong đoạn mã này.

def chat_bot(mode= 0):#Đây là định nghĩa hàm chat_bot với tham số mode mặc định là 0.
    while True:#Hàm chat_bot() sẽ tiếp tục chạy vòng lặp vô hạn, liên tục kiểm tra tin nhắn mới từ cuộc trò chuyện trên Facebook Messenger, trả lời tin nhắn của người dùng và thực hiện các chức năng vẽ tranh tương ứng.
        link = s.get(f'https://mbasic.facebook.com/messages/read/?tid=cid.c.{id_fb}%3A100082496852554', headers=headers)#Đây là lệnh để gửi yêu cầu HTTP GET đến địa chỉ URL được xây dựng từ chuỗi format (f-string) với giá trị của biến id_fb, để đọc tin nhắn trên Facebook Messenger. Kết quả của yêu cầu được lưu vào biến link.Đây là lệnh để gửi yêu cầu HTTP GET đến địa chỉ URL được xây dựng từ chuỗi format (f-string) với giá trị của biến id_fb, để đọc tin nhắn trên Facebook Messenger. Kết quả của yêu cầu được lưu vào biến link.
        page = link.content#Lấy nội dung của trang web đã được tải về và lưu vào biến page.
        soup = BeautifulSoup(page, 'html.parser')#Sử dụng thư viện BeautifulSoup để phân tích cú pháp của trang web và lưu kết quả vào biến soup, để tiện cho việc trích xuất dữ liệu từ HTML.

        last_guy = soup.find("div", {"id":"messageGroup"}).select("div > div > div > a > strong")[-1].get_text()#Tìm và trích xuất tên của người gửi tin nhắn cuối cùng trong cuộc trò chuyện từ trang web đã phân tích cú pháp. Tên này được lưu vào biến last_guy.
        last_message = soup.find("div", {"id":"messageGroup"}).find_all("div", recursive=False)[-1].find_all("div", recursive=False)[-1].find("span").get_text()#Tìm và trích xuất nội dung của tin nhắn cuối cùng trong cuộc trò chuyện từ trang web đã phân tích cú pháp. Nội dung này được lưu vào biến last_message.
        if last_guy == name_fb:#Kiểm tra nếu tin nhắn cuối cùng là từ người dùng có tên name_fb (được khai báo trước đó).
            # print(last_message)
            if mode == 0:
                if "vẽ" in last_message.lower():#Kiểm tra nếu nội dung của tin nhắn cuối cùng chứa từ "vẽ" (không phân biệt hoa thường).
                    engine_nhan_tin(hoi_thoai("Hãy viết lại câu sau với nghĩa không đổi:\nBạn muốn vẽ tranh về điều gì?", mode= 1, role_system= "AI viết lại câu."))#Gọi hàm engine_nhan_tin() với tham số là kết quả của hàm hoi_thoai(), để trả lời tin nhắn của người dùng
                    mode = 1#Gán giá trị 1 cho biến mode, đây là một biến điều khiển chế độ của trò chuyện. Nếu mode = 1, tức là đang trong chế độ trả lời câu hỏi về việc vẽ tranh.
                else:#Nếu tin nhắn cuối cùng không chứa từ "vẽ", điều này có nghĩa là đang trong chế độ mặc định.
                    engine_nhan_tin(hoi_thoai(last_message))
            else:
                if "dừng" in last_message.lower():#Kiểm tra nếu nội dung của tin nhắn cuối cùng chứa từ "dừng" (không phân biệt hoa thường), đây là tín hiệu để thoát khỏi chế độ vẽ tranh.
                    mode = 0#Gán giá trị 0 cho biến mode, đây là chế độ mặc định của trò chuyện.
                    engine_nhan_tin(hoi_thoai("Cảm ơn bạn."))#Gọi hàm engine_nhan_tin() với tham số là kết quả của hàm hoi_thoai(), để trả lời tin nhắn của người dùng và thông báo "Cảm ơn bạn".
                else:
                    ve_tranh(last_message)#Gọi hàm ve_tranh() với tham số là nội dung của tin nhắn cuối cùng, để thực hiện việc vẽ tranh dựa trên tin nhắn của người dùng.
                    engine_gui_anh(driver)#Gọi hàm engine_gui_anh() với tham số là đối tượng driver, để gửi ảnh đã vẽ đến người dùng qua Facebook Messenger.
        else:#Nếu tin nhắn cuối cùng không phải từ người dùng hiện tại, thì sẽ chờ 10 giây trước khi kiểm tra lại tin nhắn mới.
            sleep(10)

chat_bot()#chạy hàm chat_bot()