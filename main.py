from selenium import webdriver
from time import sleep
import os


class PyPost:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        print("Bot ready")

        # self.follow_requests()

    def readFile(self):

        if os.path.isfile("creds.txt"):

            to_store = []

            creds = {0, 1}
            for i, row in enumerate(open("creds.txt")):
                if i in creds:
                    to_store.append(row)
                    # print(to_store[i].strip("\n"))
            user = to_store[0]
            pw = to_store[1]

        else:
            login_info = open("creds.txt", "w+")
            user = input("Username >")
            login_info.write(user + "\n")
            self.username = user
            pw = input("Password >")
            login_info.write(pw)

        self.login(user, pw)

    def login(self, username, pw):

        self.username = username
        self.pw = pw

        self.driver.get("https://www.instagram.com/accounts/login/")
        # Locates the username field and inputs the provided username
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(self.username)
        # Locates the password field and inputs the provided password('pw')
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(self.pw)
        sleep(2)
        # Locates the "log in" button and clicks it
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        # Close the notification prompt on login
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

        self.follow_requests()

    def follow_requests(self):
        self.driver.find_element_by_xpath(
            '//a[contains(@href,"/accounts/activity")]').click()
        sleep(3)
        self.driver.find_element_by_class_name(
            'coreSpriteNotificationRightChevron').click()


my_bot = PyPost()
my_bot.readFile()
