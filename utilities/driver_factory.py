from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.firefox.service import Service as FireFox_Service
from selenium.webdriver.edge.service import Service as Edge_Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.options import Options


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id: int, is_headless=True):

        if int(driver_id) == DriverFactory.CHROME:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument('--disable-dev-shm-usage')
                chrome_options.add_argument("--window-size=1920x1080")
            driver = Chrome(service=Chrome_Service(ChromeDriverManager().install()), options=chrome_options)

        elif int(driver_id) == DriverFactory.FIREFOX:
            driver = Firefox(service=FireFox_Service(GeckoDriverManager().install()))

        elif int(driver_id) == DriverFactory.EDGE:
            driver = Edge(service=Edge_Service(EdgeChromiumDriverManager().install()))

        else:
            driver = Chrome(service=Chrome_Service(ChromeDriverManager().install()))

        return driver
