from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 初始化浏览器
def login(when):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/Users/chenhaihong/Library/Application Support/Google/Chrome")
    options.add_argument("profile-directory=Profile 3")
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        driver.get("https://gym.sysu.edu.cn/#/")

        shenzhen = WebDriverWait(driver, 20).until(#这里是找到深圳校区对应XPATH
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/section[1]/div/div[4]/h3'))
        )
        shenzhen.click()
        
        time.sleep(1)
        gym = WebDriverWait(driver, 20).until(#这里是找到健身房对应XPATH
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div[4]/div[4]'))
        )
        gym.click()
        
        time.sleep(1)
        day_after_tomorrow = WebDriverWait(driver, 20).until(#观察发现，最多可以预约到后天的时间，//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[3]/div[3]就是后天的XPATH
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[3]/div[3]'))
        )
        day_after_tomorrow.click()

        if when == 'T1416':
            T1416 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[2]/button'))
            )
            T1416.click()

        elif when == 'T1618':
            T1618 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[2]/td[2]/button'))
            )
            T1618.click()
        
        elif when == 'T1820':
            T1820 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[3]/td[2]/button'))
            )
            T1820.click()
        
        elif when == 'T2022':
            T2022 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[4]/td[2]/button'))
            )

    except Exception as e:
        driver.save_screenshot('/Users/chenhaihong/DOC/Github/GYM_AutoReserve/error.png')
        print(f"最终点击失败: {str(e)}")
        with open("page.html", "w") as f:
            f.write(driver.page_source)

if __name__ == "__main__":
    day = input("预约时间：")
    if day == 'T1416':
        login('T1416')
    elif day == 'T1618':
        login('T1618')
    elif day == 'T1820':
        login('T1820')
    elif day == 'T2022':
        login('T2022')
    else:
        print("输入错误")