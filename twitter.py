import os
import sys
import requests
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Event

def load_cookies(driver, cookies_file):
    with open(cookies_file, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

def download_image(url, folder_path, image_name, stop_event):
    if stop_event.is_set():
        return
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # 检查图片大小
        if int(response.headers.get('content-length', 0)) < 100 * 1024:  # 100 KB
            print(f"Image {image_name} is less than 100KB, skipping download.")
            return
        with open(os.path.join(folder_path, image_name), 'wb') as file:
            for chunk in response.iter_content(1024):
                if stop_event.is_set():
                    break
                file.write(chunk)

def download_images_concurrently(image_urls, user_folder_path, stop_event):
    total_images = len(image_urls)
    with ThreadPoolExecutor(max_workers=3) as executor:  # 限制为3个线程
        futures = [executor.submit(download_image, img_url, user_folder_path, f'image_{idx + 1}.jpg', stop_event) for idx, img_url in enumerate(image_urls)]
        for future in tqdm(as_completed(futures), desc="Progress", unit="image", total=total_images):
            try:
                future.result()
            except Exception as e:
                print(f"Error downloading image: {e}")

def parse_page_source(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    image_urls = set()
    for img in soup.find_all('img', {'src': True}):
        src = img['src']
        if 'pbs.twimg.com/media' in src:
            high_res_src = src.replace('name=medium', 'name=4096x4096')
            high_res_src = high_res_src.replace('name=small', 'name=4096x4096')
            high_res_src = high_res_src.replace('name=360x360', 'name=4096x4096')
            image_urls.add(high_res_src)
    return image_urls

def get_media_images(username, cookies_file, base_folder_path, stop_event):
    url = f'https://x.com/{username}/media'

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get('https://x.com/login')
        load_cookies(driver, cookies_file)
        driver.refresh()

        print("Page loading, please wait", end="", flush=True)
        driver.get(url)

        while not stop_event.is_set():
            time.sleep(0.5)
            print(".", end="", flush=True)
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "img"))
                )
                break
            except:
                continue

        if stop_event.is_set():
            return []

        print("\nPage loaded, starting to parse the content.")

        all_image_urls = set()
        page_sources = []

        scroll_pause_time = 1
        scroll_attempts = 0
        max_scroll_attempts = 20
        last_height = driver.execute_script("return document.body.scrollHeight")

        while scroll_attempts < max_scroll_attempts and not stop_event.is_set():
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                scroll_attempts += 1
            else:
                scroll_attempts = 0
            last_height = new_height

            page_sources.append(driver.page_source)

        if stop_event.is_set():
            return []

        with ThreadPoolExecutor(max_workers=3) as executor:  # 限制为3个线程
            futures = [executor.submit(parse_page_source, page_source) for page_source in page_sources]
            for future in tqdm(as_completed(futures), desc="Parsing", unit="page", total=len(page_sources)):
                try:
                    all_image_urls.update(future.result())
                except Exception as e:
                    print(f"Error parsing page source: {e}")

        user_folder_path = os.path.join(base_folder_path, username)
        if not os.path.exists(user_folder_path):
            os.makedirs(user_folder_path)

        print("Downloading images:")
        download_images_concurrently(all_image_urls, user_folder_path, stop_event)

    finally:
        driver.quit()

    return list(all_image_urls)
