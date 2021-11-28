
#导入程序需要的库
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import xlrd
import sys


#定义获取信息的函数
def get_info():
    #cursor.execute("create table if not exists shuoshuo(id int primary key auto_increment,name varchar(4),time varchar(50),contents varchar(150));")

    # 读取账号密码
    account_number = None
    password = None
    with open('acc_pass.txt', encoding='utf-8') as f:
        cnt = 0
        for line in f.readlines():
            line = line.strip()
            if cnt == 0:
                account_number = line[4:-1]
                cnt += 1
            else:
                password = line[4:-1]
    #声明变量
    global time
    # 请求url隐式等待15s
    driver.get('http://stu.zstu.edu.cn/webroot/decision/login?origin=d437973c-0849-491b-968d-a3f50f534381')
    driver.implicitly_wait(15)




    driver.find_element_by_xpath(
        '//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/input').clear()

    # 账号密码
    driver.find_element_by_xpath(
        '//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/input').send_keys(account_number)
    driver.find_element_by_xpath(
        '//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/input').clear()
    driver.find_element_by_xpath(
        '//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div/div[6]/div/div[1]').click()
    time.sleep(5)

    driver.find_element_by_xpath(
        '//*[@id="wrapper"]/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[5]/div/div/div[1]/div/div[1]/div/div/div[1]/div/div[4]').click()
    driver.implicitly_wait(3)

    driver.find_element_by_xpath(
        '//*[@id="wrapper"]/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[5]/div/div/div[1]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div[3]').click()


    #切换iframe
    iframe = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div[1]/div/div[1]/div[1]/div[1]/iframe[2]')
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath('//*[@id="B12-0-0"]/span').click()

    #切回去再切进iframe，因为页面出现了更变
    time.sleep(1)
    driver.implicitly_wait(15)
    driver.switch_to.default_content()
    iframe = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div[1]/div/div[1]/div[1]/div[1]/iframe[2]')
    print(iframe)
    driver.switch_to.frame(iframe)

    #浙江理工大学填入
    k = driver.find_element_by_xpath('//*[@id="D10-0-0"]/div/input')
    k.send_keys('浙江理工大学')

    #省、市、区写入
    k = driver.find_element_by_xpath('//*[@id="D9-0-0"]/div/div[2]')
    k.click()
    driver.implicitly_wait(3)
    time.sleep(0.5)
    sheng = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[34]')
    sheng.click()
    driver.implicitly_wait(3)
    k = driver.find_element_by_xpath('//*[@id="E9-0-0"]/div/div[2]')
    k.click()
    driver.implicitly_wait(4)
    time.sleep(0.5)
    shi = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]')
    shi.click()
    driver.implicitly_wait(3)
    k = driver.find_element_by_xpath('//*[@id="F9-0-0"]/div/div[1]/input')
    k.send_keys("江干区")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div').click()
    driver.implicitly_wait(3)

    #身体状况
    bodystatus = driver.find_element_by_xpath('//*[@id="D18-0-0"]/div/span[1]/div')
    bodystatus.click()
    #页面滚动、填报
    js4 = "arguments[0].scrollIntoView();"
    temperature1 = driver.find_element_by_xpath('//*[@id="D20-0-0"]/div/span[1]/div')
    driver.execute_script(js4, temperature1)
    temperature1.click()
    driver.implicitly_wait(3)
    temperature2 = driver.find_element_by_xpath('//*[@id="D21-0-0"]/div/span[1]/div').click()
    driver.implicitly_wait(3)
    healthcode1 = driver.find_element_by_xpath('//*[@id="F26-0-0"]/div/span[1]/div')
    driver.execute_script(js4, healthcode1)
    healthcode1.click()
    driver.implicitly_wait(3)
    bigdatacode2 = driver.find_element_by_xpath('//*[@id="F27-0-0"]/div/span[1]/div').click()
    driver.implicitly_wait(3)
    yesorno3 = driver.find_element_by_xpath('//*[@id="F28-0-0"]/div/span[2]/div').click()
    driver.implicitly_wait(3)
    yesorno4 = driver.find_element_by_xpath('//*[@id="F29-0-0"]/div/span[2]/div').click()
    driver.implicitly_wait(3)
    yesorno5 = driver.find_element_by_xpath('//*[@id="F30-0-0"]/div/span[2]/div')
    driver.execute_script(js4, yesorno5)
    yesorno5.click()
    driver.implicitly_wait(3)
    yesorno6 = driver.find_element_by_xpath('//*[@id="F32-0-0"]/div/span[2]/div').click()
    driver.implicitly_wait(3)
    yesorno7 = driver.find_element_by_xpath('//*[@id="F34-0-0"]/div/span[1]/div/span').click()
    driver.implicitly_wait(3)

    # 最后三个选项
    last_yesorno1 = driver.find_element_by_xpath('//*[@id="F36-0-0"]/div/span[2]/div')
    driver.execute_script(js4, last_yesorno1)
    last_yesorno1.click()
    driver.implicitly_wait(3)
    last_yesorno2 = driver.find_element_by_xpath('//*[@id="F38-0-0"]/div/span[2]/div').click()
    driver.implicitly_wait(3)
    last_yesorno3 = driver.find_element_by_xpath('//*[@id="F40-0-0"]/div/span[2]/div').click()
    driver.implicitly_wait(3)

    #提交
    submit = driver.find_element_by_xpath('//*[@id="fr-btn-"]/div')
    submit.click()

if __name__ == '__main__':
    
    driver = webdriver.Chrome(R"E:\桌面\py程序\Eauto\chromedriver.exe")
    driver.maximize_window()

    get_info()
    print("完成")

