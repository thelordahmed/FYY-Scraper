from yelp import Yelp
from yellowpages import YellowPages
from facebook import Facebook


class Connections:
    def __init__(self, view, main):
        self.view = view
        self.main = main

        # SIGNALS
        self.main.sig.ok_message.connect(self.view.ok_message)
        self.main.sig.non_modal_ok_message.connect(self.view.non_modal_ok_message)
        self.main.sig.error_message.connect(self.view.error_message)
        self.main.sig.add_to_tabelWidget.connect(self.view.addToTableWidget)
        self.main.sig.statusBar_msg.connect(self.view.statusbar.showMessage)
        # EXPORTING
        self.view.export_btn.clicked.connect(lambda: self.main.export(
            filter_keyword=self.view.source_cb.currentText(),
            sort_keyword=self.view.sortBy_cb.currentText()
        ))
        # CLEAR BUTTON
        self.view.clear_btn.clicked.connect(self.main.clear_btn_func)
        # YELP BUTTONS
        self.view.yelp_openBrowser.clicked.connect(self.main.yelp_openBrowser)
        self.view.yelp_start.clicked.connect(lambda: self.main.process_start(self.main.yelp_process, self.view.yelp_start, self.view.yelp_stop))
        self.view.yelp_stop.clicked.connect(lambda: self.main.stop_button_func(Yelp, self.view.yelp_stop))
        # FACEBOOK BUTTONS
        self.view.fb_openBrowser.clicked.connect(self.main.fb_open_browser)
        self.view.fb_start.clicked.connect(lambda: self.main.process_start(self.main.fb_process, self.view.fb_start, self.view.fb_stop))
        self.view.fb_stop.clicked.connect(lambda: self.main.stop_button_func(Facebook, self.view.fb_stop))
        # YELLOW PAGES BUTTONS
        self.view.yp_openBrowser.clicked.connect(self.main.yp_open_browser)
        self.view.yp_start.clicked.connect(lambda: self.main.process_start(self.main.yp_process, self.view.yp_start, self.view.yp_stop))
        self.view.yp_stop.clicked.connect(lambda: self.main.stop_button_func(YellowPages, self.view.yp_stop))
