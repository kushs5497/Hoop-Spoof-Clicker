# auto_ref.py
import sf
import time
import random
import requests
import subprocess
import chromedriver_autoinstaller
from proxy import get_proxy, init_proxies

def automate_referal():
    driver = sf.web_driver(headless=False, proxy=None)

    # run mullvad relay set location us
    subprocess.run(['mullvad', 'connect'])

    link = 'https://hoop.photo/share/2CssJm5wh6evkp8SvHOFSETrMMV2'
    link = 'https://hoop.photo/share/2CssJm5wh6evkp8SvHOFSETrMMV2'
    apple_XPATH = '//*[@id="store-button"]/a[1]/img'
    gplay_XPATH = '//*[@id="store-button"]/a[2]/img'
    refresh_count = 2
    store_click_count = 2

    # Open the link refresh_count times and press each store button store_click_count times
    print(f"Opening link: {link} and refreshing {refresh_count} times.")
    for _ in range(refresh_count):
        time.sleep(random.uniform(0, 1)) 
        driver.get(link)

    print(f"Clicking store buttons {store_click_count} times each.")
    for _ in range(store_click_count):
        time.sleep(random.uniform(0, 1)) 
        try:
            apple_button = driver.find_element('xpath', apple_XPATH)
            apple_button.click()
        except (sf.StaleElementReferenceException, sf.NoSuchElementException):
            print("Apple button not found or stale, retrying...")
            continue
        time.sleep(random.uniform(0, 1)) 
        try:
            gplay_button = driver.find_element('xpath', gplay_XPATH)
            gplay_button.click()
        except (sf.StaleElementReferenceException, sf.NoSuchElementException):
            print("Google Play button not found or stale, retrying...")
            continue

    driver.quit()

    

subprocess.run(['mullvad', 'disconnect'])
chromedriver_autoinstaller.install()

for _ in range(1):  # Run the automation 5 times
    subprocess.run(['mullvad', 'connect'])
    time.sleep(random.uniform(0, 1)) 
    automate_referal()
    time.sleep(random.uniform(0, 1)) 
    subprocess.run(['mullvad', 'disconnect'])
    time.sleep(random.uniform(3, 7))  # Sleep for a random time between 1-2 minutes
    
