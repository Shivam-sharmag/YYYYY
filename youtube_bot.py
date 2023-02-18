from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time 
driver = webdriver.Chrome()
while True:
    driver.get("https://www.youtube.com/watch?v=vAa951sMoFg")
    time.sleep(5)

