from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os




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
driver.set_window_rect(1000,0)
action = ActionChains(driver)
    
    
driver.get("https://mbasic.facebook.com/messages/t/100018590648536/")
sleep(5)
cookies_fb = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1681611582316%2C%22v%22%3A1%7D;fr=0zZoPJbSlLtRN1Y3M.AWW_4hNqbq2PWLAtMo5dJF7OCPs.BkOyMl.Zx.AAA.0.0.BkO1s7.AWUdNB0HS7E;xs=42%3ASTBurjPNROeJ5A%3A2%3A1681611457%3A-1%3A16021;datr=e1k7ZOv6CRBR1_aQgIgigvvY;locale=en_GB;c_user=100082496852554;wd=929x887;sb=7qIqY270Jc2jg9i7A5dkid5x'
cookie_fb = [i.strip() for i in cookies_fb.split(";") if i != "" and i != "\n"]
for ck in cookie_fb:
    name, value = ck.split("=",1)
    driver.add_cookie({"name":name, "value":value})

driver.refresh()
sleep(5)
# input()
them_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Add Photos"]'))).click()
gui_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="file1"]')))
gui_anh.send_keys('D:/Code_test/Fix_code/ai/img1.jpg')
gui_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="file2"]')))
gui_anh.send_keys('D:/Code_test/Fix_code/ai/img2.jpg')
gui = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Send"]'))).click()



    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
