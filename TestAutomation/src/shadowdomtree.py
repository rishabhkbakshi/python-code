from selenium import webdriver


def expand_shadow_element(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.password_manager_enabled" : False}
chrome_options.add_experimental_option("prefs", prefs)
capabilities = chrome_options.to_capabilities()

driver = webdriver.Chrome(executable_path="C:/Users/Rishabh Bakshi/Downloads/Compressed/chromedriver_win32/chromedriver.exe", desired_capabilities=capabilities)
driver.maximize_window()

# Implicit Wait when element takes time to load
driver.implicitly_wait(20)
driver.get("https://developer.servicenow.com/dev.do")

root11 = driver.find_element_by_tag_name('dps-app')
shadow_root11 = expand_shadow_element(root11)

root0 = shadow_root11.find_element_by_tag_name('dps-navigation-header')
shadow_root0 = expand_shadow_element(root0)

root1 = shadow_root0.find_element_by_tag_name('dps-login')
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element_by_css_selector('dps-button')
shadow_root2 = expand_shadow_element(root2)

search_button = shadow_root2.find_element_by_css_selector('span.dps-button-label')
search_button.click()

