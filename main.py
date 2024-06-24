# main.py
import os
import sys
from login import main as login_main
from twitter import get_media_images
from webdriver_manager.chrome import ChromeDriverManager


def check_and_download_chromedriver():
    try:
        # Attempt to locate chromedriver automatically
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.quit()
    except Exception as e:
        print(f"An error occurred while checking or downloading chromedriver: {e}")
        sys.exit(1)


def main():
    cookies_file = 'twitter_cookies.pkl'
    base_folder_path = 'downloaded_images'

    # Check and create base folder if it doesn't exist
    if not os.path.exists(base_folder_path):
        os.makedirs(base_folder_path)
        print(f"Created folder: {base_folder_path}")

    check_and_download_chromedriver()

    if not os.path.exists(cookies_file):
        print("Cookies file not found. Please login first.")
        login_main()

    username = input("Enter the download username: ")
    image_urls = get_media_images(username, cookies_file, base_folder_path)
    print(f"Downloaded {len(image_urls)} images for user {username}")


if __name__ == "__main__":
    main()
