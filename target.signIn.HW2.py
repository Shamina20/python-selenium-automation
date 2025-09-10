from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')


# Click Account button tab using find element
driver.find_element(By.XPATH, "//a[@id='account-sign-in']//span[text()='Account']").click()
sleep(2)
# Click  Signin button using find element
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
sleep(5)
# Verify
driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']")
driver.find_element(By.XPATH, "//button[text()='Sign in with passkey' and contains(@class,'T5sAi styles_filleddefault__7QnWt')]")
print("Test Passed")