import os
import platform
from PySide2 import QtCore
from PySide2.QtGui import QCloseEvent, Qt
from PySide2.QtWidgets import *
from webbrowser import open
# Import your design class
from design import Ui_MainWindow as design
import controller
from models import Session


class View(QMainWindow, design):
    def __init__(self, api_url, parent=None):
        super(View, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.show()
        self.session = Session()
        self.state = "idle"
        # todo - activate the license key
        # self.api_url = api_url
        self.setWindowTitle(f"FYY Scraper {controller.version}")
        # HIDING TABWDIGET TOP BAR
        self.container_tabwid.tabBar().hide()
        # self.license_frame.hide()
        self.adjustSize()
        self.commandLinkButton.setText(f"Copyright © 2021 {controller.copyright_text}")


    @staticmethod
    def copyrights():
        open(controller.copyright_url)

    ######################################

    # Customizing the close event
    def closeEvent(self, event: QCloseEvent):
        if platform.system() == "Darwin":
            os.system("killall chromedriver")
            os.system("killall 'Google Chrome'")
        else:
            os.system("taskkill /t /F /im chromedriver.exe")

    @staticmethod
    def addToTableWidget(data: tuple, tablewidget_object: QTableWidget):  # slot >> trigger singal
        """
        Use this method if you have TableWidget to add items in rows
        """
        row_pos = tablewidget_object.rowCount()
        tablewidget_object.insertRow(row_pos)

        for index, info in enumerate(data):
            tablewidget_object.setItem(row_pos, index, QTableWidgetItem(info))
            tablewidget_object.scrollToBottom()

    @staticmethod
    def editItemInTableWidget(tablewidget_object: QTableWidget, textToFind: str, value: str, column: int):
        item = tablewidget_object.findItems(textToFind, Qt.MatchEndsWith)[0]
        row = tablewidget_object.row(item)
        tablewidget_object.setItem(row, column, QTableWidgetItem(value))

    @staticmethod
    def addToListWidget(items: list, listwidget: QListWidget):
        for item in items:
            listwidget.addItem(item)

    def saveDialog(self):
        """:return saving path"""
        path = QFileDialog.getSaveFileName(self, "save data", "data", "*.csv")
        return path[0]

    def confirmMessage(self, title: str, text: str, mode="question"):
        """
        use this method to show a confirm dialog
        :return: True if yes clicked - False if No clicked
        """
        if mode == "warning":
            re = QMessageBox.warning(self, title, text, QMessageBox.Yes | QMessageBox.No)
        else:
            re = QMessageBox.question(self, title, text, QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:
            return True
        else:
            return False

    def ok_message(self, title, text):
        QMessageBox.information(self, title, text, QMessageBox.Ok)

    def error_message(self, title, text):
        QMessageBox.critical(self, title, text, QMessageBox.Ok)

    def saveDialog(self):
        """:return saving path"""
        path = QFileDialog.getSaveFileName(self, "save data", "data", "*.csv")
        return path[0]

    def browse_singleFile_btn(self, lineedit_object: QLineEdit, title: str, extensions_range: str = ""):
        """
        use this on the browser button to get a file path and pass it to QLineEdit
        :return a tuple (path, file extension)
        """
        widget = lineedit_object
        path = QFileDialog.getOpenFileName(self, title, "", extensions_range)
        widget.setText(path[0])

    def browse_multipleFiles_btn(self, lineedit_object: QLineEdit, title: str, extensions_range: str = ""):
        """:return a tuple (path, file extension)"""
        path = QFileDialog.getOpenFileNames(self, title, "", extensions_range)
        if len(path[0]) > 0:
            lineedit_object.setText(str(path[0]))

    def get_file_path(self, title, extensions_range):
        path = QFileDialog.getOpenFileName(self, title, "", extensions_range)
        return path[0]

    def get_folder_path(self, title):
        path = QFileDialog.getExistingDirectory(self, title, "")
        return path

    @staticmethod
    def appendToPlainTextBox(plaintextedit_object: QPlainTextEdit, text: str):
        plaintextedit_object.insertPlainText(text)

    def changeStateToStopped(self):
        self.statusbar.showMessage(f"   >> Stopping in progress... <<")
        self.state = "stopped"

