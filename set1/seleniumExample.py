from selenium import webdriver

browser = webdriver.Firefox()
#browser.get('https://automatetheboringstuff.com')
#elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a')
#elem.click()
browser.get('https://www.google.com')
elem = browser.find_element_by_css_selector('##tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
elem.send_keys('bloop')
elem.submit()






#elems = browser.find_elements_by_css_selector('p') finds all elements on webpage
