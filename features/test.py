import time

from selenium import webdriver

from features.pages.login_page import LoginPage
from features.pages.main_page import MainPage
from features.pages.search_page import SearchResultPage

driver = webdriver.Chrome("D:\Downloads\Python\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.instagram.com/accounts/login/")

login_page = LoginPage(driver)
login_page.enter_user_name("Pasha_871s")
login_page.enter_password("123456!")
login_page.login()

main_page = MainPage(driver)
main_page.click_not_now_button()
main_page.type_in_the_search_field("#fitness")
main_page.click_result_with_test("#fitness")

search_page = SearchResultPage(driver)
time.sleep(5)
assert "Подписаться" in search_page.get_follow_button_text()

driver.quit()
