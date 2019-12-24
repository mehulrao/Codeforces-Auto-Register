from selenium import webdriver
from selenium.webdriver.common.keys import Keys

handle = input("Enter your desired handle: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

driver = webdriver.Firefox()
driver.get("https://codeforces.com/register")
element = driver.find_element_by_name("handle")
element.send_keys(handle)
element = driver.find_element_by_name("email")
element.send_keys(email)
element = driver.find_element_by_name("password")
element.send_keys(password)
element = driver.find_element_by_name("passwordConfirmation")
element.send_keys(password)
element.send_keys(Keys.RETURN)