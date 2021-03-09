import random
from urllib.parse import unquote
from time import sleep

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, NoSuchWindowException, \
    WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from scrape_emails import EmailScraper


class Yelp:
    window = None
    second_window = None
    window: Chrome
    results_elems = None
    # XPATHS
    search_input = '//input[@id="search_description"]'
    results_loading_div = '//div[contains(@class, "loading-wrapper_")]'
    detailed_loading_div = '//div[contains(@class, "mainColumnSection-spacing")]'
        # RESULTS
    results = '//li/div[contains(@class,"container__")]'
    result_name = 'div//div[contains(@class,"businessName_")]//h4/span/a'
    result_review = 'div//span[contains(@class, "reviewCount_")]'
    result_category = 'div//div[contains(@class, "priceCategory_")]/div//span/span/span/a'
    result_verfied_license = 'div//div[contains(@class, "verifiedLicenseTextBadgeContainer_")]'    # not found for all results
        # PAGINATOR
    paginator = '//li//div[contains(@class,"pagination-links")]'
    pages_links = f'{paginator}/div[contains(@class,"pagination-link-container")]//a/div'
    current_page = f'{paginator}/div[contains(@class,"pagination-link-container")]/span[not(a)]/span'   # nav link that has no "a" tag is the current page
    next_page = f'{paginator}/div[contains(@class,"navigation-button-container")][2]'
    next_page_disabled = f'{paginator}/div[contains(@class,"navigation-button-container")][2]//span[contains(@class, "navigation-button-icon--disabled")]'
    # total_pages_text = '//li/div[contains(@class,"pagination")]/div[2]/span'  # "1 of 24"
        # DETAIL INFO
    phone = '//p[contains(text(), "Phone number")]/following-sibling::p'
    website = '//p[contains(text(), "Business website")]/following-sibling::p/a'
    address = '//p/a[contains(@href, "/map/")]/following-sibling::p'
    open_hours = '//a[contains(@class, "editCategories_")]/following-sibling::div/div/div/div/span/following-sibling::span/span'

    @classmethod
    def open(cls):
        cls.window = Chrome(ChromeDriverManager().install())
        test = 'https://www.yelp.com/search?find_desc=real%20estate&find_loc=San%20Francisco%2C%20CA'
        yelp = "https://www.yelp.com"
        cls.window.get(yelp)
        return True

    @classmethod
    def is_browser_opened(cls, window_check_var):
        if window_check_var is not None:
            try:
                print(window_check_var.current_window_handle)
                return True
            except NoSuchWindowException and WebDriverException:
                return False
        else:
            return False

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
    def _extract_url(cls, href_content: str):
        start = href_content.index("?url=")
        end = href_content.index("&")
        url_quote = href_content[start:end].replace("?url=", "")
        return unquote(url_quote)

    @classmethod
    def move_to_page(cls, page: int):
        paginate_links = cls.window.find_elements_by_xpath(cls.pages_links)
        for link in paginate_links:
            if link.text == str(page):
                link.click()
                # WAIT FOR PAGE TO START LOADING
                WebDriverWait(cls.window, 60).until(
                    ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))
                # WAIT FOR LOADING TO FINISH
                WebDriverWait(cls.window, 60).until_not(
                    ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))
                return True
        # IF REACHED HERE, THAT MEANS THE TARGET PAGE DOESN'T EXISTS IN THE LINKS
        # SO I WILL NEED TO CLICK THE LAST AVAILABLE PAGE TO SHOW OTHERS
        paginate_links[-1].click()
        # WAIT FOR PAGE TO START LOADING
        WebDriverWait(cls.window, 60).until(
            ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))
        # WAIT FOR LOADING TO FINISH
        WebDriverWait(cls.window, 60).until_not(
            ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))
        # RECURSIVE
        cls.move_to_page(page)

    @classmethod
    def click_next_page(cls):
        # CHECK IF NEXT PAGE BUTTON ENABLED
        try:
            cls.window.find_element_by_xpath(cls.next_page_disabled)
            return False
        except NoSuchElementException:
            cls.window.find_element_by_xpath(cls.next_page).click()
            # WAIT FOR PAGE TO START LOADING
            WebDriverWait(cls.window, 10).until(
                ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))
            # WAIT FOR LOADING TO FINISH
            WebDriverWait(cls.window, 60).until_not(
                ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))

    @classmethod
    def scrape_results(cls):
        """
        return False if results page doesn't exists
        return list of lists "records"
        """
        # WAIT FOR PAGE LOADING
        WebDriverWait(cls.window, 60).until_not(ec.visibility_of_element_located((By.XPATH, cls.results_loading_div)))
        # CHECK IF RESULTS PAGE EXISTS
        try:
            search_keyword = cls.get_search_keyword()
            page = cls.window.find_element_by_xpath(cls.current_page).text
        except NoSuchElementException:
            return False
        results = cls.window.find_elements_by_xpath(cls.results)
        cls.results_elems = results

        records = []
        for result in results:
            # SCRAPING THE DATA
            name = result.find_element_by_xpath(cls.result_name).text
            try:
                reviews = int(result.find_element_by_xpath(cls.result_review).text)
            except NoSuchElementException:
                reviews = 0
            try:
                result.find_element_by_xpath(cls.result_verfied_license)
                verfied = 1
            except NoSuchElementException:
                verfied = 0
            url = result.find_element_by_xpath(cls.result_name).get_attribute("href")
            # RECORD DATA STRUCTURE
            record = [name, reviews, verfied, search_keyword, page, url]
            records.append(record)
        return records

    @classmethod
    def scrape_result_details(cls, url: str):
        """
        this method opens the url in a new tab and scrape the data then returns a list object
        """
        cls.window: Chrome
        # OPENING THE URL IN A NEW TAB
        cls.window.execute_script(f'''window.open("{url}", "_blank");''')
        sleep(1)
        cls.window.switch_to.window(cls.window.window_handles[-1])
        sleep(2)
        # EXPLICTLY WAIT FOR PAGE TO LOAD
        WebDriverWait(cls.window, 60).until(ec.visibility_of_element_located((By.XPATH, '//a[contains(@class, "logo-link_")]')))
        # WAIT FOR PAGE LOADING
        WebDriverWait(cls.window, 60).until_not(ec.visibility_of_element_located((By.XPATH, cls.detailed_loading_div)))
        # WEBSITE SCRAPING
        try:
            website_href_code = cls.window.find_element_by_xpath(cls.website).get_attribute("href")
            website = cls._extract_url(website_href_code)
        except NoSuchElementException:
            website = "---"
        # EMAIL SCRAPING
        if website != "---":
            email = EmailScraper.scrape_website(website)
            if email is False:
                email = "---"
        else:
            email = "---"
        # PHONE SCRAPING
        try:
            phone = cls.window.find_element_by_xpath(cls.phone).text
        except NoSuchElementException:
            phone = "---"
        # ADDRESS SCRAPING
        try:
            address = cls.window.find_element_by_xpath(cls.address).text
        except NoSuchElementException:
            address = "---"
        # OPEN HOURS SCRAPING
        try:
            open_hours = cls.window.find_element_by_xpath(cls.open_hours).text
        except NoSuchElementException:
            open_hours = "---"
        # CLOSING THE TAB AND GETTING BACK TO RESULTS PAGE
        cls.window.close()
        sleep(1)
        cls.window.switch_to.window(cls.window.window_handles[0])
        # DELAY: BREAKING BOT PATTERN
        sleep(random.randint(2, 6))
        record = [email, phone, website, address, open_hours]
        return record

    @classmethod
    def scrape_result_details2(cls, url: str):
        if not cls.is_browser_opened(cls.second_window):
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1200,1100")
            cls.second_window = Chrome(ChromeDriverManager().install(), options=options)
        cls.second_window.get(url)
        # EXPLICTLY WAIT FOR PAGE TO LOAD
        WebDriverWait(cls.second_window, 60).until(
            ec.visibility_of_element_located((By.XPATH, '//a[contains(@class, "logo-link_")]')))
        # WAIT FOR PAGE LOADING
        WebDriverWait(cls.second_window, 60).until_not(ec.visibility_of_element_located((By.XPATH, cls.detailed_loading_div)))
        # WEBSITE SCRAPING
        try:
            website_href_code = cls.second_window.find_element_by_xpath(cls.website).get_attribute("href")
            website = cls._extract_url(website_href_code)
        except NoSuchElementException:
            website = "---"
        # EMAIL SCRAPING
        if website != "---":
            email = EmailScraper.scrape_website(website)
            if email is False or email is None or email == "":
                email = "---"
        else:
            email = "---"
        # PHONE SCRAPING
        try:
            phone = cls.second_window.find_element_by_xpath(cls.phone).text
        except NoSuchElementException:
            phone = "---"
        # ADDRESS SCRAPING
        try:
            address = cls.second_window.find_element_by_xpath(cls.address).text
        except NoSuchElementException:
            address = "---"
        # OPEN HOURS SCRAPING
        try:
            open_hours = cls.second_window.find_element_by_xpath(cls.open_hours).text
        except NoSuchElementException:
            open_hours = "---"
        # DELAY: BREAKING BOT PATTERN
        sleep(random.randint(2, 6))
        record = [email, phone, website, address, open_hours]
        return record
