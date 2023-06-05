import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

PATH = "/Users/wevilaguo/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://google.com")
print(driver.title)
search = driver.find_element(by=By.NAME, value="query")
search.clear()
search.send_keys("男孩")
search.send_keys(Keys.RETURN)
# WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "sc-6ee89537-2"))
# )
time.sleep(20)
titles = driver.find_elements(by=By.CLASS_NAME, value="sc-b205d8ae-3")
for title in titles:
    print(title.text)


# link=driver.find_element_by_link_text("什麼?這個約兒是男生!!!??").click()
driver.find_element(by=By.LINK_TEXT,value="什麼?這個約兒是男生!!!??").click()
driver.back()
driver.back()
driver.forward()
driver.forward()

# driver.quit()
