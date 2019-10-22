from selenium import webdriver
from instagram.pages.login_page import LoginPage

driver = webdriver.Chrome("D:\Downloads\Python\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/accounts/login/")

login_page = LoginPage(driver)
login_page.enter_user_name("pyautomation")
login_page.enter_password("Ab123456!")
login_page.login()