import time


class SignInPage():

    def __init__(self, driver):
        self.driver = driver

    def click_create_account_button(self):
        create_account_button = self.driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
        create_account_button.click()
        time.sleep(1)

    def click_myself_button(self):
        for_myself_button = self.driver.find_element_by_xpath(
            "//*[@id='initialView']/div[2]/div[3]/div/div/span[1]/div[2]/div")
        for_myself_button.click()
