# try :
#     from selenium import webdriver
# except NameError as e :
#     print  (e)


from selenium import webdriver
import chromedriver_binary 

browser = webdriver.Chrome(
    executable_path ='C:/Program Files/chromedriver/chromedriver.exe')

