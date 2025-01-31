import datetime
from time import sleep

import selenium
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

def ClickNext():
    NextButton = driver.find_element(By.ID, "NextButton")
    NextButton.click()
    sleep(4)

def DoSurvey(numberPassed, commentPassed):
    driver.get('https://sonicdrivein.com/feedback')
    sleep(10)
    ClickNext()
    StoreIDText = driver.find_element(By.ID, "QR~QID19")
    StoreIDText.send_keys("2514")
    ClickNext()
    CorrectButton = driver.find_element(By.ID, "QID24-1-label")
    CorrectButton.click()
    ClickNext()
    OrderIDText = driver.find_element(By.ID, "QR~QID20")
    OrderIDText.send_keys(numberPassed)                                             #TODO Change numbers
    ClickNext()
    OrderIDText = driver.find_element(By.ID, "QR~QID26")
    OrderIDText.send_keys(str(datetime.date.today()))                                             #TODO Change to current date
    ClickNext()
    SatButton = driver.find_element(By.ID,"QID3-5-label")
    SatButton.click()
    sleep(3)
    ClickNext()
    CommentText = driver.find_element(By.ID, "QR~QID6")
    CommentText.send_keys(commentPassed)
    sleep(1)
    ClickNext()
    SatButton = driver.find_element(By.CSS_SELECTOR,"tr.ChoiceRow:nth-child(1) > td:nth-child(6)")
    SatButton.click()
    sleep(1)
    SatButton = driver.find_element(By.CSS_SELECTOR,"tr.ChoiceRow:nth-child(2) > td:nth-child(6)")
    SatButton.click()
    sleep(1)
    SatButton = driver.find_element(By.CSS_SELECTOR,"tr.ChoiceRow:nth-child(3) > td:nth-child(6)")
    SatButton.click()
    sleep(1)
    SatButton = driver.find_element(By.CSS_SELECTOR,"tr.ChoiceRow:nth-child(4) > td:nth-child(6)")
    SatButton.click()
    sleep(1)
    SatButton = driver.find_element(By.CSS_SELECTOR,"tr.ChoiceRow:nth-child(5) > td:nth-child(6)")
    SatButton.click()
    sleep(1)
    ClickNext()
    SatButton = driver.find_element(By.ID,"QID15-4-label")
    SatButton.click()
    sleep(3)
    SatButton = driver.find_element(By.ID,"QID9-1-label")
    SatButton.click()
    sleep(3)
    ClickNext()
    SatButton = driver.find_element(By.ID,"QID10-7-label")
    SatButton.click()
    sleep(3)
    ClickNext()
    SatButton = driver.find_element(By.CSS_SELECTOR,"tr.ChoiceRow:nth-child(1) > td:nth-child(6)")
    SatButton.click()
    sleep(1)
    SatButton = driver.find_element(By.CSS_SELECTOR,"tr.ChoiceRow:nth-child(2) > td:nth-child(6)")
    SatButton.click()
    sleep(1)
    ClickNext()
    SatButton = driver.find_element(By.ID,"QID11-5-label")
    SatButton.click()
    sleep(1)
    ClickNext()
    sleep(2)



