from ..items import Product
import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class WoolWorthsSpider(scrapy.Spider):
    def __init__(self):
        self.driver = self.initiate_driver()
    name = 'woolworths'
    allowed_domains = ['woolworths.com.au']
    start_urls = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        self.driver.get(response.url)
        try:
            myElem = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'shelfProductTile-descriptionLink')))
        except TimeoutException:
            print("Loading took too much time!")

        breadcrumbs = '' + self.driver.find_element_by_class_name('breadcrumbs').text
        products_names = [Product(name='' + product_name.text) for product_name in self.driver.find_elements_by_class_name('shelfProductTile-descriptionLink')]
        yield {
            'breadcrumbs':breadcrumbs.split('\n'),
            'products':products_names
        }



    def initiate_driver(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        options = Options()
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                            'notifications': 2, 'auto_select_certificate': 2,
                                                            'fullscreen': 2,
                                                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                            'media_stream_mic': 2, 'media_stream_camera': 2,
                                                            'protocol_handlers': 2,
                                                            'ppapi_broker': 2, 'automatic_downloads': 2,
                                                            'midi_sysex': 2,
                                                            'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                            'metro_switch_to_desktop': 2,
                                                            'protected_media_identifier': 2, 'app_banner': 2,
                                                            'site_engagement': 2,
                                                            'durable_storage': 2}}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")  # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        return webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')