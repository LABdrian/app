from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os 
import const as c 

class CSVDownloader:
    def __init__(self, url=c.url, downloads_dir=c.downloads_dir):
        

        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("prefs", c.prefs)
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        #self.chrome_options.add_argument("--headless")

        self.driver = webdriver.Remote(
            command_executor=c.command_executor,
            options=self.chrome_options
        )
        self.url = c.url
        self.downloads_dir = c.downloads_dir


    def enable_download_in_headless_chrome(self):
        self.driver.command_executor._commands["send_command"] = c.session_command_tuple
        session_command_params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': self.downloads_dir}}
        self.driver.execute("send_command", session_command_params)

    def open_web_page(self):
        self.driver.get(self.url)


    def navigate(self, selector):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )
            element.click()
        except TimeoutException:
            print(f"Elemento con selector '{selector}' no encontrado o no visible.")

    def select_option_from_opened_dropdown(self, option_text):
        try:
  
            time.sleep(1) 
            option_to_select = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f"//nb-option[contains(text(), '{option_text}')]"))
            )

            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"//nb-option[contains(text(), '{option_text}')]"))
            )
            option_to_select.click()
        except TimeoutException:
            print(f"Timeout: La opción con texto '{option_text}' no se encontró o no está visible.")
        except StaleElementReferenceException:
            print(f"El elemento ya no está adjunto al DOM o ha sido recreado.")


    def close_browser(self):
        self.driver.quit()

    @staticmethod
    def execute():
        downloader = CSVDownloader(c.url)
        downloader.open_web_page()
        downloader.navigate(c.doc_down)
        downloader.navigate(c.tables_list)
        downloader.select_option_from_opened_dropdown(c.table) 
        downloader.navigate(c.years_list)
        downloader.select_option_from_opened_dropdown(c.year)
        downloader.navigate(c.locations_list)
        downloader.select_option_from_opened_dropdown(c.location)
        downloader.navigate(c.download)
        downloader.enable_download_in_headless_chrome()
        time.sleep(10) 

   
        downloaded_files = os.listdir('./downloads')
        if downloaded_files:
            print("Archivos descargados:", downloaded_files)
        else:
            print("No se encontraron archivos descargados.")
            
        downloader.close_browser()


CSVDownloader.execute()


