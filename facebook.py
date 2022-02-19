import random
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    InvalidArgumentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import controller
import re
import json




class Facebook:
    window = None
    state = "idle"
    window: Chrome
    login_form = '//form[contains(@class, "featuredLogin")]'
    search_input = '//input[@type="search" and @role="combobox" and @value!=""]'
    ajax_loader = '//div[@aria-busy and @role="progressbar" and @data-visualcompletion="loading-state"]'
    pages_category_btn = '//div[@data-visualcompletion="ignore-dynamic"]/a[contains(@href, "search/pages")]'
    pages_category_btn_active = '//div[@data-visualcompletion="ignore-dynamic"]/a[contains(@href, "search/pages") and @aria-current="page"]'
    end_of_results = '//div[@role="feed"]//div[last()][@class]/div[@class]/div[@class]/span[@class][text()]'
    # search_result_name = '//div[@role="article"]//a[@role="link" and @tabindex and @class and @aria-label]'
    search_result_name = '//div[@role="article"]//a[@role="link"]'
    # TO CHECK IF PAGE LOADED OR NOT
    page_about_link = '//div/div/div/a[contains(@href, "/about") and @role="link"]'
    # PAGE DETAILS INFO
    detail_ajax_loader = '//*[@id="mount_0_0_PO"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[4]/div/div/div[1]//div[@aria-busy="true" and @role="progressbar" and @data-visualcompletion="loading-state"]'
    close_chat_btn = '//div[@data-prevent_chattab_focus]//div/span[2]'
    address = '//a[contains(@href, "maps") and @role="link"]/span/span'
    website = '//div/div/div/div/div/div[2]/div/div/span/span/a[@role="link" and @target="_blank" and @rel="nofollow noopener" and contains(text(), "http") and not(contains(text(), "twitter")) and not(contains(text(), "youtube")) and not(contains(text(), "instagram"))] | //div[contains(@data-pagelet, "ProfileTilesFeed")]//span[not(contains(text(), "twitter")) and not(contains(text(), "youtube")) and not(contains(text(), "instagram")) and contains(text(), ".com") and not(contains(text(), "@")) or contains(text(), "http") ]'  # .text
    email = '//div/div/div/div/div/div[2]/div/div/span/span/a[@role="link" and @target="_blank" and contains(text(), "@")  and contains(@href, "mailto:")] | //div[contains(@data-pagelet, "ProfileTilesFeed")]//div/span[contains(text(), "@")  and contains(text(), ".")]'  #.text
        # IF OPEN HOURS NOT FOUND LOOK FOR OPEN NOW
    open_hours = '//div[@class]/span[@class and @dir]/div[@class and @tabindex]/div[@class]/span[@class][1]'
        # THIS WILL RETURN MULTIPLE VALUES, GET THEM AND EXTRACT THE PHONE NUMBER WITH REGEX
    phone = '//div[not(@class)]/div[@class]/div[@class]/div[@class]/div[i]/../div[2]/div[@class]/div[@class]/span[@class and @dir="auto"]/span[not(a) and contains(text(), "0") or contains(text(), "9") or contains(text(), "1")] | //div[contains(@data-pagelet, "ProfileTilesFeed")]//div[@class]/div[@class]/div[@class]/span[@class and @dir="auto" and contains(text(), "0") or contains(text(), "9") or contains(text(), "1")]'


    @classmethod
    def open(cls):
        options = Options()
        options.add_argument(f"--user-data-dir={controller.browser_folder}")
        try:
            cls.window = Chrome(ChromeDriverManager().install(), options=options)
        except InvalidArgumentException:
            cls.window.quit()
            sleep(1)
            cls.window = Chrome(ChromeDriverManager().install(), options=options)
        cls.window.implicitly_wait(5)
        cls.window.get("https://www.facebook.com")
        cls.window.maximize_window()

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
    def get_results_urls(cls):
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
        search_keyword = cls.window.find_element_by_xpath(cls.search_input).get_attribute("value")
        results = []  # [url, name]
        completed_elements = []
        # to check on the last iter
        last_loop_iter = False
        while True:
            # MAKE SURE THAT THE AJAX LOADER DOESN'T EXISTS
            WebDriverWait(cls.window, 10).until(ec.invisibility_of_element_located((By.XPATH, cls.ajax_loader)))
            elements = cls.window.find_elements_by_xpath(cls.search_result_name)
            cls.window.switch_to.window(cls.window.current_window_handle)
            for elem in elements:
                # SKIPPING COMPLETED PAGES
                if elem in completed_elements:
                    continue
                # AVOIDING THE STALE ELEMENTS
                try:
                    url = elem.get_attribute("href")
                    # FIXING A BUG - SHOWING WERID RESULTS AT THE BEGINING OF THE ELEMENTS LIST
                    try:
                        name = elem.find_element_by_xpath("span[1]").text
                    except NoSuchElementException:
                        continue
                    # SCROLLING THE LAST ELEMENT
                    cls.window.execute_script("arguments[0].scrollIntoView();", elem)
                except StaleElementReferenceException:
                    break
                # AVOIDING WRONG ELEMENTS
                if "__cft__" in url or "/search/pages/" in url or "/groups/" in url:
                    continue
                # name = elem.text
                result = [url, name]
                completed_elements.append(elem)
                print(result)
                results.append(result)
            if last_loop_iter is True:
                break
            # GET BACK TO LOOP IF THERE ARE MORE ELEMENTS TO LOAD
            sleep(2)
            try:
                cls.window.find_element_by_xpath(cls.end_of_results)
                last_loop_iter = True
                continue
            except NoSuchElementException:
                WebDriverWait(cls.window, 20).until(ec.invisibility_of_element_located((By.XPATH, cls.ajax_loader)))


            # # check if the ajax loader exists >>> if it exists >>> keep going.. that means we still have more pages to show
            # try:
            #     WebDriverWait(cls.window, 10).until(ec.visibility_of_element_located((By.XPATH, cls.ajax_loader)))
            #     continue
            # except TimeoutException:
            #     # if ajax loader has gone, that means we have loaded the last elements but it will not be scraped
            #     # so it will loop one last time and break after that to get the last shown elements
            #     last_loop_iter = True
            #     continue
        with open(controller.fb_processed_json, "w") as f:
            obj = {
                "search_keyword": search_keyword,
                "results": results
            }
            f.write(json.dumps(obj))
        return results

    @classmethod
    def scrape_details(cls, url):
        cls.window.get(url)
        try:
            WebDriverWait(cls.window, 10).until(ec.invisibility_of_element_located((By.XPATH, cls.detail_ajax_loader)))
        except TimeoutException:
            print("NOT FOUND")
            pass
        # CHECK IF PAGE LOADED
        sleep(random.randint(3, 8))
        # ADDRESS SCRAPING
        try:
            address = cls.window.find_element_by_xpath(cls.address).text
        except NoSuchElementException:
            address = "---"
        # WESBITE SCRAPING
        try:
            website = cls.window.find_element_by_xpath(cls.website).text
        except NoSuchElementException:
            website = "---"
        # EMAIL SCRAPING
        try:
            email = cls.window.find_element_by_xpath(cls.email).text
        except NoSuchElementException:
            email = "---"
        # OPEN HOURS SCRAPING
        try:
            open_hours = cls.window.find_element_by_xpath(cls.open_hours).text
        except NoSuchElementException:
            open_hours = "---"
        # PHONE SCRAPING
        try:
            phone = cls.window.find_element_by_xpath(cls.phone).text
        except NoSuchElementException:
            phone = "---"
        # # PHONE SCRAPING
        # elements = cls.window.find_elements_by_xpath(cls.phone_elems)
        # phone = "---"
        # for elem in elements:
        #     match = re.search(r"(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?))(\d{3}(\s|-?))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?",
        #                       elem.text)
        #     if match is not None:
        #         phone = match.group()
        #         break
        if website == "---" and email == "---" and phone == "---":
            return False
        return [address, website, email, phone, open_hours]
