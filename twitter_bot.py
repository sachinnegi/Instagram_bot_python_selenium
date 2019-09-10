from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep,strftime
from random import randint
class instagram:
    def __init__(self,username,password):
        driver_location="D:/Selenium/twitter_bot/env/Scripts/chromedriver.exe"
        self.browser=webdriver.Chrome(driver_location)
        self.username=username
        self.password=password
    def login(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        user=self.browser.find_element_by_name("username")
        user.send_keys(self.username)
        password=self.browser.find_element_by_name("password")
        password.send_keys(self.password)
        sign_in=self.browser.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div")
        sign_in.click()
        sleep(3)
        #turn off the turn-on notification now 
        notification=self.browser.find_element_by_class_name("aOOlW").click()
    def search(self,tag):
        self.browser.get("https://www.instagram.com/explore/tags/dogs/")    
        sleep(3)
        first_thumbnail=self.browser.find_element_by_css_selector("#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0")
        first_thumbnail.click()
        sleep(1)
        follow_button=self.browser.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button")
        sleep(1)
        like_button=self.browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span")
        time.sleep(1)
        self.browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[2]/button/span").click()
        comment_box=self.browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea")
        if follow_button.text=="Follow":
            follow_button.click()
            like_button.click()
            comment_box.send_keys("Beautiful")
            comment_box.send_keys(Keys.RETURN) 
            # .send_keys(Keys=RETURN)

        #else:
            
        #search_box=self.browser.find_element_by_class_name("XTCLo")
        #search_box.send_keys(tag)
        #search_box.send_keys(Keys.RETURN)
        sleep(3)

phone='9411132651'
password='9756813724'
bot=instagram(phone,password)
bot.login()
bot.search("sexy")



#import pandas as pd


#password=browser.find_element_by_css_selector('form input')[1]
#password.send_keys("9756813724")
#sign_in=browser.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4)")
#sign_in.click()