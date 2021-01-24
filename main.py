from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#newmodal - класс у ждуна в стиме
#MailListItem-dragWrap-2s  - класс контейнера письма

def loginemail(rambler, password):
    ramdriver = webdriver.Chrome()
    ramdriver.set_window_size(800, 800)
    ramdriver.get("https://mail.rambler.ru/")
    actions = ActionChains(ramdriver)

    ramdriver.implicitly_wait(12)

    ramdriver.switch_to.frame(ramdriver.find_element_by_tag_name("iframe"))
    ramemail = ramdriver.find_element_by_id('login')
    rampass = ramdriver.find_element_by_id('password')
    ramin = ramdriver.find_element_by_class_name('rui-Button-content')
    
    ramemail.send_keys(rambler)
    time.sleep(0.2)
    rampass.send_keys(password)
    time.sleep(0.2)
    ramin.click()
