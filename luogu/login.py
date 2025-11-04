import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ===== 关键：反检测设置 =====
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

wd = webdriver.Chrome(options=options)

# ===== 关键：修改 webdriver 属性 =====
wd.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    '''
})

wd.implicitly_wait(10)

# 登录
wd.get('https://www.luogu.com.cn/auth/login')
# time.sleep(2)  # 等待页面加载

el = wd.find_element(By.CSS_SELECTOR, '#app > div.main-wrapper.lfe-body > div > div > div > div.step-1.active > div:nth-child(1) > div.input-group > input[type=text]')
el.send_keys('1074154081@qq.com')
# time.sleep(1)

wd.find_element(By.CSS_SELECTOR, '#app > div.main-wrapper.lfe-body > div > div > div > div.step-1.active > div:nth-child(1) > button').click()
# time.sleep(2)

psw = wd.find_element(By.CSS_SELECTOR, '#app > div.main-wrapper.lfe-body > div > div > div > div.step-2.active > div.methods > div > input[type=password]')
psw.send_keys('10741Wyk.')
wd.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[1]/div[2]/div/div/input').click()
time.sleep(7)

# 点击登录按钮
login_btn = wd.find_element(By.CSS_SELECTOR, '#app > div.main-wrapper.lfe-body > div > div > div > div.step-2.active > div.methods > div > button')
login_btn.click()
time.sleep(2)

# 访问题目提交页面
wd.get('https://www.luogu.com.cn/problem/P5329#submit')
# time.sleep(3)

# 填充代码（使用 JS）
code = """
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World" << endl;
    return 0;
}
"""


# 输入代码
# //*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]
# //*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div[2]
# //*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div[3]
# //*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div[4]
# wd.find_element(By.XPATH,'//*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]').send_keys('1'+code)
wd.find_element(By.XPATH,'//*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div[2]').send_keys(code)
# wd.find_element(By.XPATH,'//*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div[3]').send_keys('3'+code)
# wd.find_element(By.XPATH,'//*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div[4]').send_keys('4'+code)
# # 点击提交按钮
# //*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/button
# submit_btn = wd.find_element(By.XPATH, '//*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/button')
# submit_btn.click()
# time.sleep(8)
print("代码已提交！")
time.sleep(100)

# wd.quit()