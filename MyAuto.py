from selenium import webdriver
from selenium.webdriver.common.by import By

path = '/Users/ana7ta7iya/PycharmProjects/Myheart/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(5)

keyword = 'ball'

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(keyword)

driver.find_element(By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input').click()


driver.quit



# //*[@id="nav-search-submit-text"]/input