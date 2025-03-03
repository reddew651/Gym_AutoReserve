from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# 初始化浏览器（Chrome示例）
def login(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/Users/chenhaihong/Library/Application Support/Google/Chrome")
    options.add_argument("profile-directory=Profile 3")
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://tiyu.sysu.edu.cn/")
    
    try:
        # 点击目标链接
        link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="block-block-7"]/div/p[1]/a'))
        )
        link.click()

        # 切换到新窗口（如果有）
        time.sleep(2)
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])

        # 输入账号密码
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

        # 提交登录
        driver.find_element(By.XPATH, '//*[@id="fm1"]/section[2]/input[4]').click()

        link2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/section[1]/div/div[4]/h3'))
        )
        link2.click()

        link3 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div[4]/div[4]'))
        )
        link3.click()
        
        one = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[3]/div[2]'))
        )
        one.click()

        one1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[3]/td[2]/button'))
        )
        one1.click()

        # 等待登录完成
        time.sleep(5)
        print("登录流程已完成")

    finally:
        if input("是否关闭浏览器？（y/n）") == 'y':
            driver.quit()
        else:
            print("浏览器未关闭")

# 使用示例（替换为实际账号密码）
if __name__ == "__main__":
    
    login("chenhh93", "Chh-651-zsdx")