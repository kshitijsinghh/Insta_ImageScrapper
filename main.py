from datetime import time
import time
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from webnavigate import webNevigation
from chromdriver import drivers
#chrome_options = Options()
#chrome_options.add_argument("user-data-dir=selenium")
#chrome_options.add_argument("user-data-dir=C:\\Users\\Leaf\\Desktop\\Random\\selenium")
#chrome_options.add_argument('--profile-directory=Default')
#chrome_options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')
#driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
tz = pytz.timezone("Asia/Kolkata")

webNevigation.nevigateToinstagram()


Target_Account= input("Enter the Target Account: \n")
time.sleep(10)

drivers.driver.get(f"https://www.instagram.com/{Target_Account}/")
time.sleep(10)
for l in range(3):
    drivers.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)
time.sleep(40)
drivers.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

i=drivers.driver.find_element_by_class_name("_2z6nI")
time.sleep(20)
#driver.execute_script("arguments[0].scrollIntoView();",i)

drivers.driver.execute_script("arguments[0].scrollIntoView();",i)
time.sleep(10)

#scr1 = driver.find_element_by_xpath("//*[@id='react-root']") #//*[@id="react-root"]/section
        

    
#pi=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div/div/div[10]/div[2]/a/div")
#driver.execute_script("arguments[0].scrollIntoView();",pi)

j=i.find_elements_by_class_name("eLAPa")
k=1
for r in j:
    drivers.drivers.execute_script("arguments[0].scrollIntoView();",r)
    time.sleep(10)
    r.find_element_by_class_name("IDFI-BUTTON").click()
    print(str(k)+" Image Downloaded")
    k=k+1
drivers.driver.close()
    
