from selenium.webdriver.common.by import By
from webdriver import create_webdriver
import time

base_url = 'https://utexas.app.box.com/s/evo96v5md4r8nooma3z17kcnfjzp2wed?page='

def scrape_page(driver, page_n=1, delay_between_downloads=60):
    """
    Scrapes one page of this Box page.
    """
    
    driver.get(base_url + str(page_n))

    folder_divs = driver.find_elements(by=By.CLASS_NAME, value='item-name')

    from selenium.webdriver import ActionChains
    for folder_div in folder_divs:
        action = ActionChains(driver)
        action.context_click(folder_div).perform()
        driver.find_elements(by=By.CLASS_NAME, value='DownloadMenuItem')[0].click()
        driver.find_elements(by=By.CLASS_NAME, value='modal-close-button')[0].click()
        print('Started download: ' + folder_div.text)
        time.sleep(delay_between_downloads)


if __name__ == '__main__':
    driver = create_webdriver()
    for page_n in range(1,88):
        scrape_page(driver, page_n=page_n)