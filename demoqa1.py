
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
expected_page_title = "ToolsQA"
assert driver.title == expected_page_title
submited_name = "Tom Brown"
submited_email ="brown@tttmail.com"
submited_current_adderss = "Madrid"
submited_permanent_adderss = "London"
driver.find_element_by_id("userName").send_keys(submited_name)
driver.find_element_by_id("userEmail").send_keys(submited_email)
driver.find_element_by_id("currentAddress").send_keys(submited_current_adderss)
driver.find_element_by_id("permanentAddress").send_keys(submited_permanent_adderss)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_id("submit").click()
actual_name = driver.find_element_by_id("name").text
actual_email = driver.find_element_by_id("email").text
actual_current_address = driver.find_element_by_id("currentAddress").text
actual_permanent_address = driver.find_element_by_id("permanentAddress").text
assert submited_name == actual_name
assert submited_email == actual_email
assert submited_current_adderss == actual_current_address
assert submited_permanent_adderss == actual_current_address
driver.close()
driver.quit()
