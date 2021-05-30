from chromdriver import drivers
import time


class webNevigation:

    def nevigateToinstagram():
        """Connecting to whatsapp web through chrome Driver"""
        try:
            drivers.driver.get('https://www.instagram.com/')
            time.sleep(5)
            search_box=drivers.driver.find_element_by_class_name('TqC_a')
        except:
            MY_USERNAME = input("Enter username: \n")
            MY_PASSWORD = input("Enter password: \n")
            time.sleep(5)
            print("Bot is active, enter the credentials")
            drivers.driver.get('https://www.instagram.com/')
            username = drivers.driver.find_element_by_name("username")
            username.send_keys(MY_USERNAME)
            password = drivers.driver.find_element_by_name("password")
            password.send_keys(MY_PASSWORD)
            password.send_keys("\n")
