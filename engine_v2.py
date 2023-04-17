from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os




id_fb = 100018590648536

def engine_gui_anh(driver):
    them_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Add Photos"]'))).click()
    gui_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="file1"]')))
    gui_anh.send_keys(f'{os.getcwd()}/img1.jpg')
    gui_anh = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="file2"]')))
    gui_anh.send_keys(f'{os.getcwd()}/img2.jpg')
    gui = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Send"]'))).click()



    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    # none = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
