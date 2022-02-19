import csv
import os
import platform
import random
from time import sleep
import usaddress
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QTableWidget
import threading

from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from sqlalchemy import func
from view import View
from models import Report, YelpResults, YellowPagesResults, FacebookPages, Session
from yelp import Yelp
from facebook import Facebook
from connections import Connections
from states import States
from yellowpages import YellowPages
import traceback
import controller
import json
# hidden imports (for EXE compiling)
import pycrfsuite._dumpparser
from pycrfsuite import _logparser


class Signals(QtCore.QObject):
    ok_message = QtCore.Signal(str, str)
    non_modal_ok_message = QtCore.Signal(str, str)
    error_message = QtCore.Signal(str, str)
    add_to_tabelWidget = QtCore.Signal(tuple, QTableWidget)
    statusBar_msg = QtCore.Signal(str)


class Main:
    def __init__(self):
        self.view = View("API URL")
        self.sig = Signals()
        self.states = States(self.view, self)
        self.session = Session()
        # UI WIDGETS CALLBACKS
        Connections(self.view, self)
        # LOADING INTERFACE VALUES - OPENED IN ANOTHER THREAD TO ENHANCE OPENING SPEED
        # self.session.query(Report).delete()
        # self.session.query(YelpResults).delete()
        # self.session.commit()
        threading.Thread(target=self.ui_default_status).start()

    @staticmethod
    def parse_address(address: str) -> dict:
        """
        this method will parse full usa address to city, state and street address
        """
        # AVOIDING BUGS
        try:
            adr = usaddress.tag(address)
        except:
            return {
                "city": "---",
                "state": "---",
                "street": address
            }
        try:
            city = adr[0]["PlaceName"]
        except:
            city = "---"
        try:
            state = adr[0]["StateName"]
        except:
            state = "---"
        if adr[1] != "Ambiguous":
            street_address = address.replace(city, "").replace(state, "")
        else:
            street_address = "---"
        return {
            "city": city,
            "state": state,
            "street": street_address
        }

    @staticmethod
    def clean_phone_number(phone: str):
        symbols = ["(", ")", " ", "-", "\\", "/", "+"]
        for sym in symbols:
            phone = phone.replace(sym, "")
        return phone

    def ui_default_status(self):
        self.view.listWidget.setCurrentRow(0)
        self.view.container_tabwid.setCurrentIndex(0)
        self.view.yelp_stop.setDisabled(True)
        self.view.yp_stop.setDisabled(True)
        self.view.fb_stop.setDisabled(True)
        # LOADING REPORTS
        reports = self.session.query(
            Report.name,
            Report.email,
            Report.phone,
            Report.website,
            Report.fb_page,
            Report.address,
            Report.state,
            Report.city,
            Report.open_hours,
            Report.search_keyword,
            Report.source,
        ).all()
        for record in reports:
            self.sig.add_to_tabelWidget.emit(record, self.view.tableWidget)

    def export(self, filter_keyword, sort_keyword):
        session = Session()
        # PREPARING SORT KEYWORD TO BE PASSED TO THE DATABASE QUERY
        if sort_keyword == "name":
            sort_poperty = Report.name
        elif sort_keyword == "address":
            sort_poperty = Report.address
        elif sort_keyword == "state":
            sort_poperty = Report.state
        elif sort_keyword == "city":
            sort_poperty = Report.city
        elif sort_keyword == "open hours":
            sort_poperty = Report.open_hours
        elif sort_keyword == "search keyword":
            sort_poperty = Report.search_keyword
        else:
            print("sort keyword not SPECIFIED!!! defaulted to sort by name")
            sort_poperty = Report.name
        # CHECKING IF FILTER BY SOURCE WAS CHOOSED
        try:
            if filter_keyword == "All":
                reports = session.query(
                    Report.name,
                    Report.email,
                    Report.phone,
                    Report.website,
                    Report.fb_page,
                    Report.address,
                    Report.state,
                    Report.city,
                    Report.open_hours,
                    Report.search_keyword,
                    Report.source,
                ).order_by(sort_poperty).all()
            else:
                reports = session.query(
                    Report.name,
                    Report.email,
                    Report.phone,
                    Report.website,
                    Report.fb_page,
                    Report.address,
                    Report.state,
                    Report.city,
                    Report.open_hours,
                    Report.search_keyword,
                    Report.source,
                ).filter_by(source=filter_keyword).order_by(sort_poperty).all()
            print(reports)
            if len(reports) == 0:
                self.sig.error_message.emit("Error", "No Data to export!")
                return False
            # ALLOW USER TO CHOOSE THE CSV FILE LOCATION
            path = self.view.saveDialog()
            with open(path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["Name", "Email", "Phone", "Website", "Facbook Page", "Address", "State", "City", "Open Hours",
                     "Search Keyword", "Source"])
                for row in reports:
                    writer.writerow(row)
        except Exception as e:
            print(e)
            pass

    @staticmethod
    def is_browser_opened(window_check_var):
        if window_check_var is not None:
            try:
                print(window_check_var.current_window_handle)
                return True
            except:
                return False
        else:
            return False

    def clear_btn_func(self):
        res = self.view.confirmMessage("Confirm", "The data will be deleted, Are you sure?", "warning")
        if res:
            session = Session()
            session.query(Report).delete()
            session.query(YelpResults).delete()
            session.query(YellowPagesResults).delete()
            session.query(FacebookPages).delete()
            session.commit()
            if platform.system() == "Darwin":
                os.system(f"rm {controller.fb_processed_json}")
            else:
                os.system(f"del {controller.fb_processed_json}")

            self.view.tableWidget.setRowCount(0)

    @staticmethod
    def process_start(process_func, start_btn, stop_btn):
        start_btn.setDisabled(True)
        stop_btn.setEnabled(True)
        threading.Thread(target=process_func).start()

    @staticmethod
    def stop_button_func(target_class, stop_btn):
        target_class.state = "stopped"
        stop_btn.setDisabled(True)
        stop_btn.setText("Stopping...")

    def yelp_openBrowser(self):
        if Yelp.window is not None:
            try:
                Yelp.window.switch_to.window(Yelp.window.current_window_handle)
                return False
            except NoSuchWindowException and WebDriverException:
                pass
        self.view.yelp_openBrowser.setDisabled(True)
        threading.Thread(target=Yelp.open).start()
        sleep(3)
        self.view.yelp_openBrowser.setEnabled(True)

    def yelp_process(self):
        try:
            # CHECK IF BROWSER OPENED
            if Yelp.window is not None:
                try:
                    print(Yelp.window.current_window_handle)
                except NoSuchWindowException and WebDriverException:
                    self.sig.error_message.emit("Error", "Yelp Browser Window is Not Opened!")
                    self.states.reset_start_button(self.view.yelp_start, self.view.yelp_stop,
                                                   self.view.yelp_openBrowser)
                    return False
            else:
                self.sig.error_message.emit("Error", "Yelp Browser Window is Not Opened!")
                self.states.reset_start_button(self.view.yelp_start, self.view.yelp_stop, self.view.yelp_openBrowser)
                return False
            # DATABASE SESSION VAR
            session = Session()
            # CONTINUING FOR LAST CHECKPOINT
            searching_keyword = Yelp.get_search_keyword()
            if not searching_keyword:
                self.sig.error_message.emit("Error", "Search Results Not Found!")
                self.states.reset_start_button(self.view.yelp_start, self.view.yelp_stop, self.view.yelp_openBrowser)
                return False
            record = session.query(func.max(YelpResults.page)).filter_by(
                search_keyword=searching_keyword).first()  # RETURNS TUPLE
            if record[0] is not None:
                target_page = record[0]
                # MAKE SURE THAT WE ARE NOT ON THE FIRST PAGE TO AVOID INFINITE LOOP
                if target_page > 1:
                    Yelp.move_to_page(target_page)
            # SHOWING REPORT PANEL
            self.view.listWidget.setCurrentRow(1)
            # SCRAPING RESULTS (WITHOUT DETAILS)
            results = Yelp.scrape_results()
            if results is False:
                self.sig.error_message.emit("Error", "Search Results Not Found!")
                self.states.reset_start_button(self.view.yelp_start, self.view.yelp_stop, self.view.yelp_openBrowser)
                return False
            ### PROCESS LOOP ###
            while True:
                # STOP EVENT CHECK
                if Yelp.state == "stopped":
                    break
                results = Yelp.scrape_results()
                for name, reviews, verfied, search_keyword, page, url in results:
                    self.view.statusbar.showMessage(f"    (YELP) - Scraping '{name}'...")
                    # STOP EVENT CHECK
                    if Yelp.state == "stopped":
                        break
                    # CHECK IF RESULT WAS SCRAPED BEFORE
                    db_record = session.query(YelpResults).filter_by(name=name, reviews=reviews,
                                                                     verfied_license=verfied).first()
                    if db_record is not None:
                        continue
                    # SCRAPING RESULT DETAILS
                    result_details = Yelp.scrape_result_details(url)
                    if result_details is False:
                        continue
                    email, phone, website, address, open_hours = result_details[0], result_details[1], result_details[
                        2], \
                                                                 result_details[3], result_details[4]
                    # PARSING THE ADDRESS TO STATE, CITY, STREET
                    if address != "---":
                        parsed_address = self.parse_address(address)
                    else:
                        parsed_address = {"street": "---", "state": "---", "city": "---"}
                    # CLEANING NUMBER FORMAT
                    phone = self.clean_phone_number(phone)
                    # ADDING TO THE DATABASE
                    yelp_obj = YelpResults(
                        name=name,
                        reviews=reviews,
                        verfied_license=verfied,
                        search_keyword=search_keyword,
                        page=page
                    )
                    session.add(yelp_obj)
                    session.commit()
                    # AVOIDING DUBLICATES DATA
                    if email == "---":
                        report_record = session.query(Report).filter_by(phone=phone).first() if phone != "---" else None
                    elif phone == "---":
                        report_record = session.query(Report).filter_by(email=email).first()
                    else:
                        report_record = session.query(Report).filter(
                            (Report.phone == phone) | (Report.email == email)).first()
                    if report_record is not None:
                        continue
                    report_obj = Report(
                        name=name,
                        email=email,
                        phone=phone,
                        website=website,
                        fb_page="---",
                        address=parsed_address["street"],
                        state=parsed_address["state"],
                        city=parsed_address["city"],
                        open_hours=open_hours,
                        search_keyword=search_keyword,
                        source="Yelp"
                    )
                    session.add(report_obj)
                    session.commit()
                    # ADDING TO UI
                    data = (name, email, phone, website, "---", parsed_address["street"],
                            parsed_address["state"], parsed_address["city"], open_hours, search_keyword, "Yelp")
                    self.sig.add_to_tabelWidget.emit(data, self.view.tableWidget)
                if Yelp.state == "stopped":
                    break
                # GOIING TO NEXT PAGE
                self.sig.statusBar_msg.emit(">>> (Yelp) - Delaying 15 to 25 seconds to avoid block")
                sleep(random.randint(15, 25))
                self.sig.statusBar_msg.emit("")
                if Yelp.click_next_page() is False:
                    self.sig.ok_message.emit("Yelp Note", "Yelp Completed Successfully ^_^")
                    break
        # HANDELING UNKNOWN ERRORS
        except Exception as e:
            Yelp.state = "error"
            self.sig.error_message.emit("Error",
                                        f"Something Wrong Happened\nError:\n{e}\ntraceback:\n{traceback.extract_tb(e.__traceback__)}")
        # COMPLETED ACTION
        if Yelp.state != "stopped" and Yelp.state != "error":
            self.sig.non_modal_ok_message.emit("Yelp Completed",
                                               "Yelp Completed Scraping Process Successfully ^_^")
        else:
            # RESETING STOP BUTTON
            self.view.yelp_stop.setText("")
            self.view.yelp_stop.setEnabled(True)
        self.states.reset_start_button(self.view.yelp_start, self.view.yelp_stop, self.view.yelp_openBrowser)
        Yelp.state = "idle"
        self.view.statusbar.showMessage(f"")

    def fb_open_browser(self):
        if self.is_browser_opened(Facebook.window) is False:
            self.view.fb_openBrowser.setDisabled(True)
            threading.Thread(target=Facebook.open).start()
            sleep(3)
            self.view.fb_openBrowser.setEnabled(True)

    def fb_process(self):
        try:
            # CHECK IF BROWSER OPENED
            if Facebook.window is not None:
                try:
                    print(Facebook.window.current_window_handle)
                except:
                    self.sig.error_message.emit("Error", "Facebook Browser Window is Not Opened!")
                    self.states.reset_start_button(self.view.fb_start, self.view.fb_stop, self.view.fb_openBrowser)
                    return False
            else:
                self.sig.error_message.emit("Error", "Facebook Browser Window is Not Opened!")
                self.states.reset_start_button(self.view.fb_start, self.view.fb_stop, self.view.fb_openBrowser)
                return False
            # CHANGING STATE TO "started"
            Facebook.state = "started"
            # DATABASE SESSION VAR
            session = Session()
            # CHECK IF LOGGED IN
            if Facebook.login_check() is False:
                self.sig.error_message.emit("Error", "You're Not Logged in!")
                self.states.reset_start_button(self.view.fb_start, self.view.fb_stop, self.view.fb_openBrowser)
                return False
            # GETTING THE KEYWORD
            try:
                search_keyword = Facebook.window.find_element_by_xpath(Facebook.search_input).get_attribute("value")
            except:
                self.sig.error_message.emit("Error", "search reults not found, please make your search first!")
                self.states.reset_start_button(self.view.fb_start, self.view.fb_stop, self.view.fb_openBrowser)
                return False
            # CHECKPOINT CONTINUE
            pages = None
            try:
                with open(controller.fb_processed_json, "r") as f:
                    json_obj = json.loads(f.read())
                    if search_keyword == json_obj["search_keyword"]:
                        pages = json_obj["results"]
            except:
                pass
            if pages is None:
                # GET SEARCH RESULTS
                self.view.statusbar.showMessage("    (Facebook) - Processing Pages...")
                pages = Facebook.get_results_urls()
                self.view.statusbar.showMessage("")
                if pages is False:
                    self.sig.error_message.emit("Error", "search reults not found, please make your search first!")
                    self.states.reset_start_button(self.view.fb_start, self.view.fb_stop, self.view.fb_openBrowser)
                    return False

            # SHOWING REPORT PANEL
            self.view.listWidget.setCurrentRow(1)
            # LIMIT COUNTER
            counter = 0
            #### PROCESS LOOP ####
            for url, name in pages:
                # STOP EVENT CHECK
                if Facebook.state == "stopped":
                    break
                # LIMIT COUNTER CHECK
                if counter >= 20:
                    counter = 0
                    self.view.statusbar.showMessage(
                        f"    (Facebook) -  Random Delay From 10 to 25 seconds to avoid block")
                    sleep(random.randint(10, 25))
                    self.view.statusbar.showMessage(f"")
                # CHECK IF PAGE WAS SCRAPED BEFORE
                record = session.query(FacebookPages).filter_by(url=url, name=name).first()
                if record is not None:
                    continue
                # RANDOM DELAY
                sleep(random.randint(1, 5))
                # ADDING TO FACEBOOK MODEL
                fb_model = FacebookPages(name=name, url=url)
                session.add(fb_model)
                session.commit()
                # SCRAPING THE PAGE DETAILS
                self.view.statusbar.showMessage(f"    (Facebook) -  Scraping '{name}'...")
                page_details = Facebook.scrape_details(url)
                # +1 COUTNER WHEN OPENING A PAGE
                counter += 1
                self.view.statusbar.showMessage(f"")
                if page_details is False:
                    self.view.statusbar.showMessage(f"    (Facebook) -  No Information available in {name}...")
                    sleep(random.randint(1, 3))
                    self.view.statusbar.showMessage(f"")
                    continue
                # RANDOM SLEEP
                sleep(random.randint(2, 4))
                address, website, email, phone, open_hours = page_details[0], page_details[1], page_details[2], \
                                                             page_details[3], page_details[4]
                # PARSING THE ADDRESS TO STATE, CITY, STREET
                if address != "---":
                    parsed_address = self.parse_address(address)
                else:
                    parsed_address = {"street": "---", "state": "---", "city": "---"}

                # CLEANING NUMBER FORMAT
                if phone != "---":
                    phone = self.clean_phone_number(phone)
                # AVOIDING DUBLICATES DATA
                if email == "---":
                    report_record = session.query(Report).filter_by(phone=phone).first() if phone != "---" else None
                elif phone == "---":
                    report_record = session.query(Report).filter_by(email=email).first()
                else:
                    report_record = session.query(Report).filter(
                        (Report.phone == phone) | (Report.email == email)).first()
                if report_record is not None:
                    continue
                report_obj = Report(
                    name=name,
                    email=email,
                    phone=phone,
                    website=website,
                    fb_page=url,
                    address=parsed_address["street"],
                    state=parsed_address["state"],
                    city=parsed_address["city"],
                    open_hours=open_hours,
                    search_keyword=search_keyword,
                    source="Facebook"
                )
                session.add(report_obj)
                session.commit()
                # ADDING TO UI
                data = (name, email, phone, website, url, parsed_address["street"],
                        parsed_address["state"], parsed_address["city"], open_hours, search_keyword, "Facebook")
                self.sig.add_to_tabelWidget.emit(data, self.view.tableWidget)
        except Exception as e:
            Facebook.state = "error"
            self.sig.error_message.emit("Error",
                                        f"Something Wrong Happened\nError:\n{e}\ntraceback:\n{traceback.extract_tb(e.__traceback__)}")
        # COMPLETED ACTION
        if Facebook.state != "stopped" and Facebook.state != "error":
            self.sig.non_modal_ok_message.emit("Facebook Completed",
                                               "Facebook Completed Scraping Process Successfully ^_^")
        else:
            self.view.fb_stop.setText("")
            self.view.fb_stop.setEnabled(True)
        self.states.reset_start_button(self.view.fb_start, self.view.fb_stop, self.view.fb_openBrowser)
        Facebook.state = "idle"
        self.view.statusbar.showMessage("")
        Facebook.window.quit()

    def yp_open_browser(self):
        if self.is_browser_opened(YellowPages.window) is False:
            self.view.yp_openBrowser.setDisabled(True)
            threading.Thread(target=YellowPages.open).start()
            sleep(3)
            self.view.yp_openBrowser.setEnabled(True)

    def yp_process(self):
        try:
            # CHECK IF BROWSER OPENED
            if YellowPages.window is not None:
                try:
                    print(YellowPages.window.current_window_handle)
                except NoSuchWindowException and WebDriverException:
                    self.sig.error_message.emit("Error", "YellowPages Browser Window is Not Opened!")
                    self.states.reset_start_button(self.view.yp_start, self.view.yp_stop, self.view.yp_openBrowser)
                    return False
            else:
                self.sig.error_message.emit("Error", "YellowPages Browser Window is Not Opened!")
                self.states.reset_start_button(self.view.yp_start, self.view.yp_stop, self.view.yp_openBrowser)
                return False
            # CHANGING STATE TO "started"
            YellowPages.state = "started"
            # DATABASE SESSION VAR
            session = Session()
            # CONTINUING FOR LAST CHECKPOINT
            searching_keyword = YellowPages.get_search_keyword()
            if not searching_keyword:
                self.sig.error_message.emit("Error", "Search Results Not Found!")
                self.states.reset_start_button(self.view.yp_start, self.view.yp_stop, self.view.yp_openBrowser)
                return False
            record = session.query(func.max(YellowPagesResults.page)).filter_by(
                search_keyword=searching_keyword).first()  # RETURNS TUPLE
            if record[0] is not None:
                target_page = int(record[0])
                # MAKE SURE THAT WE ARE NOT ON THE FIRST PAGE TO AVOID INFINITE LOOP
                if target_page > 1:
                    YellowPages.move_to_page(target_page)
            # SHOWING REPORT PANEL
            self.view.listWidget.setCurrentRow(1)

            #### PROCESS LOOP ####
            while True:
                # STOP EVENT CHECK
                if YellowPages.state == "stopped":
                    break
                # CURRENT PAGE
                page = YellowPages.get_current_page()
                if YellowPages.state == "started":
                    self.view.statusbar.showMessage(">>>    (YELLOW PAGES) - Scraping the data... ")
                # CURRENT PAGE SOURCE
                page_source = YellowPages.window.page_source
                data = YellowPages.scrape_results(page_source)
                for name, address, phone, website, url in data:
                    # STOP EVENT CHECK
                    if YellowPages.state == "stopped":
                        break
                    # SKIP IF IT WAS SCRAPED BEFORE
                    record = session.query(YellowPagesResults).filter_by(
                        name=name,
                        address=address,
                        phone=phone,
                        website=website,
                        url=url
                    ).first()
                    if record is not None:
                        continue
                    # ADD TO THE DATABASE
                    yp_obj = YellowPagesResults(
                        name=name,
                        address=address,
                        phone=phone,
                        url=url,
                        website=website,
                        page=page,
                        search_keyword=searching_keyword
                    )
                    session.add(yp_obj)
                    session.commit()
                    self.view.statusbar.showMessage(f"   (YellowPages) - Scraping '{name}'...")
                    # PARSING THE ADDRESS TO STATE, CITY, STREET
                    if address != "---":
                        parsed_address = self.parse_address(address)
                    else:
                        parsed_address = {"street": "---", "state": "---", "city": "---"}
                    # CLEANING NUMBER FORMAT
                    phone = self.clean_phone_number(phone)
                    # SCRAPING THE EMAIL
                    email = YellowPages.scrape_email(url)
                    # AVOIDING DUBLICATES DATA
                    if email == "---":
                        report_record = session.query(Report).filter_by(phone=phone).first() if phone != "---" else None
                    elif phone == "---":
                        report_record = session.query(Report).filter_by(email=email).first()
                    else:
                        report_record = session.query(Report).filter(
                            (Report.phone == phone) | (Report.email == email)).first()
                    if report_record is not None:
                        continue
                    open_hours = "---"
                    report_obj = Report(
                        name=name,
                        email=email,
                        phone=phone,
                        website=website,
                        fb_page="---",
                        address=parsed_address["street"],
                        state=parsed_address["state"],
                        city=parsed_address["city"],
                        open_hours=open_hours,
                        search_keyword=searching_keyword,
                        source="Yellow Pages"
                    )
                    session.add(report_obj)
                    session.commit()
                    # ADDING TO UI
                    data = (name, email, phone, website, "---", parsed_address["street"],
                            parsed_address["state"], parsed_address["city"], open_hours, searching_keyword,
                            "Yellow Pages")
                    self.sig.add_to_tabelWidget.emit(data, self.view.tableWidget)
                    self.view.statusbar.showMessage("")
                if YellowPages.state == "stopped":
                    break
                # GOIING TO NEXT PAGE
                self.sig.statusBar_msg.emit(">>> (YellowPages) - Delaying 15 to 25 seconds to avoid block")
                sleep(random.randint(15, 25))
                self.sig.statusBar_msg.emit("")
                if YellowPages.click_next_page() is False:
                    break
        # HANDELING UNKNOWN ERRORS
        except Exception as e:
            YellowPages.state = "error"
            self.sig.error_message.emit("Error",
                                        f"Something Wrong Happened\nError:\n{e}\ntraceback:\n{traceback.extract_tb(e.__traceback__)}")
        # COMPLETED ACTION
        if YellowPages.state != "stopped" and YellowPages.state != "error":
            self.sig.non_modal_ok_message.emit("YellowPages Completed",
                                               "YellowPages Completed Scraping Process Successfully ^_^")
        else:
            # RESETING STOP BUTTON
            self.view.yp_stop.setText("")
            self.view.yp_stop.setEnabled(True)
        self.states.reset_start_button(self.view.yp_start, self.view.yp_stop, self.view.yp_openBrowser)
        YellowPages.state = "idle"
        self.view.statusbar.showMessage(f"")


if __name__ == '__main__':
    app = QApplication()
    main = Main()
    app.exec_()
