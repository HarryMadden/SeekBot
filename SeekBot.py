from selenium import webdriver
import time
import xlwings
import unittest
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

while True:
    #open page
    webpage = 'ENTER PERSONALISED SEEK SEARCH URL HERE'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(webpage)
    webpage = driver.page_source
    #driver.close()

    #sign in
    driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div[1]/span[2]/div[1]/div[2]/nav/a[1]').click()
    time.sleep(0.1)

    #type email
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('ENTER LOG IN EMAIL HERE')

    #type password
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('ENTER PASSWORD HERE')

    #click sign in
    driver.find_element_by_xpath('//*[@id="app"]/div/main/div[2]/div/div/div[1]/div[2]/div[2]/form/div[2]/div[3]/button').click()
    time.sleep(0.5)

    #click first job
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[3]/section/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/article/span[2]/span/h1/a').click()
   

    #is job application on seek
    if driver.find_elements_by_xpath("//*[contains(text(), 'Applications for this role will take you to the advertiser’s site.')]"):
     driver.execute_script("window.history.go(-1)")
     time.sleep(0.5)
    else:
     time.sleep(1)
     
    #apply for job
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div[2]/aside/span/div[1]/section/div/div[1]/div/span/div/div/div/div/a').click()
    time.sleep(0.1)

    #select resume (make sure resume is previously uploaded)
    ddelement= Select(driver.find_element_by_id('selectedResume'))
    ddelement.select_by_index(1)
    time.sleep(0.1)

    #select/upload cover letter and confirm
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[3]/div/fieldset/div/div[2]/div/div[1]/div[1]/div/div/div/label').click()
    driver.find_element_by_id("uploadedCoverLetter").click()
    time.sleep(0.5)
    os.startfile(r"ENTER PATH TO SCRIPT HERE")
    time.sleep(0.5)
    #driver.find_element_by_css_selector('#desktop-bottom-nav > div > button').click()
    time.sleep(0.5)
    #driver.find_element_by_css_selector('#desktop-bottom-nav > div > button').click()
    time.sleep(99999)
    
    #check next job (UNFINISHED)










    
