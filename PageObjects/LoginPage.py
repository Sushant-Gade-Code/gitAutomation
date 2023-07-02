from selenium.webdriver.common.by import By

from selenium import webdriver

class LogInPage:
    link_Sign_XPATH=(By.XPATH,"//a[@href='/login']")
    text_Username_XPATH=(By.XPATH,"//input[@name='login']")
    text_Password_ID =(By.ID,"password")
    btn_SignIn_Name=(By.NAME,"commit")
    btn_Menu_XPATH=(By.XPATH,'//div[@class="AppHeader-user"]//span/span/img')
    btn_SignOut_XPATH=(By.XPATH,'//a[@href="/logout"]/span')
    btn_con_signOut_XPATH=(By.XPATH,'//form[@action="/logout"]/input[2]')
    def __init__(self,driver):
        self.driver=driver

    def getSignLink(self):
        self.driver.find_element(*LogInPage.link_Sign_XPATH).click()

    def getUsername(self,Username):
        self.driver.find_element(*LogInPage.text_Username_XPATH).clear()
        self.driver.find_element(*LogInPage.text_Username_XPATH).send_keys(Username)

    def getPassword(self,Password):
        self.driver.find_element(*LogInPage.text_Password_ID).clear()
        self.driver.find_element(*LogInPage.text_Password_ID).send_keys(Password)

    def getSignbtn(self):
        self.driver.find_element(*LogInPage.btn_SignIn_Name).click()

    def getMenuButton(self):
        self.driver.find_element(*LogInPage.btn_Menu_XPATH).click()

    def getSingOutbtn(self):
        self.driver.find_element(*LogInPage.btn_SignOut_XPATH).click()

    def getConSignOut(self):
        self.driver.find_element(*LogInPage.btn_con_signOut_XPATH).click()


