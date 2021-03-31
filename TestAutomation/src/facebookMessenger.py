'''
Created on May 4, 2018

Edited on May 1, 2020

Edited on March 25, 2021

@author: Rishabh Bakshi

@summary: 'How can I connect to Facebook and say hello to every friend using Python Selenium?'

'''

import time

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
# import pyautogui

chrome_options = webdriver.ChromeOptions()
'''
1. Disable the push-notification pop-up for a website (profile.default_content_setting_values.notifications)
2. Browser will not ask to for the 'save the password' (profile.password_manager_enabled)
'''
prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.password_manager_enabled" : False}
chrome_options.add_experimental_option("prefs", prefs)
capabilities = chrome_options.to_capabilities()

# to open firefox webbrowser and maximize the window
# driver = webdriver.Firefox(executable_path='C:/Users/Rishabh Bakshi/Downloads/Compressed/geckodriver-v0.20.1-win32/geckodriver.exe')
driver = webdriver.Chrome(executable_path="C:/Users/Rishabh Bakshi/Downloads/Compressed/chromedriver_win32/chromedriver.exe", desired_capabilities=capabilities)
driver.maximize_window()

# driver.set_window_size(50, 200) [Set the size of your driver]
# driver.set_window_position(50, 100) [On the specific portion of the screen]

# Implicit Wait when element is taking time to load
driver.implicitly_wait(20)

# connect to the specific ip address
driver.get("http://www.facebook.com")

# Login to Facebook
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("bakshirishab90@gmail.com")
driver.find_element_by_id("pass").clear()
driver.find_element_by_id("pass").send_keys("RISH?fb1109")
driver.find_element_by_name("login").click();

# Waiting time 
time.sleep(5)

# pyautogui.hotkey('ctrl','f')
# pyautogui.typewrite('', interval=0.25)
# pyautogui.keyDown('enter')
# pyautogui.keyUp('enter')

# Click on Profile Name
driver.find_element_by_xpath("//a[@href='/me/']").click()

# Click on 'Friends' option
driver.find_element_by_xpath("//a[contains(@href,'/friends') and @role='tab']").click()

# Waiting time 
time.sleep(3)

'''
I defined a blank list 
it is used to store 'profile name' of  each friend 
'''
listProfileName = []

# Flag to check the visibility of 'Photos' Section (this section's placing is just after the friend list)
photoSection = False

# Loop to check the 'Photos' Section  in each iteration
while photoSection == False:
    try:
        # Taking the element of 'Photos' Section 
        # We are finding the 'Photos' section which is placed after the friendlist section
        # It will visible when your friendlist is fully loaded
        photoElem = driver.find_element_by_xpath("//h2//a[contains(@href,'/photos')]")
        print(photoElem.text)
        
        # Check the element of 'Photos' Section 
        if photoElem.text == "Photos":
            photoSection = True
            break
        else:
            continue
    except Exception:
        # Get the list of all friends [Remove all duplicate name by using 'set']
        profilePicList = set(driver.find_elements_by_xpath("//img[@height='80']/parent::*[@role='button' or @role='link']"))
        
        # Press PAGE_DOWN to get the invisible friend on the current visible portion on the page
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN);

# traverse all the element of the set
for profilePic in profilePicList:
    # Get the profile URL of friend in each iteration of the loop by using 'href' attribute
                
    profileURL = profilePic.get_attribute("href") if profilePic.tag_name == 'a' else ''
    
    finalProfileName = ''
    
    '''
    We have got two type profile URL 
    1. Which contains Profile name 
    2. Which contains Profile Id
    So we have added both check by using if-else
    '''
    if profileURL == '' :
        finalProfileName = 'user not exist'
    elif profileURL.find('profile.php?id=') == -1:
        finalProfileName = profileURL[profileURL.index('.com/') + len('.com/'):]
    else:
        finalProfileName = profileURL[profileURL.index('profile.php?id=') + len('profile.php?id='):]
    
    # Append the list by the profile name
    listProfileName.append(finalProfileName)
    
'''
Now its time to send message to each and every friend of your friendlist
For this purpose 'What you have to do'

1. You have to apply a for loop to traverse each and every element of the set 
2. Make the Message URL of friend 
3. Hit to the  browser
4. Paste the message

Note :- In case program is getting error while execution. I have added exception handling.
=========================== Wow! It's done =======================
'''
print('Total Friends are {count}'.format(count=len(listProfileName)))

for cat in listProfileName:
    try:
        print("https://www.facebook.com/messages/t/{userName}".format(userName=cat));
        if cat == 'user not exist' :
            continue;
        else:
            driver.get("https://www.facebook.com/messages/t/{userName}".format(userName=cat))
            time.sleep(1)
    #         wait = WebDriverWait(driver, 5, 2, NoSuchElementException);
    #         wait.until(expected_conditions.element_to_be_clickable(driver.find_element_by_xpath("(//span/span[text()='Done'])[1]")), "Element Found").click()
            driver.switch_to_active_element().send_keys("HI, \n its a test message \n plz don't reply \n")
            time.sleep(2)
    except UnexpectedAlertPresentException:
        driver.switch_to_alert().accept()  
    except Exception:
        continue
    
# To close the browser
driver.quit()
