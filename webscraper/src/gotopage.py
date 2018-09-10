from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
##for sleep mainly##
import time
from constants import *
import math
import csv


##creating lists for compolation later##
new_list = []
compiled_list =[["first name", "last name", "agent id", "phone number", "broker"]]
##fields from site we are scraping##
firstnames = []
lastnames = []
broker = []
phonenumber = []
agentid = []
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='Documents\chromedriver', chrome_options=option)

def elementSearch(nameOfInfo, className):
    informationElement = browser.find_elements_by_class_name(className)
    informationList = [x.text for x in informationElement]
    for i in informationList:
        nameOfInfo.append(i)
    return informationList



browser.get("https://idp.northstarmls.com/idp/Authn/UserPassword")

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "formtitle")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

browser.find_element_by_id("j_username").send_keys(username)


browser.find_element_by_id("password")
browser.find_element_by_id("password").click()
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_id("loginbtn").click()

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ctl02_m_ucSpeedBar_m_tbSpeedBar"]')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

for i in range(len(alphabet)):
    browser.get("https://matrix.northstarmls.com/Matrix/Home")
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ctl02_m_ucSpeedBar_m_tbSpeedBar"]')))
    except TimeoutException:
        print("Timed out waiting for page to load")
    browser.find_element_by_xpath('//*[@id="ctl02_m_ucSpeedBar_m_tbSpeedBar"]').send_keys("Agent {}*".format(alphabet[i]),Keys.RETURN)
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ctl01_m_ucSpeedBar_m_tbSpeedBar"]')))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
    numofentries = browser.find_element_by_xpath('//*[@id="m_lblPagingSummary"]/b[3]')
    textentries = numofentries.text
    numofpages = math.ceil((int(textentries)/100))
    elementSearch(firstnames, "d74m9")
    elementSearch(lastnames, "d74m7")
    elementSearch(agentid, "d74m11")
    elementSearch(phonenumber, "d74m12")
    elementSearch(broker, "d74m14")
    for i in range((numofpages-1)):
        browser.execute_script("__doPostBack('m_DisplayCore','Redisplay|,,{}00')".format(i+1))
        try:
            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ctl01_m_ucSpeedBar_m_tbSpeedBar"]')))
        except TimeoutException:
            print("Timed out waiting for page to load")
        elementSearch(firstnames, "d74m9")
        elementSearch(lastnames, "d74m7")
        elementSearch(agentid, "d74m11")
        elementSearch(phonenumber, "d74m12")
        elementSearch(broker, "d74m14")

for i in range(len(firstnames)):
    new_list.append(firstnames[i])
    new_list.append(lastnames[i])
    new_list.append(agentid[i])
    new_list.append(phonenumber[i])
    new_list.append(broker[i])
    compiled_list.append(new_list)
    new_list = []


with open(r"C:\csv\compiled.csv", "w", newline ="") as compiledCSV:
    writecompiledtoCSV = csv.writer(compiledCSV, delimiter=",")
    writecompiledtoCSV.writerows(compiled_list)

browser.quit()
