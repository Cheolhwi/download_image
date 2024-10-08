import os
import sys
import signal
import time
from login import main as login_main
from twitter import get_media_images
from webdriver_manager.chrome import ChromeDriverManager
from threading import Event
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import subprocess
import shutil

# Global flag to control thread termination
terminate_event = Event()
COOKIE_MAX_AGE = 7 * 24 * 60 * 60  # One week in seconds


def check_and_download_chromedriver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless=new")

        # Specify the correct version of chromedriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.quit()
    except OSError as e:
        # Check if the error is related to WinError 193
        if "[WinError 193]" in str(e):
            print("OSError: [WinError 193] encountered. Attempting to clear WebDriver folder and retry.")

            try:
                # Get the WebDriver installation path
                webdriver_path = ChromeDriverManager().install()
                webdriver_dir = os.path.dirname(webdriver_path)

                # Clear the WebDriver folder
                shutil.rmtree(webdriver_dir)  # Remove the folder and all its contents
                print(f"Cleared WebDriver folder at: {webdriver_dir}")

                # Retry the WebDriver installation
                service = Service(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service, options=chrome_options)
                driver.quit()

                print("ChromeDriver setup succeeded after retry.")
            except Exception as retry_error:
                print(f"Failed to clear or reinstall WebDriver: {retry_error}")
                sys.exit(1)
        else:
            print(f"An error occurred while checking or downloading chromedriver: {e}")
            sys.exit(1)

def check_cookie_file_age(cookies_file):
    """Check if the cookie file is older than a week and delete if necessary."""
    if os.path.exists(cookies_file):
        file_mod_time = os.path.getmtime(cookies_file)
        current_time = time.time()

        # If the file is older than one week, delete it and prompt the user to log in
        if current_time - file_mod_time > COOKIE_MAX_AGE:
            print(f"Cookies file is older than one week. Deleting {cookies_file} and requiring a new login.")
            os.remove(cookies_file)
            return False
        else:
            print("Cookies file is up-to-date.")
            return True
    else:
        return False

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

    # Download or update chromedriver
    check_and_download_chromedriver()

    # Check if cookies file exists and is still valid
    if not check_cookie_file_age(cookies_file):
        print("Cookies file not found or too old. Please login first.")
        login_main()

    while not terminate_event.is_set():
        try:
            username = input("Enter the download username: ")
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
