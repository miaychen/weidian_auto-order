#By default, the login page set “手机号快捷登录” and region = 中国 （+86)

#loginlive: allows you to login manually 





#loginHK: automatically login when you provide (1)username; (2)password;(3)the link of the item you want to purchase when your login mobile number belongs to Hong Kong (+852). 
#If you want to change to ohter regions (except for mainland China), you may change the css selector under #点香港 choose Hong Kong to find the particular regions you want
def loginHK(item_link, username, password):
    try:        
        
        driver.get("https://sso.weidian.com/login/index.php?")

        time.sleep(1)

        #点登录 click "login" 
        driver.find_element_by_id("login_init_by_login").click()
        time.sleep(1)

        #点账号密码登录 Choose login by username and password
        driver.find_element_by_class_name("login_content_h4").click()
        time.sleep(1)

        #点选择国家和地区 Choose country and region
        driver.find_element_by_id("login_pwd_right").click()
        time.sleep(1)

        #点香港 choose Hong Kong
        driver.find_elements_by_css_selector("ul#login_country_code_list > li:nth-child(21) > ul > li")[9].click()

        driver.find_element_by_css_selector("input#login_isRegiTele_input").clear()
        driver.find_element_by_css_selector("input#login_isRegiTele_input").send_keys(username)
        driver.find_element_by_css_selector("input#login_pwd_input").clear()
        driver.find_element_by_css_selector("input#login_pwd_input").send_keys(password)

        print("1秒后将会自动完成登录 try auto-login in 1 second")
        time.sleep(1)

        driver.find_element_by_id("login_pwd_submit").click()

        print("检测是否登录成功 Check whether login successfully")
        driver.get(str(item_link))
        time.sleep(3)
        try:
          driver.find_element_by_class_name("my-order"):
            print("(1)登录成功，进入下一步 Login: success, to next step")

    except Exception as ex:
        print("Error:" + str(ex))
        sys.exit()
