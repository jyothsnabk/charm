"""
Author:jyothsna
date:29/06/2020

"""


import time

from selenium import webdriver
from selenium.webdriver import ActionChains
# opening browser
from selenium.webdriver.common import keys
#opening browser
driver=webdriver.Chrome()

time.sleep(2)
driver.get("https://www.charmhealth.com/")
#maximize windows
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//span[text()='Login']").click()
driver.find_element_by_xpath("//input[@id='lid']").send_keys("dev+2@deepscribe.ai ")
driver.find_element_by_xpath("//input[@name='pwd']").send_keys('vgS9Y3RDhq2tnhE')
driver.find_element_by_xpath("//div[@id='signin_submit']").click()
time.sleep(1)
#hanling pop up
driver.find_element_by_xpath("//i[@class='v1-dialog-close-icon']").click()
#to click on cHARTS
driver.find_element_by_xpath("//i[@class='charts-menu-icon']").click()
time.sleep(2)
#selecting new patient
driver.find_element_by_xpath("//td[@id='encounterTitle_567242000000023809']").click()
time.sleep(2)
#clicking on edit button
driver.find_element_by_xpath("//button[text()='Edit']").click()
time.sleep(3)
#to get the elements listed under
elements=driver.find_elements_by_xpath("//div[@class='ulNoStyle']")
for i in elements:
    print(i.text)
#to select history option
elements[0].click()
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='ze_area']"))
## Insert text via xpath #
elem = driver.find_element_by_xpath("/html/body/div")
# updating the data for history
elem.send_keys("Patient presents today for concerns regarding his palpitations, but nothing he thinks is serious. He notes that he can use his Apple Watch when he experiences these palpitations. He denies having passed out. Patient’s event monitor shows that he had an auto trigger 14 times, but nothing critical. His lowest heart rate was 39 and high highest heart rate was 157. There is only sinus rhythm. When patient passed out on the tilt table, his blood pressure dropped from 109/74 to 80/63 and after his blood pressure dropped, his heart rate that was 90 dropped as well. Patient quit smoking. Current medications include: Cyproheptadine, Lexapro 10mg")
#to slect physical examination
elements[1].click()
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='ze_area']"))
## Insert text via xpath ##
elem = driver.find_element_by_xpath("/html/body/div")
elem.send_keys("")
driver.close()

