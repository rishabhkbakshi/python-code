'''
Created on May 4, 2018
@author: Rishabh Bakshi
'''

'''
Before writing this program you have to install 'pyautogui' package
This package will help to interact with windows element
'''
import pyautogui
from selenium import webdriver

# to open firefox webbrowser and maximize the window
browser = webdriver.Firefox(executable_path='<path>/geckodriver.exe')
browser.maximize_window()

# connect to the specific ip address
browser.get("http://192.168.1.1:8090/httpclient.html")

# Here I am pressing the key combination to minimize the current window
# Which alt+space+'n'
pyautogui.keyDown('alt')
pyautogui.keyDown('space')
pyautogui.press('n')
pyautogui.keyUp('space')
pyautogui.keyUp('alt')

#find the html text field names for input of name and password
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

#fill the textfields with with the credentials
username.send_keys("<UserID>")
password.send_keys("<Password>")

#search the button in the html and click the submit button
login = browser.find_element_by_name("btnSubmit")
login.submit()