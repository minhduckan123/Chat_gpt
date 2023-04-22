from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#Dòng from selenium.webdriver.common.by import By và from selenium.webdriver.support.ui import WebDriverWait được sử dụng để import các lớp và phương thức cần thiết từ thư viện Selenium.
from selenium.webdriver.support import expected_conditions as EC#được sử dụng để import module expected_conditions của Selenium và đặt cho nó cái tên tắt là EC.
import os# được sử dụng để import module os trong Python, cho phép tương tác với hệ điều hành.




id_fb = 100018590648536

def engine_gui_anh(driver):# là một hàm con (function) nhận đối số là một đối tượng driver của Selenium. Hàm này được sử dụng để tải lên và gửi 2 ảnh (img1.jpg và img2.jpg) lên Facebook Messenger thông qua giao diện người dùng của trình duyệt.
    them_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Add Photos"]'))).click()
    #Dòng them_anh sử dụng WebDriverWait để chờ đến khi phần tử có xpath //input[@value="Add Photos"] xuất hiện trên trang web, sau đó thực hiện click vào nút đó.
    gui_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="file1"]')))
    gui_anh.send_keys(f'{os.getcwd()}/img1.jpg')
    #Dòng gui_anh sử dụng WebDriverWait để chờ đến khi phần tử có xpath //input[@name="file1"] xuất hiện trên trang web, sau đó gửi đường dẫn của file img1.jpg lên phần tử đó.
    gui_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="file2"]')))
    gui_anh.send_keys(f'{os.getcwd()}/img2.jpg')
    #Dòng tương tự áp dụng cho ảnh thứ 2 với xpath //input[@name="file2"].
    gui = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Send"]'))).click()
    #Dòng gui sử dụng WebDriverWait để chờ đến khi phần tử có xpath //input[@value="Send"] xuất hiện trên trang web, sau đó thực hiện click vào nút đó để gửi tin nhắn chứa 2 ảnh đã tải lên.
