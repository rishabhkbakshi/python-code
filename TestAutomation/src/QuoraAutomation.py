'''
Created on May 4, 2020

@author: Rishabh Bakshi
'''

import os
import time
# Package for excel library
import xlsxwriter
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class QuoraAutomation:
             
    def browserInitialization(self):
        chrome_options = webdriver.ChromeOptions()
        '''
        1. Disable the push-notification pop-up for a website (profile.default_content_setting_values.notifications)
        2. Browser will not ask for the 'save the password' (profile.password_manager_enabled)
        '''
        prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.password_manager_enabled" : False}
        chrome_options.add_experimental_option("prefs", prefs)
        capabilities = chrome_options.to_capabilities()
         
        # Give the path of you chromedriver
        driver = webdriver.Chrome(executable_path=r"C:/Users/Rishabh Bakshi/Downloads/Compressed/New folder/chromedriver_win32/chromedriver.exe", desired_capabilities=capabilities)
        driver.maximize_window()
         
        # Implicit Wait when element takes time to load
        driver.implicitly_wait(30)
        driver.get("http://www.quora.com")
        return driver
     
    # Used 'staticmethod' annotation so i can call the method direct by the name of class
    @staticmethod
    def exportAnswersToExcel(setQuestions, allAnswersData):
        # ---------------- Now we have all answers data (allAnswersData) -------- #
         
        '''
        $$$$$
            It's time to write all data into the excel file
            Are you ready ?
            Yes ?
             
            Then let's go
        $$$$$
        '''
        # xlsxwriter => See at the top or visit this link (https://xlsxwriter.readthedocs.io/)
        workbook = xlsxwriter.Workbook('All_Quora_Answer.xlsx')
        # Giving the name of excel-sheet
        worksheet = workbook.add_worksheet('Answers-Details')
         
        # formatting the excel
        col_format = workbook.add_format({'bold': True, 'font_size' : 15, 'align': 'left', 'align': 'top', 'border': 1})
        worksheet.set_column(0, 1, 70)
         
        # Define the columns
        worksheet.write('A1', 'Questions', col_format)
        worksheet.write('B1', 'Answers', col_format)
         
        cell_format = workbook.add_format()
        cell_format.set_align('left')
        cell_format.set_align('top')
        cell_format.set_text_wrap(True)
     
        # set the data into the cells of excel
        if len(setQuestions) == len(allAnswersData):  
             
            # For Questions 
            for i in range(len(setQuestions)):
                worksheet.write('A{index}'.format(index=(i + 2)), setQuestions[i], cell_format)
             
            # For answers
            for i in range(len(allAnswersData)):
                tempList = allAnswersData[i]
                worksheet.write('B{index}'.format(index=(i + 2)), '\n'.join(tempList), cell_format)
         
        # Close the object of excel              
        workbook.close()
         
    def timeToAction(self, driver):
        try:
            # Explicit Wait for special condition
            wait = WebDriverWait(driver, 30)
             
            # login to the quora with your credential
            driver.find_element_by_xpath("//input[@placeholder='Email']").clear()
            driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys('bakshirishab90@gmail.com')
            driver.find_element_by_xpath("//input[@placeholder='Password']").clear()
            driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys('Rkb@1991')                          
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[contains(@id,'_submit_button')]"))).click()
               
            time.sleep(2)
             
            # click on your profile pic which is place at top right     
            # then click on on the your name xpath=> (//div[contains(@class,'q-relative')]//img)[1]
            driver.find_element_by_css_selector("div.q-inlineFlex > img.qu-minWidth--24").click()
            # xpath = (//img/ancestor::a[contains(@href,'profile')])/ancestor::div/following-sibling::a
            wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a.q-box  span[class*=Title]"))).click()
             
            # switch to new window
            driver.switch_to_window(driver.window_handles[1])
                 
            # Get the total answers count you have written
            totalAnswersCount = int(driver.find_element_by_css_selector("div.q-click-wrapper[role=tab]:nth-child(2)").text.replace('Answers', '').strip())
            print('Total Answer I have written => {count}'.format(count=totalAnswersCount))
             
            # Click on answers tab which is place at below the your profile summary
            driver.find_element_by_xpath("(//div[contains(@class,'qu-whiteSpace--nowrap')]//div[contains(@class,'qu-display--flex')])[2]").click()
             
            # use set to store only distinct web-element of each answers block
            setAnswers = set()
            # Define the list for questions
            setQuestions = list()
             
            '''
            While loop to get the answers block till the end of page 
            Because at the one time the quora shows only 10 answers 
            If you go at the 10th answers then page will load 
            and show next 10-15 answers
            '''
            breakCondition = False
            while breakCondition == False:
                # Giving the condition to ensure that my all answers are loaded 
                if len(setAnswers) < totalAnswersCount :
                    # pressing 'Page-Down' key to reach at the bottom
                    # I used 'body' tag you can use any parent tag like. <form>, <html> etc
                    driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
                    lstElems = driver.find_elements_by_xpath("//div[contains(@class,'spacing_log_answer_content')]")
                    setAnswers.update(lstElems)
                else:
                    # Now my defined 'set' is loaded by my all answers block element 
                    breakCondition = True
             
            '''
            Define the list to store all the my answers data
            In this list I am storing list of list
            '''
            allAnswersData = []
            # checking the count of all answers
            '''
            len() => To get the size of the collection
            range() => function returns a sequence of numbers, starting from 0 by default, 
                        and increments by 1 (by default), and ends at a specified number.
            format() => the specified value(s) and insert them inside the string's placeholder.
                        (https://www.w3schools.com/python/ref_string_format.asp)
            strip() => As as .trim() in java
            list() => to convert any type of collection into list
            map() => a specified function for each item in a iterable
            '''
            if totalAnswersCount == len(setAnswers):
                for i in range(totalAnswersCount):
                    # Getting the the text of a particular Question
                    strQues = driver.find_element_by_xpath(
                                                "(//div[contains(@class,'qu-flexWrap--wrap')]//span[@class='rendered_qtext'])[{index}]".format(index=(i + 1))).text
                     
                    # Store into the 'setQuestions'
                    setQuestions.append(strQues)
                    print("Question No. => {index} => \n{questions}".format(index=(i + 1), questions=strQues))
                    print("Writing the data for Answer No. => {index} => \n".format(index=(i + 1)))
                     
                    # Code to click on '(more)' link button of particular answer
                    ac = ActionChains(driver)
                    try:
                        lnkMore = driver.find_element_by_xpath("(//div[contains(@class,'spacing_log_answer_content')])[{index}]//div[contains(text(),'(more)')]"
                                                               .format(index=(i + 1)))
                        ac.move_to_element(lnkMore).click(lnkMore).pause(1).perform()
                    except Exception:
                        ac.move_to_element(driver.find_element_by_xpath("(//div[contains(@class,'spacing_log_answer_content')])[{index}]"
                                                                      .format(index=(i + 1)))).click().pause(1).perform()
                     
                    # Some sleep time to load the whole answer content
                    time.sleep(2)
                     
                    # Get every elements of the answer. like 'p','div', 'img', 'ol', 'blockquote' and 'pre'
                    lstAllAnswerElem = driver.find_elements_by_xpath("((//div[contains(@class,'spacing_log_answer_content')]//span[contains(@class,'rendered_qtext')])"
                                                + "[{index}])/*".format(index=(i + 1)))
                        
                    # Define the list to get all data of one answer
                    answerData = []
                    for j in range(len(lstAllAnswerElem)):
                        tagName = lstAllAnswerElem[j].tag_name.strip()
                        # .text is used to get inner text of web-element
                        if  tagName == 'p':
                            answerData.append(lstAllAnswerElem[j].text)
                        elif tagName == 'div':
                            '''
                            Code will execute if the answers content any image
                            1. Getting all elems of images
                            2. Set the directory path to store the image
                            3. Set the name of image 
                            4. Download the image.
                            '''
                            try:
                                # 1
                                elemDiv = driver.find_element_by_xpath("((//div[contains(@class,'spacing_log_answer_content')]//span[contains(@class,'rendered_qtext')])[{indexi}])/*[{indexj}]//img".format(indexi=(i + 1), indexj=(j + 1)))
                   
                                # 2 os.getcwd() => returns current working directory of a process
                                filePathForImage = "{path}\\answers-images\\Answer_{index}".format(path=os.getcwd(), index=(i + 1))
                                 
                                if os.path.exists(filePathForImage) == False:
                                    os.makedirs(filePathForImage)
                                 
                                # 3
                                answerData.append("Image Path => {path}\\Image_In_Div_{index}.png".format(path=filePathForImage, index=(j + 1)))
                                 
                                # 4 To download the image        
                                urlretrieve(elemDiv.get_attribute('src').replace('.webp', ''), "{path}\\Image_In_Div_{index}.png".format(path=filePathForImage, index=(j + 1)))
                            except Exception as e:
                                print('error{msg}'.format(msg=e)) 
                            answerData.append(lstAllAnswerElem[j].text)
                        elif tagName == 'blockquote':
                            answerData.append('\"{data}\"'.format(data=lstAllAnswerElem[j].text))
                        elif tagName == 'pre':
                            answerData.append('\"\"{data}\"\"'.format(data=lstAllAnswerElem[j].text))
                        elif tagName == 'ol':
                            # if you have written answer content after click on bullet points
                            liList = lstAllAnswerElem[j].find_elements_by_tag_name("li")
                            # traverse each elem of bullet points and append to the 'answerData' 
                            list(map(lambda x: answerData.append('\t{data}'.format(data=x.text)), liList))
                       
                    # if you have written any reference links in you answers.    
                    hrefList = driver.find_elements_by_xpath("((//div[contains(@class,'spacing_log_answer_content')]//span[contains(@class,'rendered_qtext')])[{index}])//a"
                                                      .format(index=(i + 1)));
                    answerData.append('Reference_Links =>\n')
                    list(map(lambda x:answerData.append('\t{hrefAttrib}'.format(hrefAttrib=x.get_attribute('href'))), hrefList))
                     
                    # Store the all data of a particular answer
                    allAnswersData.append(answerData)
                     
            QuoraAutomation.exportAnswersToExcel(setQuestions, allAnswersData);
            print('Done')
        except Exception as e:
            print('error{msg}'.format(msg=e)) 
     
        # Close the browser.
        driver.close()
 
 
# We know when main() method is present in the program then this method will call first
def main():
    objQA = QuoraAutomation()
    driver = objQA.browserInitialization()
    objQA.timeToAction(driver)
 
 
# To call main method at the initialization of call then we have to write this block of code
if __name__ == "__main__":
    main()
