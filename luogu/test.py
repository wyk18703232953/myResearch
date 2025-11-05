import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

def login(wd, email, password):
    wd.get('https://www.luogu.com.cn/auth/login')
    el = wd.find_element(By.CSS_SELECTOR, '#app > div.main-wrapper.lfe-body > div > div > div > div.step-1.active > div:nth-child(1) > div.input-group > input[type=text]')
    el.send_keys(email)
    wd.find_element(By.CSS_SELECTOR, '#app > div.main-wrapper.lfe-body > div > div > div > div.step-1.active > div:nth-child(1) > button').click()
    psw = wd.find_element(By.CSS_SELECTOR, '#app > div.main-wrapper.lfe-body > div > div > div > div.step-2.active > div.methods > div > input[type=password]')
    psw.send_keys(password)
    wd.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[1]/div[2]/div/div/input').click()
    time.sleep(7)


def submit_code(wd, url, code):
    wd.get(url)
    wd.execute_script("""
        arguments[0].innerText = arguments[1];
        // 如果需要保留格式用 innerHTML
        // arguments[0].innerHTML = arguments[1];
    """, wd.find_element(By.XPATH, '//*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div[2]'),code
    )
    submit_btn = wd.find_element(By.XPATH, '//*[@id="app"]/div[4]/main/div/div/div[2]/div/div[2]/button')
    # submit_btn.click()
    time.sleep(8)
    print("代码已提交！")

# ===== 关键：反检测设置 =====
if __name__ == "__main__":
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
    try:
        email='1074154081@qq.com'
        password='10741Wyk.'
        login(wd, email, password)
        file_path="D:/myResearch/luogu/answer/P10716.txt"
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
            # print(code)
        # url=f"https://www.luogu.com.cn/problem/{pid}#submit"
        url=f"https://www.luogu.com.cn/problem/P1393#submit"
        time.sleep(2)
        submit_code(wd, url, code)
    finally:
        time.sleep(100)

