# Simpel webscraper, som navigerer til jobopslaget og udfylder mine oplysninger - så er denne process optimeret.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://s360digital.com/da'

browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="menu-item-6259"]/a').click()

browser.find_element_by_xpath('/html/body/main/ul/li[2]/a').click()

browser.find_element_by_xpath('/html/body/main/article/section[2]/div[2]/div/div/div[2]/div/div/div/div/a').click()

browser.find_element_by_xpath('/html/body/main/article/section[1]/div/div[2]/div/a').click()

time.sleep(2)

window_before = browser.window_handles[0]

window_after = browser.window_handles[1]

browser.switch_to_window(window_after)

FirstName = browser.find_element_by_id('candidate_first_name')
LastName = browser.find_element_by_id("candidate_last_name")
Email = browser.find_element_by_id("candidate_email")
Tlf = browser.find_element_by_id("telephone-input")
CoverLetter = browser.find_element_by_id("candidate_job_applications_attributes_0_cover_letter")

FirstName.send_keys("Christian")
LastName.send_keys("Dahl")
Email.send_keys("mail@christiandahl.com")
Tlf.send_keys("42 510 500")
CoverLetter.send_keys("Ansøgning til job som cloud developer (Studentermedarbejder) hos S360 i Aarhus")
