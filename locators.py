from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')

# find by ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# find by XPath
driver.find_element(By.XPATH, '//input[@aria-label="Search Amazon"]')
driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon"]')
driver.find_element(By.XPATH, '//input[@name="field-keywords"]')

# XPath, many attr
driver.find_element(By.XPATH, '//input[@tabindex="0" and @role="searchbox"]')
driver.find_element(By.XPATH, '//input[@role="searchbox" and @tabindex="0" and....]')

# XPath, text()
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# Any tag, just *
driver.find_element(By.XPATH, '//*[@aria-label="Search Amazon"]')

# Xpath, parent => child node
driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")
# Contains:
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and contains(@href, 'nav_cs_bestsellers')]")


#Homework2- Practice with locators
# Amazon logo
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
# Email field
driver.find_element(By.ID,"//input[@id='ap_email']")
#Continue button
driver.find_element(By.ID,"//input[@id='continue']")
# Conditions of use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use' and contains(@href, 'ap_signin_notification_condition_of_use?ie')]")
# Privacy Notice link
driver.find_element(By.XPATH,"//a[text()='Privacy Notice' and contains(@href, 'ap_signin_notification_privacy_notice?ie')]")
# Need help link
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
# Forgot your password link
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")
# Other issues with Sign-In link
driver.find_element(By.ID, "//a[@id='ap-other-signin-issues-link']")
# Create your Amazon account button
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")


#Homework3 - Find the most optimal locators for StackOverflow Create Account page elements
# Create Account - 2 class
driver.find_element(By.CSS_SELECTOR,'.flex--item.fs-headline1')
# By Clicking signup - 2 class
driver.find_element(By.CSS_SELECTOR,'.flex--item.js-terms')
# Email - ID
driver.find_element(By.CSS_SELECTOR, '#email')
# Password - ID
driver.find_element(By.CSS_SELECTOR, '#password')
#Hidden password symbol - tag+class
driver.find_element(By.CSS_SELECTOR,'svg.ps-absolute.js-show-password')
# signup-button - using ID
driver.find_element(By.CSS_SELECTOR, '#submit-button')
# signup with google - tag + 2 class + attributes
driver.find_element(By.CSS_SELECTOR,'button.flex--item.s-btn__google[data-provider="google"]')
# signup with github - tag + 2 class + attributes
driver.find_element(By.CSS_SELECTOR,'button.flex--item.s-btn__github[data-provider="github"]')
# get stackoverflow link - Partial attributes
driver.find_element(By.CSS_SELECTOR, "[href*='https://stackoverflow.com/teams?']")
