def loginemail(rambler, password, useragent):
    opts = Options()
    opts.add_argument(f"user-agent={useragent}")
    ramdriver = webdriver.Chrome(chrome_options=opts)
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

    steam(email, useragent)
    ramdriver.switch_to.default_content()
    
    message = ramdriver.find_element_by_xpath("//span[contains(text(),'Steam')]")
    message.click()
    time.sleep(2)
    link = ramdriver.find_elements_by_tag_name('tbody')[8]
    actions.move_to_element(link)
    time.sleep(2)
    link.click()
    time.sleep(5)

    

def steam(rambler, useragent):
    opts = Options()
    opts.add_argument(f"user-agent={useragent}")
    steamdrive = webdriver.Chrome(chrome_options=opts)
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
        element = WebDriverWait(steamdrive, 200).until(
            EC.presence_of_element_located((By.CLASS_NAME, "newmodal"))
        )
    finally:
        time.sleep(5)
    try:
        element = WebDriverWait(steamdrive, 200).until(
            EC.presence_of_element_located((By.CLASS_NAME, "accountname"))
        )
    finally:
        time.sleep(5)