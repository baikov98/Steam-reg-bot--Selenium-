from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    print()
    ramemail.send_keys(rambler)
    time.sleep(0.2)
    rampass.send_keys(password)
    time.sleep(0.2)
    ramin.click()

    steam(email)
    ramdriver.switch_to.default_content()
    
    message = ramdriver.find_element_by_xpath("//span[contains(text(),'Steam')]")
    message.click()
    time.sleep(2)
    link = ramdriver.find_elements_by_tag_name('tbody')[8]
    #ramdriver.find_element_by_xpath("//span[contains(text(),'Подтвердить адрес эл. почты')]")

    actions.move_to_element(link)
    time.sleep(2)
    link.click()
    time.sleep(120)

def steam(rambler):
    steamdrive = webdriver.Chrome()
    steamdrive.get("https://store.steampowered.com/join/")

    steamdrive.implicitly_wait(12)

    fomemail = steamdrive.find_element_by_id('email')
    formemail2 = steamdrive.find_element_by_id('reenter_email')
    checkbox = steamdrive.find_element_by_id('i_agree_check')
    submit = steamdrive.find_element_by_id('createAccountButton')
    cap = steamdrive.find_element_by_tag_name("iframe")

    fomemail.send_keys(rambler)
    time.sleep(0.2)
    formemail2.send_keys(rambler)
    time.sleep(0.2)
    checkbox.click()
    time.sleep(0.2)
    cap.click()
    time.sleep(1)
    try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "newmodal"))
    )
    finally:
        driver.quit()




f = open('emails.txt', 'r')
for str in f:
    email = ''
    password = ''

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

    #steam(email)
    loginemail(email, password)


""" def main():
    if __name__ == "__main__":
        main() """