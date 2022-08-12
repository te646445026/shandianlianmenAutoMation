from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager


#get直接返回，不再等待界面加载完成
desired_capabilities = DesiredCapabilities.EDGE
desired_capabilities["pageLoadStrategy"] = "none"

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
#browser = webdriver.Edge(executable_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe")
username = 'te646445026'
password = 'cjhmatlab1208'


try:
    #打开浏览器
    try:
        browser.get('http://bbs.sdbeta.com/')
        print("打开浏览器成功")
        print("----------------")
    except:
        print("打开浏览器失败，请检查驱动是否与浏览器版本一致")
        print("----------------")

    #将浏览器最小化显示
    #browser.minimize_window() 
    #等待5s
    time.sleep(5)
    
    #找到用户框，输入账号
    #inputName = WebDriverWait.until(EC.presence_of_element_located((By.ID,'nav_pwuser')))
    inputName = browser.find_element(By.ID,'nav_pwuser')
    inputName.send_keys(username)
    
    
    #找到密码框，输入密码
    #inputPassword = wait.until(EC.presence_of_element_located((By.ID,'showpwd')))
    inputPassword = browser.find_element(By.ID,'showpwd')
    inputPassword.send_keys(password)
    
    #找到登录按钮，点击
    #button = wait.until(EC.presence_of_element_located((By.NAME,'head_login')))
    button  = browser.find_element(By.NAME,'head_login')
    button.click()
    
    time.sleep(2)
    
    #找到每日打卡按钮，点击进入打卡页面
    #button = wait.until(EC.presence_of_element_located((By.NAME,'head_login')))
    button  = browser.find_element(By.CSS_SELECTOR,'#nav_key_up_138').click()
    
    time.sleep(2)
    
    try:
        #点击打卡
        #button = browser.find_element_by_class_name('card fr card_old').click()
        button = browser.find_element(By.ID,'punch').click()
        
        time.sleep(2)
        print('签到成功')
    except :
        print('已签到过')
        
    
    #找到每日签到，输入内容：
    inputWord = browser.find_element(By.ID,'weibo_content')
    Word = input('输入你想说的：')
    inputWord.send_keys(Word)
    
    # #点击发布
    time.sleep(2)
    button = browser.find_element(By.ID,'weibo_submit').click()
    
    time.sleep(2)
    #点击帖子
    button = browser.find_element(By.CSS_SELECTOR,'li#app_article [href]').click()

    time.sleep(2)
    #点击我的回复
    button = browser.find_element(By.ID,'a_post').click()

    time.sleep(2)
    #点击要回复的帖子
    button = browser.find_element(By.CSS_SELECTOR,'tr.tr3>td.f14>a.s5').click()

    try:                                                    
        time.sleep(5)
        #跳转到新页面
        handles = browser.window_handles
        browser.switch_to_window(handles[-1])

        #开始打卡
        time.sleep(2)
        inputWord = browser.find_element(By.CSS_SELECTOR,'textarea#textarea')
        Word = '坚持打卡，坚持坚持'
        inputWord.send_keys(Word)

        #点击发布
        time.sleep(2)
        button = browser.find_element(By.CSS_SELECTOR,'button[name=Submit]').click()

        print('回复成功')
    except :
        print('回复失败')
    
    
    #获取最新积分情况
    time.sleep(2)
    text = browser.find_element(By.CSS_SELECTOR,'p:nth-child(2)>a:nth-child(1)')
    print("我的电魂数量：",text.text)
    text = browser.find_element(By.CSS_SELECTOR,'p:nth-child(2)>a:nth-child(2)')
    print("我的威望数量：",text.text)
    text = browser.find_element(By.CSS_SELECTOR,'p:nth-child(2)>a:nth-child(3)')
    print("我的成员组为：",text.text)


        
except :
    print('打开失败')

finally:
    time.sleep(2)



browser.quit()
    

    

    








