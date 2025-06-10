# sf.py

import chromedriver_autoinstaller

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, UnexpectedAlertPresentException, NoSuchElementException, NoAlertPresentException

def web_driver(headless=False, proxy=None):
    #chromedriver_autoinstaller.install()  # Automatically installs the latest version of ChromeDriver
    
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument("--incognito")  # 👈 This enables incognito mode
    options.add_argument('--no-sandbox')
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Optional but helps in some cases
        options.add_argument('--disable-dev-shm-usage')  # Prevents shared memory issues in Docker, WSL, etc.
    
    if proxy:
        if proxy.startswith('http://') or proxy.startswith('https://'):
            options.add_argument(f'--proxy-server={proxy}')
        else:
            options.add_argument(f'--proxy-server=https://{proxy}')
    
    #options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)
    return driver