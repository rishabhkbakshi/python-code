import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.password_manager_enabled" : False}
chrome_options.add_experimental_option("prefs", prefs)
capabilities = chrome_options.to_capabilities()

driver = webdriver.Chrome(executable_path="C:/Users/Rishabh Bakshi/Downloads/Compressed/chromedriver_win32/chromedriver.exe", desired_capabilities=capabilities)
driver.maximize_window()

# Implicit Wait when element takes time to load
driver.implicitly_wait(20)
driver.get("http://www.instagram.com")

driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys('xxxxx')
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys('xxxxx')   
wait = WebDriverWait(driver, 30)                       
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
time.sleep(2)

# navigate to the profile page of your account
driver.get("http://www.instagram.com/rishabhkbakshi");

# Get the count of all followers
totalFollowers = int(driver.find_element_by_xpath("//a[contains(@href,'followers')]").text.replace('followers', '').strip())
driver.find_element_by_xpath("//a[contains(@href,'followers')]").click()

# loop till the last follower element
for indx in range(totalFollowers) :
    try:
        target = driver.find_element_by_xpath("//div[@role='presentation']//h1//ancestor::div/div//li[{index}]".format(index=(indx + 1)))
        
        # Code to scroll the followers till the end
        driver.execute_script("arguments[0].scrollIntoView();", target)
    except Exception as e:
        continue

# Print the all account name and user name 
accountNames = driver.find_elements_by_xpath("//div[@role='presentation']//a[not(contains(@style,'height'))]")
list(map(lambda x:print(x.text), accountNames))

'''
.encode("utf-8") is used to handle and encode the emojis
if you don't write this then you will get this type of exeption
UnicodeEncodeError: 'charmap' codec can't encode characters
'''
userNames = driver.find_elements_by_xpath("//div[@role='presentation']//button/parent::div/preceding-sibling::div//div[contains(@class,'w')]")
list(map(lambda x:print(x.text.encode("utf-8")), userNames))

print('done')
