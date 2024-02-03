from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from conftest import BaseURL
from hrmhelpers.Selenium_helper import Selenium_Helper

class AdminPage(Selenium_Helper):

    email_ele = (By.XPATH,"//input[@name='username']")
    password_ele = (By.XPATH,"//input[@name='password']")
    login_ele = (By.XPATH,"//button")
    forgotpassword_ele=(By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    resetusername_ele=(By.XPATH,"//*[@id='app']/div[1]/div[1]/div/form/div[1]/div/div[2]/input")
    reset_ele=(By.XPATH,"//button[@type='submit']")
    admin_ele=(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")


    def __init__(self,driver):
        super().__init__(driver)


    #doing a valid login
    def login(self,username):
        self.webelement_enter(self.email_ele,username)
        sleep(2)
        self.webelement_click(self.forgotpassword_ele)
        sleep(2)
        self.webelement_enter(self.resetusername_ele,username)
        sleep(2)
        self.webelement_click(self.reset_ele)
        sleep(4)
        if (self.driver.find_element(by=By.XPATH,value="//*[@id='app']/div[1]/div[1]/div/h6")):
            self.driver.get(BaseURL)
            sleep(4)
        else:
            self.driver.get(BaseURL)
            sleep(2)

    def Logocheck(self,username ,password):

        self.webelement_enter(self.email_ele, username)
        self.webelement_enter(self.password_ele, password)
        sleep(2)
        self.webelement_click(self.login_ele)
        sleep(2)
        if (self.driver.find_element(by=By.XPATH,value="//img[@alt='client brand banner']")):
            print("OrangeHRM logo is displayed")
        self.webelement_click(self.admin_ele)
        sleep(2)

    def Headercheck(self):

        items = self.driver.find_elements(by=By.XPATH, value="//li[@data-v-5327b38a]")
        i = 1
        for item in items:
            if (self.driver.find_element(by=By.XPATH, value="//li[@data-v-5327b38a][" + str(i) + "]")).is_displayed():
                self.driver.find_element(by=By.XPATH, value="//li[@data-v-5327b38a][" + str(i) + "]").click()
                sleep(2)
                print("Header" + str(i) +" is displayed")
            i += 1


    def Mainmenucheck(self):

        items = self.driver.find_elements(by=By.XPATH, value="//li[@data-v-636d6b87]")
        i = 0
        for item in items:
            i += 1
            if (self.driver.find_element(by=By.XPATH, value="//li[@data-v-636d6b87][" + str(i) + "]")).is_displayed():
                self.driver.find_element(by=By.XPATH, value="//li[@data-v-636d6b87][" + str(i) + "]").click()
                sleep(1)
                if i == 10:
                    self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div[1]/div[1]/form/div[4]/button[1]").click()
                    sleep(2)
            print("Main menu " + str(i) + " is displayed")









