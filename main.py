from selenium import webdriver
from selenium.webdriver.common import options
import time
from selenium.webdriver.common.keys import Keys

def get_driver():
  #Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-inforbars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver

def main():
  driver = get_driver()
  #Lấy xpath của các thẻ input và điền thông tin
  driver.find_element(by="id", value="id_username").send_keys("automated")
  
  #Điền tt chờ 2s
  time.sleep(2)
  
  #Điền pass và ấn Enter (Keys.RETURN)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(5)

  #Click Home
  driver.find_element(by= "xpath", value="/html/body/nav/div/a").click()
  
  #Check xem đã đăng nhập đến bước nào
  print(driver.current_url)
  
print(main())
