class CreateAccount():

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first):
        first_name_field = self.driver.find_element_by_id("firstName")
        first_name_field.send_keys(first)

    def enter_last_name(self, last):
        last_name_field = self.driver.find_element_by_id("lastName")
        last_name_field.send_keys(last)

    def enter_password(self, password):
        password_field = self.driver.find_element_by_name("Passwd")
        password_field.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")
        confirm_password_field.send_keys(confirm_password)

    def enter_username(self, username):
        user_name_field = self.driver.find_element_by_id("username")
        user_name_field.clear()
        user_name_field.send_keys(username)

    def click_next_button(self):
        next_button = self.driver.find_element_by_id("accountDetailsNext")
        next_button.click()
