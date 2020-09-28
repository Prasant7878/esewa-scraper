from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10) # seconds
options = webdriver.ChromeOptions()
options.set_headless()


def login(username, password):
    driver.get('https://esewa.com.np')

    username_field = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div[1]/input')
    password_field = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div[2]/input')
    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div[3]/button[1]')
    print('[+] Elements Found')
    username_field.send_keys(username)
    print('[+] Username Entered')
    password_field.send_keys(password)
    print('[+] Password Entered')
    password_field.send_keys(Keys.RETURN)


class LastTransaction:
    def __init__(self):
        while not driver.current_url == "https://esewa.com.np/#/statements":
            print('[+] Gettings Statements page')
            driver.get('https://esewa.com.np/#/statements')
            time.sleep(1)

        self.text = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[3]/div[2]').text
        self.date = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[2]').text
        self.credited_amount = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[7]/span').text
        self.debited_amount = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[6]').text
        self.channel = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[9]').text
        self.balance = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr/td[8]').text
        self.statement = self.text + ' --> Rs. ' + self.credited_amount + ' at ' + self.date


def sniff():
    # First login then,
    # sniff
    lt = LastTransaction()
    last_balance = lt.balance
    while 1:
        driver.refresh()
        try:
            lt = LastTransaction()
        except:
            continue
        if last_balance != lt.balance:
            last_balance = lt.balance
            print(lt.statement)
        time.sleep(1)



if __name__ == '__main__':
    username = '9863467818'
    password = '#g2$&RaFQSFdg&6W%2j545X5@X'
    login(username, password)
    sniff()
