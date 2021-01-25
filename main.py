from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random as rnd
import proxy
#newmodal - класс у ждуна в стиме
#MailListItem-dragWrap-2s  - класс контейнера письма
#accountname  password reenter_password  Готово

def rndtm():
    return rnd.randrange(100, 350, 1) / 1000

def getua():
    r = open('ua.txt', 'r')
    ua = '1'
    step = 0
    rand = rnd.randrange(0, 42)

    for i in r:
        step += 1
        if (step == rand):
            ua = i
    r.close()
    return ua


f = open('emails.txt', 'r')
for str in f:
    useragent1 = getua()
    email = ''
    password = ''
    login = ''
    for i in str:
        if (i != ':'):
            email += i
        if (i == ':'):
            break
    flag = False
    for i in str:
        if (flag == True):
            password += i
        if (i == ':'):
            flag = True
    for i in str:
        if (i != '@'):
            login += i
        if (i == '@'):
            break

    """ opts = Options()
    opts.add_argument(f"user-agent={useragent}") """

    #ramdriver = webdriver.Chrome(chrome_options=opts)
    ramdriver = proxy.get_chromedriver(True, user_agent=useragent1)
    ramdriver.set_window_size(800, 800)
    #ramdriver.get("https://mail.rambler.ru/")
    ramdriver.get("https://2ip.ru")
    time.sleep(20)
    steamdrive = proxy.get_chromedriver(True, user_agent=useragent1)
    steamdrive.get("https://store.steampowered.com/join/")
    #steam(email, useragent)
    steamdrive.implicitly_wait(12)
    fomemail = steamdrive.find_element_by_id('email')
    formemail2 = steamdrive.find_element_by_id('reenter_email')
    checkbox = steamdrive.find_element_by_id('i_agree_check')
    submit = steamdrive.find_element_by_id('createAccountButton')
    cap = steamdrive.find_element_by_tag_name("iframe")

    fomemail.send_keys(email)
    time.sleep(0.2)
    formemail2.send_keys(email)
    time.sleep(0.2)
    checkbox.click()
    time.sleep(0.2)
    cap.click()
    time.sleep(1)
    #</steam>
    actions = ActionChains(ramdriver)

    ramdriver.implicitly_wait(12)

    ramdriver.switch_to.frame(ramdriver.find_element_by_tag_name("iframe"))
    ramemail = ramdriver.find_element_by_id('login')
    rampass = ramdriver.find_element_by_id('password')
    ramin = ramdriver.find_element_by_class_name('rui-Button-content')
    ramemail.send_keys(email)
    time.sleep(0.2)
    rampass.send_keys(password)
    time.sleep(0.2)
    ramin.click()

    try:
        element = WebDriverWait(steamdrive, 400).until(
            EC.presence_of_element_located((By.CLASS_NAME, "newmodal"))
        )
    finally:
        time.sleep(6)
        
    ramdriver.switch_to.default_content()
    
    message = ramdriver.find_element_by_xpath("//span[contains(text(),'Steam')]")
    message.click()
    time.sleep(2)
    link = ramdriver.find_elements_by_tag_name('tbody')[8]
    actions.move_to_element(link)
    time.sleep(2)
    link.click()
    time.sleep(3)
    #<steam>
    try:
        element = WebDriverWait(steamdrive, 200).until(
            EC.presence_of_element_located((By.ID, "accountname"))
        )
        loginput = steamdrive.find_element_by_id('accountname')
        passput = steamdrive.find_element_by_id('password')
        passput2 = steamdrive.find_element_by_id('reenter_password')
        submitbut = steamdrive.find_element_by_xpath("//span[contains(text(),'Готово')]")
        loginput.send_keys(login)
        time.sleep(0.2)
        passput.send_keys(password)
        time.sleep(0.2)
        passput2.send_keys(password)
        time.sleep(0.2)
        submitbut.click()
        time.sleep(30)
    finally:
        time.sleep(5)
    #</steam>




    