# Simple Application for Selenium module
from typing import KeysView
from selenium import webdriver
import selenium
from selenium.webdriver import common
'''
When you want to use selenium module, you need to download the proper version of browser driver.
Taking Chrome for example, you need to download proper version of chromedriver.exe and put it into the source folder.
(https://chromedriver.chromium.org/downloads)
'''
browser = webdriver.Chrome()
print(type(browser))

# open webpage in browser
browser.get('http://inventwithpython.com')

# search element on the webpage
'''
Function used to search element(s):

browser.find_element_by_class_name()
browser.find_elements_by_class_name()

browser.find_element_by_css_selector()
browser.find_elements_by_css_selector()

browser.find_element_by_id()
browser.find_elements_by_id()

browser.find_element_by_link_text()
browser.find_elements_by_link_text()

browser.find_element_by_partial_link_text()
browser.find_elements_by_partial_link_text()

browser.find_element_by_tag_name()
browser.find_elements_by_tag_name()
'''

# WebElement's attribute and function
# tag_name -> html label name, <a>...
# get_attribute(name)
# text -> return text in the html label
# clear() -> clear text in the form or other text columns
# is_displayed() -> return True, if the element is visible
# is_enabled() -> return True, if the element is enabled
# is_selected() -> return Trun, if the element(box or other buttons in form) is selected
# location -> return dict consists of x and y 


# get specific element on the webpage
try:
    elem = browser.find_element_by_class_name('container')
    print('Find <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# auto click on the button of the webpage
linkElem = browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click() # follows the "Read Online for Free" link

# input and submit the form
# https://keepass.info/help/kb/testform.html (website for test)

browser = webdriver.Chrome()
browser.get('https://keepass.info/help/kb/testform.html')

acceptBtn = browser.find_element_by_id('consent_btn_accept')
acceptBtn.click()

userElem = browser.find_element_by_id('LoginFormUser')
pwdElem = browser.find_element_by_name('pwd')

userElem.send_keys('not an real email')
pwdElem.send_keys('not an real password') # input words to the specific column

pwdElem.submit()

# pass special key (stored at: selenium.webdriver.common.keys)
from selenium.webdriver.common.keys import Keys
'''
Keys.DOWN/UP/LEFT/RIGHT 
Keys.ENTER/RETURN   
Keys.HOME/END/PAGE_DOWN/PAGE_UP 
Keys.ESCAPE/BACK_SPACE/DELETE
Keys.F1~F12 
Keys.TAB
'''
browser = webdriver.Chrome()
browser.get("http://nostarch.com")
htmlElem = browser.find_element_by_tag_name('html') # get the html element and send instruction to the whole webpage
htmlElem.send_keys(Keys.END) #Scrolls to the bottom
htmlElem.send_keys(Keys.HOME) #Scrolls to the top

'''
browser.back() -> go to next page
browser.forward() -> go to previous page
browser.refresh() -> refresh the whole page
browser.quit() -> close the webpage
'''

# More information of the selenium module: https://selenium-python.readthedocs.io/ 
