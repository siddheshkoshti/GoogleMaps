
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def capture_screenshot(d,path):
    file_name = path + "screenshot_" + time.asctime().replace(":", "_") + ".png"
    d.save_screenshot(file_name)

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.google.com/maps/@18.4929606,73.8286848,15z?entry=ttu")
driver.maximize_window()
driver.implicitly_wait(20)

def searchplace():
    place = driver.find_element(By.XPATH, "//*[@id=\"searchboxinput\"]").send_keys("Mumbai")
    search = driver.find_element(By.XPATH,"//*[@id=\"searchbox-searchbutton\"]")
    search.click()
searchplace()

def directions():
    time.sleep(6)
    route = driver.find_element(By.XPATH, "//*[@id=\"QA0Szd\"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/div")
    route.click()
directions()

def find():
    find = driver.find_element(By.XPATH, "//*[@id=\"sb_ifc50\"]/input").send_keys("Pune")
    time.sleep(6)
    search = driver.find_element(By.XPATH, "//*[@id=\"directions-searchbox-0\"]/button[1]")
    search.click()
find()

def Kilometer():
    time.sleep(5)
    getDirection = driver.find_elements(By.XPATH, "//*[@id=\"QA0Szd\"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div/div[2]/button")
    time.sleep(6)

Kilometer()

driver.save_screenshot("./screenshot/successful.jpeg")