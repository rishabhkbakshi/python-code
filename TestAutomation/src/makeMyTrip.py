'''
Created on May 7, 2018
@author: Rishabh Bakshi
'''
'''  program to automate the automate the login and browser surfing '''
from datetime import datetime, timedelta
from selenium import webdriver
import time

# to open firefox webbrowser and maximize the window
driver = webdriver.Firefox(executable_path='<path>/geckodriver.exe')
driver.maximize_window()

print("Execution");

# connect to the specific ip address
driver.get("https://www.makemytrip.com")

# Click on the 'From Date' field
driver.find_element_by_id("hp-widget__depart").click()

# Get the date of next day
tommorowsDate = datetime.now() + timedelta(days=1);
print(tommorowsDate);

# Get the month of 'tommorowsDate'
strMonth = tommorowsDate.strftime("%B");
print(strMonth);

# Wait Time 
time.sleep(4);

# Get the list of months of opened calendar
strUIMonth = driver.find_elements_by_xpath("//div[contains(@class,'dateFilter')][1]/div[contains(@class,'ui-datepicker-multi')]//span[contains(@class,'month')]")[0]

# Check the month of calculate date to the month of UI date
if strMonth.lower() == strUIMonth.text.lower():
    
    # Used 'following-sibling' to click on tomorrow's day (Edge-Cases)
    if len(list(driver.find_elements_by_xpath("//div[contains(@class,'dateFilter')][1]//td[contains(@class,'ui-datepicker-today') or contains(@class,'ui-datepicker-current')]/following-sibling::td[1]/a"))) != 0:
        
        # Add this code to handle 'StaleElementReferenceException'
        result = False
        while result != True:
            try:
                driver.find_element_by_xpath("//div[contains(@class,'dateFilter')][1]//td[contains(@class,'ui-datepicker-today') or contains(@class,'ui-datepicker-current')]/following-sibling::td[1]/a").click()
            except Exception:
                result = True
    else:
        # If today's date show in the last colomn of calender
        lstDate = driver.find_elements_by_xpath("//div[contains(@class,'dateFilter')][1]/div[contains(@class,'ui-datepicker-multi')]/div[2]//a[@class='ui-state-default']")
        for elem in lstDate:
            if elem.text.lower() == strMonth.lower():
                elem.click()
else:
    # When given date is the ladt day of the month
    lstDate = driver.find_elements_by_xpath("//div[contains(@class,'dateFilter')][2]/div[contains(@class,'ui-datepicker-multi')]/div[2]//a[@class='ui-state-default']")
    for elem in lstDate:
        if elem.text.lower() == "1":
            elem.click()                    

# Close the web browser
driver.quit()