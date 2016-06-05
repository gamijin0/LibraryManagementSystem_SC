#coding: utf-8
from selenium import webdriver
import time
class Importer:
    driver = webdriver.Firefox()
    url = ""
    username = "chaos"
    password = "xlsd1996"

    def __init__(self,url):
        self.url = url


    def login(self):
        self.driver.get(self.url+"/accounts/login/?next=/")
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
                userData.append([data[1],data[2],data[3],data[9]])

        for person in userData[1:]:
            print person[1].encode('utf-8')
            one.choosePage(self.url+"/accounts/user/add/")
            self.CreateUser(person=person)
            time.sleep(0.3)

        print "用户数据导入完成"

    def CreateUser(self,person):
        self.driver.find_element_by_id("id_username").send_keys(person[0])
        self.driver.find_element_by_id("id_password").send_keys(person[0][-6:])
        if("@" in str(person[3])):
            self.driver.find_element_by_id("id_email").send_keys(person[3])
        else:
            self.driver.find_element_by_id("id_email").send_keys(str(person[3]).strip()+"@qq.com")
        self.driver.find_element_by_id("id_nickname").send_keys(person[1])

        if(person[2]==u"男"):
            self.driver.find_element_by_id("id_sex_0").click()
        else:
            self.driver.find_element_by_id("id_sex_1").click()

        options = self.driver.find_element_by_id("id_is_active").find_elements_by_tag_name("option")
        options[0].click()

        self.driver.find_element_by_id("id_submit").click()

    def importBookData(self,fileName):
        import os
        import csv
        filepath = os.getcwd() + "/../static/other/"

        Data = list()

        with open(filepath + fileName, mode='r') as f:
            lines = f.readlines()
            for i in lines:
                data = i.decode('utf-8').split(',')
                Data.append(data)

        # for person in userData[1:]:
        #     print person[1].encode('utf-8')
        #     one.choosePage(self.url + "/accounts/user/add/")
        #     self.CreateUser(person=person)
        #     time.sleep(0.3)
        for book in Data[7:]:
            time.sleep(1)
            self.choosePage(self.url+"/system/save/")
            self.SaveBook(book=book)



        print "图书数据导入完成"

    def SaveBook(self,book):
        import random
        self.driver.find_element_by_id("id_book_myid").send_keys(book[0])
        self.driver.find_element_by_id("id_book_name").send_keys(book[1])
        self.driver.find_element_by_id("id_author").send_keys(book[2])
        self.driver.find_element_by_id("id_press").send_keys(book[3])
        self.driver.find_element_by_id("id_publication_year").send_keys(book[4])
        self.driver.find_element_by_id("id_category_id").send_keys(u"普通")
        self.driver.find_element_by_id("id_inventory").send_keys(random.randint(5,12))

        self.driver.find_element_by_id("id_submit").click()


if(__name__=="__main__"):
    one = Importer("http://127.0.0.1:8000")
    one.login()
    one.importBookData("books_data.csv")




