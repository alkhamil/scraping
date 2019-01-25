from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os

chrome_options = Options()
chrome_options.add_argument("--window-size=1366x768")
# path location driver
chrome_driver = 'C:/Data/Project/Github/scraping/driver/chromedriver.exe'
browser = webdriver.Chrome(
    chrome_options=chrome_options, executable_path=chrome_driver)

browser.get('https://datatables.net/examples/styling/display.html')
time.sleep(3)
# select 100
Select(browser.find_element_by_class_name(
    'dataTables_length').find_element_by_tag_name('select')).select_by_value('100')

# find rows
rows = browser.find_element_by_tag_name(
    'tbody').find_elements_by_tag_name('tr')
for row in rows:
    all_col = row.find_elements_by_tag_name('td')
    col_1 = all_col[0].get_attribute('innerHTML')
    col_2 = all_col[2].get_attribute('innerHTML')
    col_3 = all_col[5].get_attribute('innerHTML')
    print("========================================")
    print(col_1 + '|' + col_2 + '|' + col_3)
    print("========================================")


browser.quit()
