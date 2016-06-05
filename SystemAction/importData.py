#coding: utf-8
from selenium import webdriver
import time
class Importer:
    driver = webdriver.Firefox()
    url = "http://127.0.0.1:8000/accounts/login/?next=/"
    username = "chaos"
    password = "xlsd1996"
    def login(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id("id_username").send_keys(self.username)
        self.driver.find_element_by_id("id_password").send_keys(self.password)
        self.driver.find_element_by_id("id_login").click()

    def choosePage(self,url):
        self.driver.get(url)

    def importUserData(self,fileName):
        import os
        import csv
        filepath = os.getcwd()+"/../static/other/"

        userData = list()

        with open(filepath+fileName,mode='r') as f:
            lines = f.readlines()
            for i  in lines:
                data = i.decode('utf-8').split(',')
                #print i.decode('utf-8').split(',')
                userData.append([data[1],data[2],data[3],data[8]])

        for person in userData[1:]:
            print person[1].encode('utf-8')
            one.choosePage("http://127.0.0.1:8000/accounts/user/add/")
            self.CreateUser(person=person)
            time.sleep(0.8)

    def CreateUser(self,person):
        self.driver.find_element_by_id("id_username").send_keys(person[0])
        self.driver.find_element_by_id("id_password").send_keys(person[0][-6:])
        if("@" in str(person[3])):
            self.driver.find_element_by_id("id_email").send_keys(person[3])
        else:
            self.driver.find_element_by_id("id_email").send_keys(str(person[3])+"@qq.com")
        self.driver.find_element_by_id("id_nickname").send_keys(person[1])

        if(person[2]==u"男"):
            self.driver.find_element_by_id("id_sex_0").click()
        else:
            self.driver.find_element_by_id("id_sex_1").click()

        options = self.driver.find_element_by_id("id_is_active").find_elements_by_tag_name("option")
        options[0].click()

        self.driver.find_element_by_id("id_submit").click()





if(__name__=="__main__"):
    one = Importer()
    one.login()
    one.choosePage("http://127.0.0.1:8000/accounts/user/add/")
    one.importUserData("2014-wulian.csv")




