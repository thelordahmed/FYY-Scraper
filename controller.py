from platform import system
import os


if system() == "Darwin":
    data_folder = f"{os.path.expanduser('~')}/Library/FYYScraper"
else:
    data_folder = r"C://ProgramData/FYYScraper/Data"
browser_folder = os.path.join(data_folder, "browserData")
fb_processed_json = os.path.join(data_folder, "fb_processed_pages.json")

version = "1.0.2"
copyright_text = "AhmeDSaeeD | (lordahmed on Fiverr)"
copyright_url = "https://fiverr.com/lordahmed"