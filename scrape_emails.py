from time import sleep

import requests
from bs4 import BeautifulSoup
import re
import email_scraper
from urllib import parse

#todo - fix this output "href='//realtor.acceleragent.com/Login?pmProductURL=teamcherylv.com&LoginName=cheryl.villanueva@compass.com"


class EmailScraper:
    payload = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:86.0) Gecko/20100101 Firefox/86.0"
    }
    url_keywords = ["contact", "Contact", "about", "About", "profile", "Profile"]

    @classmethod
    def decode_protected_email(cls, email_code):
        de = ""
        k = int(email_code[:2], 16)
        for i in range(2, len(email_code) - 1, 2):
            de += chr(int(email_code[i:i + 2], 16) ^ k)
        return de

    @classmethod
    def _get_emails(cls, html: str) -> list:
        """
        returns list of emails - list of strings
        """
        # CHECK IF THERE IS A PROETECED EMAIL
        soup = BeautifulSoup(html, "lxml")
        elem = soup.find(class_="__cf_email__")
        email_list = []
        if elem is not None:
            coded_email = elem["data-cfemail"]
            email = cls.decode_protected_email(coded_email)
            email_list.append(email)
            return email_list
        # RETURN ALL POSSIBLE EMAILS IN PAGE SOURCE
        email_set = email_scraper.scrape_emails(html)
        if len(email_set) > 0:
            for i in email_set:
                if i not in email_list and "@sentry.io" not in i:
                    email_list.append(i)
        return email_list


    @classmethod
    def scrape_single_url(cls, url) -> list or False:
        """
        return False if url is not reachable
        return list of emails -> (list of strings)
        """
        try:
            response = requests.get(url, headers=cls.payload)
        except Exception as e:
            print(e)
            return False
        if response.status_code == 200:
            email = cls._get_emails(response.text)
            return email
        else:
            return False

    @classmethod
    def scrape_website(cls, website: str):
        """
        return False if website is not reachable
        return list of emails -> (list of strings)
        """
        emails = cls.scrape_single_url(website)
        if emails is False:
            return False    # CONNECTION PROBLEM
        # IF NOT FOUND ON MAIN PAGE, TRY OTHER ROUTES
        if emails is None:
            response = requests.get(website, headers=cls.payload)
            soup = BeautifulSoup(response.text, "lxml")
            targeted_a_tags = []
            emails_list = []
            urls_list = []
            for keyword in cls.url_keywords:
                a_tags = soup.select(f'a[href*="{keyword}"]')
                targeted_a_tags.extend(a_tags)

            for a_tag in targeted_a_tags:
                url = a_tag["href"]
                # CHECK IF URL IS PART OR FULL URL
                if parse.urlparse(url).netloc == "":
                    url = parse.urljoin(website, url)
                if url not in urls_list:
                    urls_list.append(url)

            for url in urls_list:
                emails = cls.scrape_single_url(url)
                for email in emails:
                    if email not in emails_list:
                        emails_list.append(email)
            # CONVERTING LIST TO STRING
            emails_str = ", "
            emails_str = emails_str.join(emails_list)
            return emails_str
        emails_str = ", "
        emails_str = emails_str.join(emails)
        return emails_str


# class EmailScraperSelenium:
#     url_keywords = ["contact", "about"]
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--window-size=1200,1100")
#     options.add_argument("--disable-gpu")
#     driver = None
#     email_search_xpath = '//*[contains(text(), "@")]'
#     email_regex = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
#
#
#     @classmethod
#     def scrape_single_url(cls, url: str):
#         if cls.driver is None:
#             cls.driver = Chrome(ChromeDriverManager().install(), options=cls.options)
#         cls.driver.get(url)
#         sleep(1)
#         cls.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#         sleep(1)
#         elements = cls.driver.find_elements_by_xpath(cls.email_search_xpath)
#         match = None
#         # SEARCHING IN TAGS VALUES
#         for elem in elements:
#             match = re.search(cls.email_regex, elem.text.lower())
#             if match is not None:
#                 return match.group()
#         return match
#
#     @classmethod
#     def scrape_website(cls, website: str):
#         email = cls.scrape_single_url(website)
#         if email is None:
#             # ALL "a" TAGS WITH A KEYWORD IN THE URL
#             a_tags = []
#             for keyword in cls.url_keywords:
#                 a_tags.extend(cls.driver.find_elements_by_xpath(f'//a[contains(@href, "{keyword}")]'))
#             if len(a_tags) > 0:
#                 for a_tag in a_tags:
#                     try:
#                         email = cls.scrape_single_url(a_tag.get_attribute("href"))
#                     except StaleElementReferenceException:
#                         print("a tag stale occured!!")
#                         pass
#                     if email is not None:
#                         break
#         return email


