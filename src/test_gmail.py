import time

from selenium import webdriver
from src.pages.sign_in_page import SignInPage
from src.pages.create_account_page import CreateAccount

driver = webdriver.Chrome("D:\Downloads\Python\chromedriver.exe")
driver.get("https://accounts.google.com/")
validator_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."

user_dictionary = {'fn': 'Pavel', 'ln': 'Nikolin', 'password': 'Pasword1'}
email_list = ['@p.p', 'p@-p.p', 'p@p', 'p@p@p.p']

driver.implicitly_wait(5)

sign_in_page = SignInPage(driver)
sign_in_page.click_create_account_button()
sign_in_page.click_myself_button()

create_account_page = CreateAccount(driver)
create_account_page.enter_first_name(user_dictionary['fn'])
create_account_page.enter_last_name(user_dictionary['ln'])
create_account_page.enter_password(user_dictionary['password'])
create_account_page.enter_confirm_password(user_dictionary['password'])


def validator_username_field(email):
    create_account_page.enter_username(email)
    create_account_page.click_next_button()
    time.sleep(1)
    assert validator_error in driver.page_source


for email in email_list:
    validator_username_field(email)
driver.quit()
