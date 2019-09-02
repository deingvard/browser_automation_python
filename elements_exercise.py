
from selenium import webdriver

browser = webdriver.Chrome(executable_path='/Users/admin/Downloads/chromedriver')

browser.get("https://techstepacademy.com/training-ground")

input2_css_locator = "input[name='Input 1']"
button_xpath_locator = '//button[@id="b1"]'

# Assign elements
input2_element = browser.find_element_by_css_selector(input2_css_locator)
butn4_elem = browser.find_element_by_xpath(button_xpath_locator)

# Manipulate elements
input2_element.send_keys("Test text")
butn4_elem.click()
browser.quit()
