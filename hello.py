from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from webdriver_manager.chrome import ChromeDriverManager
path='C:/Users/habib/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.maximize_window()
url="https://www.kayak.co.in/?ispredir=true"
driver.get(url)
print(url)


 





 
choose_hotel =[]
for d in driver.find_elements(By.CLASS_NAME,'P_Ok-header-links'):
   
    for c in d.find_elements(By.TAG_NAME,'a'):
        hotel= c.get_attribute('href').find('hotel')
        
        if(hotel !=-1):
             
            choose_hotel.append(c.get_attribute('href'))
 
 
 


hotel_url=(choose_hotel[3])

driver.get(hotel_url)
 
 

select_hotel_link =[]




for d in  driver.find_elements(By.CLASS_NAME, 'soom-description'):
    for c in d.find_elements(By.TAG_NAME,'a'):
        
        
        select_hotel_link.append(c.get_attribute('href'))


Chancery_Hote_url=(select_hotel_link[3]) 
driver.get(Chancery_Hote_url)
print(Chancery_Hote_url)

hotel_images = driver.find_element(By.CLASS_NAME,  "FH8P-main-thumbnail")
hotel_images.click()


buttons = driver.find_elements(By.CLASS_NAME,  "DTct-categories-container")
for btn in buttons:
    print(btn.text)
    btn.click()
    time.sleep()
 
 
time.sleep(4)
 
