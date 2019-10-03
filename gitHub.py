# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 00:57:14 2018

@author: Fauzan
"""
#Install Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime

from selenium.webdriver import ActionChains

import os

# User Configuration
UserName = 'testQAFauzan'
Password = 'anotherjasmineofmine'

# Agar Path ke Chromedriver didefinisikan otomatis
cwd = os.getcwd()
driver = webdriver.Chrome(executable_path = cwd + "/chromedriver.exe")
driver.maximize_window()

# Menuju halaman utama Github
driver.get("https://github.com/")

# Login
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
driver.find_element_by_name('login').send_keys(UserName)
driver.find_element_by_name('password').send_keys(Password)
driver.find_element_by_name('commit').click()

# Create New Gist
driver.get("https://github.com/")

driver.find_element_by_xpath('//summary[@aria-label="Create new…"]').click()
driver.find_element_by_xpath('//a[@data-ga-click="Header, create new gist"]').click()

driver.find_element_by_name('gist[description]').send_keys('Gist ' + str(datetime.now()))

driver.find_element(By.NAME, "gist[contents][][name]").send_keys("file" + str(datetime.now()) + ".md")

el = driver.find_element(By.CLASS_NAME, "CodeMirror-lines")
ActionChains(driver).move_to_element(el).click(el).send_keys('Description file' + str(datetime.now())).perform()

driver.find_element_by_name('gist[public]').click()

# Edit Existing Gist
driver.get("https://github.com/")

driver.find_element_by_xpath('//summary[@aria-label="View profile and more"]').click()
driver.find_element_by_xpath('//a[@data-ga-click="Header, your gists, text:your gists"]').click()

driver.find_element_by_xpath('//*[@id="gist-pjax-container"]//div[2]/div[1]//a[2]/strong').click()

driver.find_element_by_xpath('//a[@aria-label="Edit this Gist"]').click()

driver.find_element_by_name('gist[description]').send_keys(' Updated')

el = driver.find_element_by_xpath('//button[@class="btn btn-primary"]')
ActionChains(driver).move_to_element(el).click(el).perform()

# Delete Existing Gist
driver.get("https://github.com/")

driver.find_element_by_xpath('//summary[@aria-label="View profile and more"]').click()
driver.find_element_by_xpath('//a[@data-ga-click="Header, your gists, text:your gists"]').click()

driver.find_element_by_xpath('//*[@id="gist-pjax-container"]//div[2]/div[1]//a[2]/strong').click()

driver.find_element_by_xpath('//button[@aria-label="Delete this Gist"]').click()

alert = driver.switch_to_alert()
alert.accept()

# View Existing Gist
driver.get("https://github.com/")

driver.find_element_by_xpath('//summary[@aria-label="View profile and more"]').click()
driver.find_element_by_xpath('//a[@data-ga-click="Header, your gists, text:your gists"]').click()

driver.close()