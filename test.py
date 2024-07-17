from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

# Replace with the path to your WebDriver
video_url = 'https://www.youtube.com/watch?v=si-vMj-FB88'

chrome_options1 = webdriver.ChromeOptions()
chrome_options1.add_argument('--lang=en-US')
chrome_options1.add_argument('--headless=new')

chrome_prefs1 = {
    "intl.accept_languages": "en,en_US"
    }
chrome_options1.add_experimental_option("prefs", chrome_prefs1)
driver = webdriver.Chrome(options=chrome_options1)

driver.get(video_url)
time.sleep(5)
#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.eom-buttons.style-scope.ytd-consent-bump-v2-lightbox > div:nth-child(1) > ytd-button-renderer:nth-child(2) > yt-button-shape > button
try:
    a=driver.find_elements(By.CLASS_NAME,"yt-spec-button-shape-next")
    for i in a: 
        if (i.get_attribute('aria-label')=="Accept the use of cookies and other data for the purposes described"):
            i.click()
            time.sleep(2)
            break

except NoSuchElementException:
    print("Element not found")
time.sleep(5)
print("To click on settings button")
driver.find_element(By.CLASS_NAME,"ytp-settings-button").click()
time.sleep(3)
data = driver.find_elements(By.CLASS_NAME,"ytp-menuitem > .ytp-menuitem-label")
for d in data:
    text=d.text
    if text=="Playback speed" :
        d.click()
        data1=driver.find_elements(By.CLASS_NAME,"ytp-menuitem > .ytp-menuitem-label")
        for da in data1:
            if da.text=="2":
                da.click()
                print('speed changed')
                time.sleep(5)
                break
        break


#print(data)
# print("To click on quality button")
# driver.find_element(By.CLASS_NAME,"ytp-menuitem:nth-child(4) > .ytp-menuitem-label").click()
# time.sleep(3)
# resoultion = driver.find_element(By.CLASS_NAME,"ytp-menuitem:nth-child(5) > .ytp-menuitem-label").text
# print(resoultion)
# print("to click on 240p resolution")
# driver.find_element(By.CLASS_NAME,"ytp-menuitem:nth-child(5) > .ytp-menuitem-label").click()
# time.sleep(3)

# Keep the browser open to watch the video
driver.quit()
