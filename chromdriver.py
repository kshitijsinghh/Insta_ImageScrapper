import pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class drivers(object):
    """Saving the last session and connecting the chrome driver for web connection"""
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=selenium")
    chrome_options.add_argument("user-data-dir=C:\\Users\\Leaf\\Desktop\\Instagram\\instagramdm_saarthi_Jos\\selenium")
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    tz = pytz.timezone("Asia/Kolkata")
