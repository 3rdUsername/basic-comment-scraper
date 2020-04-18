from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time 
from bs4 import BeautifulSoup
import pandas as pd

#chrome_options = Options()
#chrome_options.add_argument("--headless")
#Remove the pound symbol from the first two lines and add the argument in the get() if you don't want a chrome window to open

chromedriver = 'C:\Program Files (x86)\Google\Chrome\chromedriver.exe' #Enter your chromedriver.exe path
driver = webdriver.Chrome(executable_path=chromedriver)


driver.get("") #enter url 

driver.execute_script("window.scrollTo(0, 250)") #get to the bottom to click 'load more comments'
driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[4]/div[1]/a").click() #browser xpath of the sign in button
time.sleep(2)
driver.find_element_by_id("username").send_keys("") #enter your own username
driver.find_element_by_id("password").send_keys("") #enter your own password
time.sleep(2)
driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()
driver.execute_script("window.scrollTo(0, 2700)") #scrolling down to the bottom of the page

time.sleep(2)
driver.find_element_by_xpath("//div[@class='comments-comments-list__show-previous-container']").click()


for i in range(0,400): #I'll update the loop to work till the element is visible in a future update
    driver.execute_script("window.scrollTo(0, 350)")
    time.sleep(1)
    driver.find_element_by_xpath("(//div[@class='comments-comments-list__show-previous-container'])/button").click()
    
html = driver.page_source
soup = BeautifulSoup(html)
emails=[]

for x in soup.findAll('a',attrs={"class":"feed-link ember-view"}):
    string = str(x.getText())
    emails.append(string)
    
email_df= pd.DataFrame(emails)
email_df.to_csv('Emails.csv',index= False)
 
    
 
