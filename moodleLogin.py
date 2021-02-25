from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


username=input('Enter Username: ')
pwd=input('Enter Password: ')

PATH = '..\chromedriver.exe'
driver=webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
text = driver.find_element_by_id("login").text
l=text.split(' ')
num=[int(i) for i in l if i.isnumeric()]
ans=0
if 'add' in l:
    ans=sum(num)
elif 'subtract' in l:
    ans=num[0]-num[1]
elif 'first' in l:
    ans=num[0]
elif 'second' in l:
    ans=num[1]
else:
    pass
ans=str(ans)
uname = driver.find_element_by_id('username')
uname.clear()
uname.send_keys(username)

p = driver.find_element_by_id('password')
p.clear()
p.send_keys(pwd)

captcha = driver.find_element_by_id('valuepkg3')
captcha.clear()
captcha.send_keys(ans)
captcha.send_keys(Keys.RETURN)

# time.sleep(5)
# driver.quit()
