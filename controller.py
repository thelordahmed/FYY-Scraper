from platform import system
import os


if system() == "Darwin":
    data_folder = f"{os.path.expanduser('~')}/Library/FYYScraper"
else:
    data_folder = "Data"
browser_folder = os.path.join(data_folder, "browserData")

version = "1.0.0"
copyright_text = "AhmeDSaeeD | (lordahmed on Fiverr)"
copyright_url = "https://fiverr.com/lordahmed"