from selenium import webdriver

#open a page
page=webdriver.chrome()
page.get('https://www.google.com')

#for searching
x=input("enter what you want to search")
searchbox=page.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('x')

#for the search button
searchbutton=page.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[1]/div/span/svg')
searchbutton.click()
