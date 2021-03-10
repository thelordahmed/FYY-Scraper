from threading import Thread
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import math


class YellowPages:
    window = None
    pages = None
    state = "idle"

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
    def get_pages_links(cls):
        """:return a list of all pages links"""
        cur_url = cls.window.current_url
        results_number = int(cls.window.find_element_by_xpath('//div[@class="pagination"]/p').text.replace("We found", "").replace("results", ""))
        pages_number = math.ceil(results_number / 30)  # ceil to get the extra page for orphan results
        pages = []
        for page in range(1, pages_number + 1):
            if "&page=" in cur_url:
                break
            page = cur_url + f"&page={str(page)}"
            pages.append(page)
        return pages

    @staticmethod
    def scrape_data(page_source, scrape_emails=True):
        """
        returns list of lists - [[name, address, phone, email, website], ...]
        """
        soup = BeautifulSoup(page_source, "lxml")
        results_list = soup.select('div.search-results.organic > div.result')
        data = []
        for result in results_list:
            try:
                name = result.find("h2", class_="n").span.text.strip()
            except AttributeError:
                name = "-"

            ##############
            # getting the full address
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
                address = street_address + " - " + city
            # FOR THE CONVETION OF THE MAIN CLASS LOGIC, NONE VALUE MEANS "---"
            if address == "":
                address = "---"
            ##############

            try:
                phone = result.find("div", class_="phones phone primary").text.strip()
            except AttributeError:
                phone = "---"

            try:
                website = result.find("a", class_="track-visit-website")["href"]
            except AttributeError and TypeError:
                website = "---"

            if scrape_emails is True:
                url = "https://www.yellowpages.com" + result.find("h2", class_="n").a["href"]
                req = requests.get(url)
                if req.ok:
                    try:
                        soup = BeautifulSoup(req.text, "lxml")
                        info_div = soup.select_one("div.business-card-footer")
                        email = info_div.find("a", class_="email-business")["href"].replace("mailto:", "")
                        # sleep(randint(3, 7))   # added to main code
                    except AttributeError and TypeError:
                        email = "---"
                else:
                    email = "---"
            else:
                email = "---"

            record = [name, address, phone, email, website]
            if record not in data:
                data.append(record)
        return data