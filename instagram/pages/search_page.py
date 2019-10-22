from selenium.webdriver.common.by import By

from instagram.pages.base_page import BasePage


class SearchResultPage(BasePage):
    BUTTON_FOLLOW = (By.XPATH, "//button[@type='button']")

    def get_follow_button_text(self):
        return self.get_element(self.BUTTON_FOLLOW).text

    def _verify_page(self):
        self.on_this_page(self.BUTTON_FOLLOW)
