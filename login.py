import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def login_to_twitter(driver):
    driver.get('https://x.com/login')
    # 等待用户登录完成，直到跳转到主页
    WebDriverWait(driver, 300).until(
        EC.url_to_be('https://x.com/home')
    )

def save_cookies(driver, cookies_file):
    with open(cookies_file, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)

def main():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        login_to_twitter(driver)
        save_cookies(driver, 'twitter_cookies.pkl')
    finally:
        driver.quit()

    print("Cookies have been saved to twitter_cookies.pkl")

if __name__ == "__main__":
    main()
