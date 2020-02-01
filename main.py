from selenium import webdriver
from time import sleep
from time import time
from datetime import datetime
import os

from get_time import get_hour


class Pysta:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://www.instagram.com/"

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

        self.driver.get(self.base_url + "accounts/login/")
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
        sleep(3)
        # Close the notification prompt on login
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

    def automate(self):
        now = int(datetime.now().strftime("%H"))
        while True:
            returned = get_hour(now)
            sleep(10)
            if returned == 0:
                print("Hour is even")
                self.auto_like()
            else:
                print("Hour is odd")
                self.follow_requests()
        return False

    """ def get_time(self):
        now = int(datetime.now().strftime("%H"))

        current = 0
        while True:
            sleep(5)
            if now != current:
                current = now
                if now % 2 == 0:
                    self.auto_like()
                    # self.follow_requests()
                else:
                    self.auto_like()
            return False """

    def follow_requests(self):
        self.driver.find_element_by_xpath(
            '//a[contains(@href,"/accounts/activity")]').click()
        sleep(3)
        self.driver.find_element_by_class_name(
            'coreSpriteNotificationRightChevron').click()

    def auto_like(self):
        print("auto_like has started")
        window_dims = self.driver.get_window_size()
        scroll = window_dims.get("height", 1)
        post_url = []

        n = 1
        scroll_amount = 2
        for i in range(0, scroll_amount):
            print("Scrolling Started")
            sleep(5)

            self.driver.find_element_by_class_name(
                "wpO6b ").click()

            sleep(2)
            self.driver.find_element_by_xpath(
                "//button[contains(text(), 'Go to post')]").click()
            sleep(2)
            post_url = self.driver.current_url, i
            sleep(1)
            self.driver.get(self.base_url)
            sleep(3)
            self.driver.execute_script(f"window.scrollTo(0, {scroll * n})")
            sleep(2)
            n += 1
            print("Test")
            # self.driver.execute_script(f"window.scrollTo(0, {scroll})")

        print(post_url)

        # self.driver.get(self.base_url + "explore/")

    """def modtest(self):
        for i in range(1, 24):
            # print(i, i % 2)
            if i % 2 == 0:
                print("Even hour", i)
            else:
             print("Odd hour", i)
    """


if __name__ == "__main__":

    my_bot = Pysta()
    my_bot.readFile()
    my_bot.automate()

    # my_bot.auto_main()
    # my_bot.modtest()
