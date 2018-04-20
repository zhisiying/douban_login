from main import yzm
import requests
import time
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.douban.com/accounts/login'
driver.get(url)
print('请输入你的账号:')
Account = input()
print('请输入你的密码:')
password = input()
driver.find_element_by_xpath('//*[@id="email"]').send_keys(Account)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
yzms = driver.find_element_by_xpath('//img[@id="captcha_image"]').get_attribute('src')
# value = driver.find_element_by_xpath('//input[@name="captcha-id"]').get_attribute('value')
tu = requests.get(yzms).content
f = open('image.jpg', 'wb')
f.write(tu)
f.close()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="captcha_field"]').send_keys(yzm()[0].lower())
time.sleep(5)
driver.find_element_by_xpath('//input[@name="login"]').click()
f = open('./douban.html', 'w', encoding='utf8')
f.write(driver.page_source)
f.close()
