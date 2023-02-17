from selenium import webdriver
from selenium import common
from time import sleep
from selenium.webdriver.common.by import By
import keyboard
from selenium.webdriver.common import keys
import sys


# Web Draiver Steup
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
chrome_driver_path = r"D:\File\Project_Zero\AutoMation_Project\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver_path, chrome_options=options)
url = "https://twitter.com/"
browser.get(url)

usernameFile = open(sys.argv[1], "r")
data = usernameFile.read()
dataU_into_list = data.split("\n")

emailFile = open(sys.argv[2], "r")
data = emailFile.read()
dataE_into_list = data.split("\n")

count2 = int(sys.argv[3])
usersList = dataU_into_list[count2]
emailsList = dataE_into_list[count2]



def serch():
      try:
        searchbox = browser.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
      except common.exceptions.NoSuchElementException:
        sleep(2)
        searchbox = browser.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
        searchbox.clear()
        searchbox.send_keys('ahmad hmaid')
        searchbox.send_keys(keys.Keys.RETURN)
        keyboard.send("enter")
        sleep(10)
        browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/a/div[4]/div').click()
        sleep(10)  

def retweet():
      if(browser.find_element(By.XPATH,"//div[@data-testid='unretweet']").is_displayed()):
       browser.find_element(By.XPATH,"//div[@data-testid='retweet']").click()
       browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div').click()
        
def like_tweets(cycles=1):
        for i in range(cycles):
            try:
                retweet()
                if(browser.find_element(By.XPATH,"//div[@data-testid='unlike']").is_displayed()):
                  browser.find_element(By.XPATH,"//div[@data-testid='like']").click()
            except common.exceptions.NoSuchElementException:
                sleep(3)
                browser.execute_script('window.scrollTo(0,document.body.scrollHeight/30)') 
                sleep(3)
                retweet()
                browser.find_element(By.XPATH,"//div[@data-testid='like']").click()
            sleep(3)

def logOut():
      browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div').click()
      sleep(3)
      browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]').click()
      sleep(3)
      browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div').click()
      sleep(3)

def follow():
      browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div').click()

# def changeProxy():
#     with open('AutoMation_Project/valid_Proxies.txt','r') as f:
#         proxy = f.readlines()
#         url = 'https://twitter.com/'
#         counter = 0
#     for site in url:
#         try:
#             print(f"Using the proxy : {proxy[counter]}")
#             r = requests.get(url, proxies={'http': proxy[counter], 'https': proxy[counter]})
#             print(r.status_code)
#         except:
#             print("Falied")
#         finally:
#             counter += 1

# def NotifcationDialog() :
#     if(browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div').is_displayed(False)):
#         browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div')
#         browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div').click()
#         print('Hallow this is A notifcation Dialog')

def SingIn():
      try:
            browser.find_element(By.XPATH,'//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a').click()
            sleep(5)
            browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(usersList)
            browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
            sleep(3)
            browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys("010203zaqQAZ")
            browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
            sleep(3)
            # browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(emailsList)
            # browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
            browser.maximize_window()
            browser.implicitly_wait(10)
            browser.get("https://twitter.com/KaramHadi6")
            browser.implicitly_wait(10)
            sleep(3)
            # follow()
            like_tweets()
            sleep(3)
            logOut()
      except Exception:
            sleep(2)
            print('this is an error')
            print("Error" + '\n' + Exception)
            browser.close()

SingIn()
