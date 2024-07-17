import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import csv
from pytube import YouTube 
from concurrent.futures import ThreadPoolExecutor
from selenium.common.exceptions import NoSuchElementException


def read_video_ids_from_csv(csv_file, column_name):
    video_ids = []
    with open(csv_file, 'r', newline='',encoding="utf8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row:
                video_ids.append('https://www.youtube.com/watch?v='+row[column_name])
    return video_ids


# Function to watch a YouTube video
def watch_video(driver, video_url):
    yt = YouTube(video_url)  ## this creates a YOUTUBE OBJECT
    video_length = yt.length 
    if (video_length>300):
        video_length=300
    print('watching video',video_url)
    driver.get(video_url)
    time.sleep(10)
    try:
        a=driver.find_elements(By.CLASS_NAME,"yt-spec-button-shape-next")
        for i in a: 
            if (i.get_attribute('aria-label')=="Accept the use of cookies and other data for the purposes described"):
                i.click()
                print("clicked on consent")
                time.sleep(2)
                break
    except NoSuchElementException:
        print("Element not found")
   
    time.sleep(video_length)
     

def main():
    print('Starting Collection')
    csv_file = 'Conspiracy_Videos.csv'
    column_name = 'Video ID'
    video_urls = read_video_ids_from_csv(csv_file, column_name)
    print(video_urls)
    # Set up Chrome WebDriver
    # Path to your Chrome extension ZIP file
    extension_zip1 = './P1-100746920764406569411.zip'
    extension_zip2='./P2-111127828278706392511.zip'
    extension_zip3='./P3-111975351413476172549.zip'
    extension_zip4='./P4-105993388413215169490.zip'

    # Initialize the Chrome WebDriver with extension 
    #Profile 1 #100746920764406569411
    chrome_options1 = webdriver.ChromeOptions()
    chrome_options1.add_extension(extension_zip1)
    chrome_options1.add_argument("--start-maximized")  # Maximize the browser window
    chrome_options1.add_argument('--lang=en-US')
    chrome_options1.add_argument('--headless=new')
    chrome_options1.add_argument("--window-size=1920,1080")
    chrome_options1.add_argument("--allow-insecure-localhost")
    chrome_options1.add_argument("--disable-gpu")
    chrome_options1.add_argument("--no-sandbox")
    chrome_prefs1 = {
    "intl.accept_languages": "en,en_US"
    }
    chrome_options1.add_experimental_option("prefs", chrome_prefs1)
    driver1 = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options1)
    # Open Google and sign in
    url = 'https://www.google.com/accounts/Login'
    driver1.get(url)
    time.sleep(2)
    driver1.find_element(By.ID,"identifierId").send_keys('janedoe170171@gmail.com')
    time.sleep(2)
    driver1.find_element(By.ID,"identifierNext").click()
    time.sleep(2)
    driver1.find_element(By.NAME,"Passwd").send_keys('MissFemalePersona1')
    time.sleep(2)
    driver1.find_element(By.ID,"passwordNext").click()
    time.sleep(2)
    print('profile 1 logged in')
 

    # #Profile 2 # 111127828278706392511
    chrome_options2 = webdriver.ChromeOptions()
    chrome_options2.add_extension(extension_zip2)
    chrome_options2.add_argument("--start-maximized")  # Maximize the browser window
    chrome_options2.add_argument('--lang=en-US')
    chrome_options2.add_argument('--headless=new')
    chrome_options2.add_argument("--window-size=1920,1080")
    chrome_options2.add_argument("--allow-insecure-localhost")
    chrome_options2.add_argument("--disable-gpu")
    chrome_options2.add_argument("--no-sandbox")
    chrome_prefs2 = {
    "intl.accept_languages": "en,en_US"
    }
    chrome_options2.add_experimental_option("prefs", chrome_prefs2)
    driver2 = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options2)
    # Open Google and sign in
    url = 'https://www.google.com/accounts/Login'
    driver2.get(url)
    time.sleep(2)
    driver2.find_element(By.ID,"identifierId").send_keys('jhondoe170171@gmail.com')
    time.sleep(2)
    driver2.find_element(By.ID,"identifierNext").click()
    time.sleep(2)
    driver2.find_element(By.NAME,"Passwd").send_keys('MissMalePersona2')
    time.sleep(2)
    driver2.find_element(By.ID,"passwordNext").click()
    time.sleep(2)
    print('profile 2 logged in')

    # #Profile 3 #111975351413476172549
    chrome_options3 = webdriver.ChromeOptions()
    chrome_options3.add_extension(extension_zip3)
    chrome_options3.add_argument("--start-maximized")  # Maximize the browser window
    chrome_options3.add_argument('--lang=en-US')
    chrome_options3.add_argument('--headless=new')
    chrome_options3.add_argument("--window-size=1920,1080")
    chrome_options3.add_argument("--allow-insecure-localhost")
    chrome_options3.add_argument("--disable-gpu")
    chrome_options3.add_argument("--no-sandbox")
    chrome_prefs3 = {
    "intl.accept_languages": "en,en_US"
    }
    chrome_options3.add_experimental_option("prefs", chrome_prefs3)
    driver3 = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options3)
    # Open Google and sign in
    url = 'https://www.google.com/accounts/Login'
    driver3.get(url)
    time.sleep(2)
    driver3.find_element(By.ID,"identifierId").send_keys('jhondoe180181@gmail.com')
    time.sleep(2)
    driver3.find_element(By.ID,"identifierNext").click()
    time.sleep(2)
    driver3.find_element(By.NAME,"Passwd").send_keys('FactMalePersona2')
    time.sleep(2)
    driver3.find_element(By.ID,"passwordNext").click()
    time.sleep(2)
    print('profile 3 logged in')

    # #Profile 4 #105993388413215169490
    chrome_options4 = webdriver.ChromeOptions()
    chrome_options4.add_extension(extension_zip4)
    chrome_options4.add_argument("--start-maximized")  # Maximize the browser window
    chrome_options4.add_argument('--lang=en-US')
    chrome_options4.add_argument('--headless=new')
    chrome_options4.add_argument("--window-size=1920,1080")
    chrome_options4.add_argument("--allow-insecure-localhost")
    chrome_options4.add_argument("--disable-gpu")
    chrome_options4.add_argument("--no-sandbox")
    chrome_prefs4 = {
    "intl.accept_languages": "en,en_US"
    }
    chrome_options4.add_experimental_option("prefs", chrome_prefs4)
    driver4 = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options4)
    # Open Google and sign in
    url = 'https://www.google.com/accounts/Login'
    driver4.get(url)
    time.sleep(2)
    driver4.find_element(By.ID,"identifierId").send_keys('jhondoe180181@gmail.com')
    time.sleep(2)
    driver4.find_element(By.ID,"identifierNext").click()
    time.sleep(2)
    driver4.find_element(By.NAME,"Passwd").send_keys('FactMalePersona2')
    time.sleep(2)
    driver4.find_element(By.ID,"passwordNext").click()
    time.sleep(2)
    print('profile 4 logged in')

    drivers = [driver1,driver2,driver3,driver4]
    num_drivers = len(drivers)
    
    with ThreadPoolExecutor(max_workers=num_drivers) as executor:
        futures = [executor.submit(watch_videos,drivers, drivers[i], video_urls) for i in range(num_drivers)]

        # Wait for all futures to complete
        for future in futures:
            future.result()

    # Quit all drivers
    for driver in drivers:
        driver.quit()

  


def watch_videos(drivers,driver, video_urls):
    try:
        for video_url in video_urls:
            watch_video(driver, video_url)
            print("Watched video:",video_url,"profile:",drivers.index(driver))
    except Exception as e:
         print("An error occurred:", str(e))
    finally:
         driver.quit()

if __name__ == "__main__":
    main()
