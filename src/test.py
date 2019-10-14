from selenium import webdriver

driver = webdriver.Chrome("d:/Pyton-test/chromedriver.exe")
driver.get("https://wikipedia.org")

search_field = driver.find_element_by_id("searchInput")
search_button = driver.find_element_by_xpath("//form[@id = 'search-form']/fieldset/button")

search_field.send_keys("Test Automation")
search_button.click()

assert "Test Automation" in driver.title
driver.quit()


