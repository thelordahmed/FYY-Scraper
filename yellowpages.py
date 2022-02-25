import os
import random
from threading import Thread
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

# this class is a bit different than the Yelp
# in the yelp class, I need to go in each result page to scrape the details data
# but here in yellowpages, I can scrape the data from outside in the results search page

class YellowPages:
    window = None
    window: Chrome
    pages = None
    state = "idle"
    search_input = '//input[@id="query"]'
    # DOESN'T INCLUDE NEXT OR PREVE OR CURRENT PAGE LINK
    available_pages_links = '//div[@class="pagination"]/ul/li[a[not(@class)]]/a'
    results_loading_div = '//div[@class="srp-ajax-overlay" and @style]'
    next_page = '//div[@class="pagination"]//a[@class="next ajax-page"]'
    current_page = '//div[@class="pagination"]//span[@class="disabled"]'
    results = '//div[@class="result"]'
    name = '//a[@class="business-name"]/span'



    @classmethod
    def open(cls):
        win = Chrome(ChromeDriverManager().install())
        # if an element is not located .. will wait 2 seconds before throwing NoSuchElementException
        win.implicitly_wait(2)
        win.set_page_load_timeout(60)
        sleep(1)
        win.get("https://www.yellowpages.com")
        sleep(2)
        cls.window = win

    @classmethod
    def get_search_keyword(cls):
        """
        :return: searching keyword as string, or False if user didn't make search
        """
        try:
            value = cls.window.find_element_by_xpath(cls.search_input).get_attribute("value")
            return value
        except NoSuchElementException:
            return False

    @classmethod
    def get_current_page(cls) -> str:
        return cls.window.find_element_by_xpath(cls.current_page).text

    @classmethod
    def move_to_page(cls, page: int):
        paginate_links = cls.window.find_elements_by_xpath(cls.available_pages_links)
        for link in paginate_links:
            if link.text == str(page):
                cls.window.get(link.get_attribute("href"))
                sleep(random.randint(1, 3))
                return True
        # IF REACHED HERE, THAT MEANS THE TARGET PAGE DOESN'T EXISTS IN THE LINKS
        # SO I WILL NEED TO CLICK THE LAST AVAILABLE PAGE TO SHOW OTHERS
        cls.window.get(paginate_links[-1].get_attribute("href"))
        sleep(random.randint(1, 3))
        # RECURSIVE
        cls.move_to_page(page)


    @classmethod
    def click_next_page(cls):
        # CHECK IF NEXT PAGE BUTTON EXISTS
        try:
            cls.window.find_element_by_xpath(cls.next_page).click()
            # WAIT FOR PAGE TO START LOADING
            try:
                WebDriverWait(cls.window, 5).until(
                    ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))
            except:
                pass
            # WAIT FOR LOADING TO FINISH
            WebDriverWait(cls.window, 60).until_not(
                ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))
        except NoSuchElementException:
            return False

    @staticmethod
    def scrape_email(url):
        # AVOIDING TOO MANY REQUESTS
        sleep(random.randint(2, 6))
        req = requests.get(url)
        if req.ok:
            try:
                soup = BeautifulSoup(req.text, "lxml")
                # BUG FIX .. (DIDN'T TEST IT)
                info_div = soup.select_one("dl")
                email = info_div.find("a", class_="email-business")["href"].replace("mailto:", "")
                # sleep(randint(3, 7))   # added to main code
            except AttributeError and TypeError:
                email = "---"
        else:
            email = "---"
        return email

    @staticmethod
    def scrape_results(page_source):
        """
        returns list of lists - [[name, address, phone, website, url], ...]
        """
        soup = BeautifulSoup(page_source, "lxml")
        soup_list = soup.select('div.search-results.organic > div.result')
        results = []
        for result in soup_list:
            # URL SCRAPING
            url = "https://www.yellowpages.com" + result.find("h2", class_="n").a["href"]
            # NAME SCRAPING
            try:
                name = result.find("h2", class_="n").span.text.strip()
            except AttributeError:
                name = "---"
            # FULL ADDRESS SCRAPING
            try:
                street_address = result.find("div", class_="street-address").text.strip()
            except AttributeError:
                street_address = ""
            try:
                city = result.find("div", class_="locality").text.strip()
            except AttributeError:
                city = ""
            if street_address == "":
                address = city
            else:
                address = street_address + " " + city
            # ----- FOR THE CONVETION OF THE MAIN CLASS LOGIC, NONE VALUE MEANS "---"
            if address == "":
                address = "---"
            # PHONE SCRAPING
            try:
                phone = result.find("div", class_="phones phone primary").text.strip()
            except AttributeError:
                phone = "---"
            # WEBSITE SCRAPING
            try:
                website = result.find("a", class_="track-visit-website")["href"]
            except AttributeError and TypeError:
                website = "---"

            record = [name, address, phone, website, url]
            if record not in results:
                results.append(record)
        return results