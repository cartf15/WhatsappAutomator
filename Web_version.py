# try :
#     from selenium import webdriver
# except NameError as e :
#     print  (e)
import sys
sys.setrecursionlimit(2000)

from selenium import webdriver
import chromedriver_binary 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time 
import pandas as pd
import logging


CHROMEDRIVER='C:/Program Files/chromedriver/chromedriver.exe'
FILEPATH='C:/Users/USUARIO/Downloads/FOCUS123.csv'
OUTFILEPATH='C:/Users/USUARIO/Downloads/Contactos_A_EnviarWhatsapp.txt'
MSGPATH='msg.txt'


def __browser__ (CHROMEDRIVER):

    browser = webdriver.Chrome(
        executable_path =CHROMEDRIVER)
    browser.maximize_window()
    browser.get('https://web.whatsapp.com/')
    return browser


def __dataprocess__ (FILEPATH,OUTFILEPATH,MSGPATH):
    csv=pd.read_csv(FILEPATH,sep=',')
    csv=csv.iloc[:, 0:2]
    csv.to_csv(OUTFILEPATH,index = False, header=False,sep=',')

    with open (OUTFILEPATH,'r',encoding='utf8') as f:
        groups=[group.strip().replace(',',' ') for group in f.readlines()]

    # with open ('groups.txt', 'r', encoding='utf8') as f:
    #     groups=[group.strip() for group in f.readlines()]

    with open (MSGPATH,'r',encoding='utf8') as f:
        msg = f.read()
    
    return groups, msg

# time.sleep(30)

def __sendMsg__(browser,groups,msg):

    for group in groups:
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        search_box = WebDriverWait(browser, 500).until(
            EC.presence_of_element_located((By.XPATH, search_xpath))
        )
        # '//*[@id="side"]/div[1]/div/label/div/div[2]''
        
        search_box.clear()

        time.sleep(1)

        pyperclip.copy(group)

        
        search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"

        time.sleep(2)

        try : 
            group_xpath = f'//span[@title="{group}"]'
            group_title = browser.find_element_by_xpath(group_xpath)

            group_title.click()

            time.sleep(1)

            input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
            input_box = browser.find_element_by_xpath(input_xpath)

            pyperclip.copy(msg.format(group.split()[0]))
            input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
            input_box.send_keys(Keys.ENTER)

            time.sleep(2)
                    
        except Exception as e:
            logging.info(e)


browser=__browser__(CHROMEDRIVER)
groups, msg= __dataprocess__ (FILEPATH,OUTFILEPATH,MSGPATH)
__sendMsg__(browser,groups,msg)