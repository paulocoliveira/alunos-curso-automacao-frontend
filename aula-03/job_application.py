from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")

sleep(3)

full_name = driver.find_element(By.ID, "fullName")
full_name.send_keys("Paulo Oliveira")

email = driver.find_element(By.ID, "email")
email.send_keys("paulocol@gmail.com")

phone_number = driver.find_element(By.ID, "phoneNumber")
phone_number.send_keys("123456789")

Select(driver.find_element(By.ID, "desiredPosition")).select_by_visible_text("Manager")

remote = driver.find_element(By.ID, "location1")
remote.click()

years = driver.find_element(By.ID, "experienceYears")
years.send_keys("17")

html = driver.find_element(By.ID, "skill1")
html.click()

js = driver.find_element(By.ID, "skill3")
js.click()

button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()

message = driver.find_element(By.ID, "successMessage").text

sleep(1)

assert "Submission successful!" == message

sleep(5)

driver.quit()