from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
driver.close()

# from selenium import webdriver

# driver = webdriver.Firefox()

# driver.get("https://www.google.com/")
# driver.maximize_window()
# print(driver.title)
# driver.close()
