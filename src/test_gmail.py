import time

from selenium import webdriver

driver = webdriver.Chrome("D:\Downloads\Python\chromedriver.exe")
driver.get("https://accounts.google.com/")

driver.implicitly_wait(10)
create_account_button = driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
create_account_button.click()
time.sleep(1)
for_myself_button = driver.find_element_by_xpath("//*[@id='initialView']/div[2]/div[3]/div/div/span[1]/div[2]/div")
for_myself_button.click()

validator_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."
first_name_field = driver.find_element_by_id("firstName")
last_name_field = driver.find_element_by_id("lastName")
password_field = driver.find_element_by_name("Passwd")
confirm_password_field = driver.find_element_by_name("ConfirmPasswd")
next_button = driver.find_element_by_id("accountDetailsNext")
user_name_field = driver.find_element_by_id("username")

first_name_field.send_keys("Pavel")
last_name_field.send_keys("Nikolin")
password_field.send_keys("Pasword1")
confirm_password_field.send_keys("Pasword1")

email_list = ['@p.p', 'p@-p.p', 'p@p', 'p@p@p.p']

user_name_field.clear()
user_name_field.send_keys(email_list[0])
next_button.click()
time.sleep(1)
assert validator_error in driver.page_source


user_name_field.clear()
user_name_field.send_keys(email_list[1])
next_button.click()
time.sleep(1)
assert validator_error in driver.page_source


user_name_field.clear()
user_name_field.send_keys(email_list[2])
next_button.click()
time.sleep(1)
assert validator_error in driver.page_source

user_name_field.clear()
user_name_field.send_keys(email_list[3])
next_button.click()
time.sleep(1)
assert validator_error in driver.page_source

driver.quit()