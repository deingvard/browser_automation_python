from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(executable_path='/Users/admin/Downloads/chromedriver')
browser.get("https://techstepacademy.com/training-ground")

print("I have arrived")
button_xpath_locator = '//button[@id="b1"]'
butn4_elem = browser.find_element_by_xpath(button_xpath_locator)
butn4_elem.click()
WebDriverWait(browser, 5).until(alert_is_present())
print("An alert appeared")

sel = browser.find_element_by_id('sel1')
my_select = Select(sel)
my_select.select_by_index(0)

# browser.quit()