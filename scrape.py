from selenium.webdriver.common.by import By
from webdriver import create_webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

base_url = 'https://utexas.app.box.com/s/evo96v5md4r8nooma3z17kcnfjzp2wed?page='





def scrape_page(driver, page_n=1, delay_between_downloads=60):
    """
    Scrapes one page of this Box page.
    """

    driver.get(base_url + str(page_n))
    time.sleep(5)
    folder_divs = driver.find_elements(by=By.CLASS_NAME, value='item-name')
    time.sleep(5)
    from selenium.webdriver import ActionChains
    for idx, folder_div in enumerate(folder_divs):
        # scroll_shim is just scrolling the element into view, you still need to hover over it to click using an action chain.
        if 'firefox' in driver.capabilities['browserName']:
            if idx >= 13: # For the first elements scrolling overshoots, so we just do it when needed.
                driver.execute_script("arguments[0].scrollIntoView(true);", folder_div)
                time.sleep(1)
        action = ActionChains(driver)
        action.context_click(folder_div).perform()
        driver.find_elements(by=By.CLASS_NAME, value='DownloadMenuItem')[0].click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(driver.find_elements(by=By.CLASS_NAME, value='modal-close-button')[0])).click()
        #driver.find_elements(by=By.CLASS_NAME, value='modal-close-button')[0].click()
        print('Started download: ' + folder_div.text)
        time.sleep(delay_between_downloads)


if __name__ == '__main__':
    driver = create_webdriver()
    time.sleep(5)
    for page_n in range(1,88):
        print("Page:", page_n)
        scrape_page(driver, page_n=page_n)