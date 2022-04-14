# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 01:32:56 2022

@author: Kyle
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def OpenLogin():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://app.apollo.io/#/login")
    return driver
    
def EnterLogin(driver):
    EmailLogin = WebDriverWaitClick(By.ID, "o2-input", driver,'Username')
    actions = ActionChains(driver)
    actions.send_keys("")
    actions.send_keys(Keys.TAB)
    actions.send_keys("")
    actions.send_keys(Keys.ENTER)
    actions.perform()

def NavigateToSearchPage(driver):
    searcher = WebDriverWaitClick(By.ID, "searcher", driver,'Search')
    AreYouDone = input("Press Enter to Move on: ")

def MainLoop(driver):
    TopLeftCorner = WebDriverWaitClick(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/i", driver, 'TopLeftCorner', 1)
    SelectThisPage = WebDriverWaitClick(By.XPATH, "/html/body/div[4]/div/div/div/a[1]", driver, 'SelectThisPage')
    Lists = WebDriverWaitClick(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/span[4]/div", driver, 'List')
    AddToLists = WebDriverWaitClick(By.XPATH, "/html/body/div[4]/div/div/div/a", driver, 'AddToLists')
    EnterOrCreateLists = WebDriverWaitClick(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/span/i", driver, 'ClickingDropDownList')
    
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    
    Confirm = WebDriverWaitClick(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[3]/div[1]/div", driver, 'Confirm')
    Refresh = WebDriverWaitClick(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]", driver, 'Refresh', 1)
    
def WebDriverWaitClick(BY, linkAddress, driver, errorCode, sleeping = 0, failCount = 0): 
    try:
        element = WebDriverWait(driver,0).until(
        EC.element_to_be_clickable((BY, linkAddress)))
        time.sleep(sleeping)
        element.click()
        return element
    
    except:
        print("Failed at", errorCode)
        failCount += 1
        print(failCount)
        if failCount < 3:
            WebDriverWaitClick(BY, linkAddress, driver, errorCode, sleeping, failCount)
        else:
            pass

def main():
    driver = OpenLogin()
    time.sleep(2)
    EnterLogin(driver)
    time.sleep(2)
    NavigateToSearchPage(driver)
    loops = input("How Many Entries Do You want to add to list?: ")
    loops = int(loops) // 25
    loop = 0
    while loop < loops:
        MainLoop(driver)
        loop += 1
        
if __name__ == "__main__":
    main()
        