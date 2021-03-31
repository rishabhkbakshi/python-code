from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities['binary'] = 'C:/Program Files/Mozilla Firefox/firefox.exe'
driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path='C:/Users/Rishabh Bakshi/Downloads/Compressed/geckodriver-v0.26.0-win64/geckodriver.exe')

# driver.get("http://www.quora.com")

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# driver.get("https://demoqa.com/automation-practice-form/")

# driver.get("http://hydrology.gov.np/#/basin/180?_k=75qmto")

# driver.get("http://login.microsoftonline.com/")

driver.get("https://www.udemy.com/")
driver.implicitly_wait(30)
driver.maximize_window()
    
# driver.find_element_by_xpath("//input[@placeholder='Email']").clear()
# driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys('bakshirishab90@gmail.com')
# driver.find_element_by_xpath("//input[@placeholder='Password']").clear()
# driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys('Rkb@1991')                          
# #wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[contains(@id,'_submit_button')]"))).click()


# lstDiv = driver.find_elements_by_xpath("//div[@id='sister-projects-list']/div//b/parent::div")
# for div in lstDiv:
#     print(div.text)


# driver.find_elements_by_css_selector("input[name*=sex]")[0].click()
# driver.find_elements_by_css_selector("input[name*=sex]")[1].click()
# 
# lstElemExp = driver.find_elements_by_css_selector("input[type=radio][name*=exp]")
# lstElemExp[4].click()


# Function to fetch the data from the UI table
# def getHourlyDaily():
#     tableData = ''
#     thList = driver.find_elements_by_css_selector('.observation-table th')
#     # enumerate : function allows us to loop over a list and retrieve both the index and the value of each cat in the list
#     for i, th in enumerate(thList):
#         tableData = tableData + th.text + '\t' + ('\n' if i == (len(thList) - 1) else '')
#     
#     trList = driver.find_elements_by_css_selector('.observation-table tbody tr')
#     for tr in trList:
#         tdData = tr.find_elements_by_tag_name('td')
#         for i, td in enumerate(tdData):
#             tableData = tableData + td.text + ('\n' if i == (len(tdData) - 1) else '\t')
#     print(tableData)
# 
# # Code to scroll the page to the 'observation-table'
# tblElem = driver.find_element_by_css_selector(".observation-table")
# driver.execute_script("arguments[0].scrollIntoView();", tblElem)
# 
# # Call the function
# getHourlyDaily()
# # Click on the period dropdown
# driver.find_element_by_css_selector("button svg").click()
# # Select the daily option 
# driver.find_elements_by_css_selector('div span[tabindex]')[2].click()
# # Call the function
# getHourlyDaily()


# userElem = driver.find_element_by_xpath("//input[@name='loginfmt']")
# userElem.click()
# userElem.clear()
# userElem.send_keys('rishabh@gmail.com')
# driver.find_element_by_xpath("//input[@value='Next']").click()
# # time.sleep(5)
# '''
# As you are getting this error 
# 
# selenium.common.exceptions.ElementClickInterceptedException: Message: Element <input id="i0118" class="moveOffScreen" name="passwd" type="password"> 
# is not clickable at point (1361,647) because another element <div id="footerLinks" class="footerNode text-secondary"> 
# obscures it
# 
# then write the xpath of another element which is mentioned in the error 
# which is :- //div[@id='footerLinks']
# 
# use WebDriverWait 
# 
# if you don't want to use this code then simply user sleep()
# time.sleep(5) (But this is not the right way)
# '''
# wait = WebDriverWait(driver, 30);
# wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, "//div[@id='footerLinks']")))
# 
# 
# passElem = driver.find_element_by_xpath("//input[@name='passwd']")
# passElem.click()
# passElem.clear()
# passElem.send_keys('rishabh')
# driver.find_element_by_xpath("//input[@type='checkbox']").click()
# driver.find_element_by_xpath("//input[@value='Sign in']").click()


# text of category name 
txtCatName = 'Development'
# text of sub-category name
txtSubCatName = 'All Development'
# get the element of menu item 
catElem = driver.find_element_by_css_selector("a.dropdown-toggle > span:nth-child(1)")
# hover to the menu item 
ac = ActionChains(driver)
ac.move_to_element(catElem).click(catElem).pause(1).perform()

# Get the list of all category 
lstCat = driver.find_elements_by_css_selector("ul > li > ul > li > a > span:nth-child(2)")
for cat in lstCat:
    # check whether your given category name is displayed or not
    if cat.text.strip() == txtCatName:
        print('\"{txtCatName}\" is found'.format(txtCatName=txtCatName))
        # hover to the given category name 
        ac.move_to_element(cat).pause(1).perform()
        # get the list of all sub-category of the correspond category 
        lstSubCat = driver.find_elements_by_css_selector("ul li ul ul li > a span:nth-child(1)")
        for subCat in lstSubCat:
            # hover to the given sub-category name
            ac.move_to_element(subCat).pause(1).perform()
            # check whether your given sub-category name is displayed or not
            if subCat.text.strip() == txtSubCatName:
                print('\"{txtSubCatName}\" Element is found'.format(txtSubCatName=txtSubCatName))
                # if sub-category is found then break the inner-loop
                break;
            else:
                print('\"{txtSubCatName}\" Element is not found'.format(txtSubCatName=txtSubCatName))
        # also break the outer-loop because sub-category-name is found
        break;
    else:
        print('\"{txtCatName}\" is not found'.format(txtCatName=txtCatName))

driver.quit()
    
