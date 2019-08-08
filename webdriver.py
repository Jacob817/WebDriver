from selenium import webdriver
browser = webdriver.Chrome('D:\\Thz\\Python\\chromedriver')
browser.get('http://www.baidu.com')
searchBar = browser.find_element_by_id('kw')
searchBar.send_keys('炸鸡')
cli = browser.find_element_by_id('su')
cli.click()
