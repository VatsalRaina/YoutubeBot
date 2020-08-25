import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/?gl=GB&hl=en-GB")

time.sleep(5)

for i in range(3):

    searchField = driver.find_element_by_name("search_query")
    searchField.clear()
    searchField.send_keys("cambridge table tennis")
    searchField.send_keys(Keys.RETURN)

    time.sleep(5)

    vidLink = driver.find_element_by_link_text("77th Table Tennis Varsity (Oxford vs Cambridge)")
    vidLink.click()

    time.sleep(60)

driver.close()