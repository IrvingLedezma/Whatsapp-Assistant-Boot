from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
from datetime import *
import time 
import re

driver = webdriver.Chrome('/home/irving/Descargas/chromedriver') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

Yourname = 'My name'

def bye_zero (input_list) :
    tmp  = input_list.copy()
    for i in range(len(tmp)):
        try :  
            var = int(tmp[i][:2:])
        except :
            var = tmp[i][:2:]
        new_str = str(var) +tmp[i][2::]
        tmp[i] = new_str
    return tmp     

time.sleep(25)

lists_time = driver.find_elements_by_xpath('//div[@class="_1c_mC"]')  
times = [item.text for item in lists_time ]

time_element = []
for element in times :
    for m in re.finditer('\n',element) : 
        try :
            time_element.append(datetime.strptime(element[m.end()::],'%I:%M %p'))
        except Exception:
            pass

time_element = sorted(time_element) 
time_element_post = []
time_element_post = [element.strftime('%I:%M %p') for element in time_element]
time_element_trayec = time_element_post.copy() 
time_element_trayec_n = bye_zero(time_element_trayec).copy()

j =  0

start_time = time.time() 
seconds = 300

while True :

    current_time = time.time() 
    elapsed_time = current_time - start_time
    
    if elapsed_time > seconds : 
        print('Time exceeded, run again  .....')
        break


    if j < 1 : 
        print('You are in the time Loop  ...')

    lists_time = driver.find_elements_by_xpath('//div[@class="_1c_mC"]')  
    times = [item.text for item in lists_time]
    time_element = []
    for element in times :
        for m in re.finditer('\n',element) : 
            try :
                time_element.append(datetime.strptime(element[m.end()::],'%I:%M %p'))
            except Exception:
                pass
    time_element = sorted(time_element) 
    time_element_trayec = []
    time_element_trayec = [element.strftime('%I:%M %p') for element in time_element]
    time_element_trayec_n = []
    time_element_trayec_n = bye_zero(time_element_trayec).copy()

    if time_element_post[-1] != time_element_trayec[-1] :
        print('this change but not all')

    if time_element_post[-1] != time_element_trayec[-1] : 
        for item in lists_time :
            for m in re.finditer('\n',item.text) :
                if time_element_trayec_n[-1] == item.text[m.end()::] :  
                    
                    print("I've found this item " + item.text)
                    item.click()
                    message_box = driver.find_element_by_xpath('//div[@class="DuUXI"]')
                    msg = "Hello, I am Assistance from {}".format(Yourname)
                    msg = msg + "\nYou are Item : " + item.text + '\n' +str(date.today()) 
                    message_box.send_keys(msg)
                    message_box = driver.find_element_by_xpath('//button[@class="_2Ujuu"]')
                    message_box.click()
                    break
    time_element_post = []
    time_element_post = time_element_trayec.copy() 
    j += 1

 
