import os
import sys
import signal
from login import main as login_main
from twitter import get_media_images
from webdriver_manager.chrome import ChromeDriverManager
from threading import Event

# Global flag to control thread termination
terminate_event = Event()

def check_and_download_chromedriver():
    try:
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

def signal_handler(sig, frame):
    global terminate_event
    print('\nExiting program.')
    terminate_event.set()
    sys.exit(0)

def main():
    global terminate_event
    signal.signal(signal.SIGINT, signal_handler)
    cookies_file = 'twitter_cookies.pkl'
    base_folder_path = 'downloaded_images'

    if not os.path.exists(base_folder_path):
        os.makedirs(base_folder_path)
        print(f"Created folder: {base_folder_path}")

    check_and_download_chromedriver()

    if not os.path.exists(cookies_file):
        print("Cookies file not found. Please login first.")
        login_main()

    while not terminate_event.is_set():
        try:
            username = input("Enter the download username : ")
            if terminate_event.is_set():
                break
            image_urls = get_media_images(username, cookies_file, base_folder_path, terminate_event)
            if image_urls:
                print(f"Downloaded {len(image_urls)} images for user {username}")
            else:
                print("No images downloaded.")
        except KeyboardInterrupt:
            print("\nExiting program.")
            terminate_event.set()
            sys.exit(0)

if __name__ == "__main__":
    main()
