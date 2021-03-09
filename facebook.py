import random
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import controller




class Facebook:
    window = None
    window: Chrome
    login_form = '//form[contains(@class, "featuredLogin")]'
    ajax_loader = '//div[@aria-busy and @role="progressbar" and @data-visualcompletion="loading-state"]'
    pages_category_btn = '//div[@data-visualcompletion="ignore-dynamic"]/a[contains(@href, "search/pages")]'
    pages_category_btn_active = '//div[@data-visualcompletion="ignore-dynamic"]/a[contains(@href, "search/pages") and @aria-current="page"]'
    search_result_name = '//div[@role="article"]//a[@role="link"]'
    # TO CHECK IF PAGE LOADED OR NOT
    page_about_link = '//div/div/div/a[contains(@href, "/about") and @role="link"]'
    # PAGE DETAILS INFO
    address = '//a[contains(@href, "google.com/maps/dir") and @role="link"]/span/span'
    website = '//div/div/div/div/div/div[2]/div/div/span/span/a[@role="link" and @target="_blank" and @rel="nofollow noopener" and contains(text(), "http") and not(contains(text(), "twitter")) and not(contains(text(), "youtube")) and not(contains(text(), "instagram"))]'  # .text
    email = '//div/div/div/div/div/div[2]/div/div/span/span/a[@role="link" and @target="_blank" and contains(text(), "@")  and contains(@href, "mailto:")]'  #.text
    open_hours_btn = '//div/div/div/div/div/div[2]/div/div[2]/span/div/div/span[2]/i/../..'
    open_hours_dialog = '//div[@data-pagelet="root"]/div/div[@role="dialog"]'


    @classmethod
    def open(cls):
        options = Options()
        options.add_argument(f"--user-data-dir={controller.browser_folder}")
        cls.window = Chrome(ChromeDriverManager().install(), options=options)
        cls.window.implicitly_wait(5)
        cls.window.get("https://www.facebook.com")

    @classmethod
    def login_check(cls):
        """
        :returns True if already logged in, False if needs logging in.
        """
        try:
            cls.window.find_element_by_xpath(cls.login_form)
            return False
        except NoSuchElementException:
            return True

    @classmethod
    def get_pages_urls(cls):
        """
        returns list of lists [[url, name]]
        returns False if search page doesn't exists
        """
        # CHECK IF CURRENT PAGE IS SEARCH PAGE
        if "search/pages" not in cls.window.current_url:
            try:
                cls.window.find_element_by_xpath(cls.pages_category_btn).click()
                WebDriverWait(cls.window, 5).until(ec.visibility_of_element_located((By.XPATH, cls.pages_category_btn_active)))
            except NoSuchElementException:
                return False
        pages = []  # [url, name]
        completed_elements = []
        # to check on the last iter
        last_loop_iter = False
        while True:
            # MAKE SURE THAT THE AJAX LOADER DOESN'T EXISTS
            WebDriverWait(cls.window, 10).until(ec.invisibility_of_element_located((By.XPATH, cls.ajax_loader)))
            elements = cls.window.find_elements_by_xpath(cls.search_result_name)
            for elem in elements:
                # SKIPPING COMPLETED PAGES
                if elem in completed_elements:
                    continue
                cls.window.execute_script("arguments[0].scrollIntoView();", elem)
                url = elem.get_attribute("href")
                # name = elem.find_element_by_xpath("span[1]").text
                name = elem.text
                page = [url, name]
                completed_elements.append(elem)
                print(page)
                pages.append(page)
            if last_loop_iter is True:
                break
            # check if the ajax loader exists >>> if it exists >>> keep going.. that means we still have more pages to show
            try:
                WebDriverWait(cls.window, 3).until(ec.presence_of_element_located((By.XPATH, cls.ajax_loader)))
                continue
            except TimeoutException:
                # if ajax loader has gone, that means we have loaded the last elements but it will not be scraped
                # so it will loop one last time and break after that to get the last shown elements
                last_loop_iter = True
                continue
        return pages

    @classmethod
    def scrape_details(cls, url):
        cls.window.get(url)
        # CHECK IF PAGE LOADED
        try:
            WebDriverWait(cls.window, 20).until(ec.visibility_of_element_located((By.XPATH, cls.page_about_link)))
        except TimeoutException:
            return False
        # ADDRESS SCRAPING
        try:
            address = cls.window.find_element_by_xpath(cls.address).text
        except NoSuchElementException:
            address = "---"
        # ADDRESS SCRAPING
        try:
            address = cls.window.find_element_by_xpath(cls.address).text
        except NoSuchElementException:
            address = "---"

