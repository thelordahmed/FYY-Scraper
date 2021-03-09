# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(720, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(600, 100))
        self.label_6.setPixmap(QPixmap(u":/logo/Data/logo.png"))
        self.label_6.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.mainwindow_frame = QFrame(self.centralwidget)
        self.mainwindow_frame.setObjectName(u"mainwindow_frame")
        self.horizontalLayout_6 = QHBoxLayout(self.mainwindow_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, -1, -1)
        self.listWidget = QListWidget(self.mainwindow_frame)
        icon = QIcon()
        icon.addFile(u":/black-icons/Data/imgs/black icons/icons8-home-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setIcon(icon);
        icon1 = QIcon()
        icon1.addFile(u":/black-icons/Data/imgs/black icons/icons8-document-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/black-icons/Data/imgs/black icons/icons8-about-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setIcon(icon2);
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMinimumSize(QSize(160, 0))
        self.listWidget.setStyleSheet(u"QListView { /* The tab widget frame */\n"
"    background:transparent;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QListView::item {\n"
"    background: qlineargradient(spread:pad, x1:0.44335, y1:0.482955, x2:1, y2:0, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    min-width: 8ex;\n"
"    padding: 20px 0;\n"
"}\n"
"\n"
"QListView::item:selected, QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB;\n"
"	color:black;\n"
"	border-right: 0;\n"
"}\n"
"\n"
"QListView::item:!selected {\n"
"    margin-top: 0px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setIconSize(QSize(33, 33))
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(0)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setBatchSize(100)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)

        self.horizontalLayout_6.addWidget(self.listWidget)

        self.container_tabwid = QTabWidget(self.mainwindow_frame)
        self.container_tabwid.setObjectName(u"container_tabwid")
        self.container_tabwid.setStyleSheet(u"")
        self.container_tabwid.setTabPosition(QTabWidget.North)
        self.container_tabwid.setElideMode(Qt.ElideRight)
        self.container_tabwid.setUsesScrollButtons(False)
        self.container_tabwid.setDocumentMode(False)
        self.container_tabwid.setTabBarAutoHide(False)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.verticalLayout_9 = QVBoxLayout(self.main)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.groupBox = QGroupBox(self.main)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 12)
        self.yp_openBrowser = QPushButton(self.groupBox)
        self.yp_openBrowser.setObjectName(u"yp_openBrowser")
        sizePolicy.setHeightForWidth(self.yp_openBrowser.sizePolicy().hasHeightForWidth())
        self.yp_openBrowser.setSizePolicy(sizePolicy)
        self.yp_openBrowser.setStyleSheet(u"padding:10 20")

        self.horizontalLayout.addWidget(self.yp_openBrowser)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.yp_start = QPushButton(self.groupBox)
        self.yp_start.setObjectName(u"yp_start")
        sizePolicy.setHeightForWidth(self.yp_start.sizePolicy().hasHeightForWidth())
        self.yp_start.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u":/black-icons/Data/imgs/black icons/icons8-play-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.yp_start.setIcon(icon3)
        self.yp_start.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.yp_start)

        self.yp_stop = QPushButton(self.groupBox)
        self.yp_stop.setObjectName(u"yp_stop")
        sizePolicy.setHeightForWidth(self.yp_stop.sizePolicy().hasHeightForWidth())
        self.yp_stop.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u":/black-icons/Data/imgs/black icons/icons8-pause-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.yp_stop.setIcon(icon4)
        self.yp_stop.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.yp_stop)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.main)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.yelp_openBrowser = QPushButton(self.groupBox_2)
        self.yelp_openBrowser.setObjectName(u"yelp_openBrowser")
        sizePolicy.setHeightForWidth(self.yelp_openBrowser.sizePolicy().hasHeightForWidth())
        self.yelp_openBrowser.setSizePolicy(sizePolicy)
        self.yelp_openBrowser.setStyleSheet(u"padding:10 20")

        self.horizontalLayout_2.addWidget(self.yelp_openBrowser)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy3)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.yelp_start = QPushButton(self.groupBox_2)
        self.yelp_start.setObjectName(u"yelp_start")
        sizePolicy.setHeightForWidth(self.yelp_start.sizePolicy().hasHeightForWidth())
        self.yelp_start.setSizePolicy(sizePolicy)
        self.yelp_start.setIcon(icon3)
        self.yelp_start.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.yelp_start)

        self.yelp_stop = QPushButton(self.groupBox_2)
        self.yelp_stop.setObjectName(u"yelp_stop")
        sizePolicy.setHeightForWidth(self.yelp_stop.sizePolicy().hasHeightForWidth())
        self.yelp_stop.setSizePolicy(sizePolicy)
        self.yelp_stop.setIcon(icon4)
        self.yelp_stop.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.yelp_stop)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.main)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fb_openBrowser = QPushButton(self.groupBox_3)
        self.fb_openBrowser.setObjectName(u"fb_openBrowser")
        sizePolicy.setHeightForWidth(self.fb_openBrowser.sizePolicy().hasHeightForWidth())
        self.fb_openBrowser.setSizePolicy(sizePolicy)
        self.fb_openBrowser.setStyleSheet(u"padding:10 20")

        self.horizontalLayout_3.addWidget(self.fb_openBrowser)

        self.line_3 = QFrame(self.groupBox_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.fb_start = QPushButton(self.groupBox_3)
        self.fb_start.setObjectName(u"fb_start")
        sizePolicy.setHeightForWidth(self.fb_start.sizePolicy().hasHeightForWidth())
        self.fb_start.setSizePolicy(sizePolicy)
        self.fb_start.setIcon(icon3)
        self.fb_start.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.fb_start)

        self.fb_stop = QPushButton(self.groupBox_3)
        self.fb_stop.setObjectName(u"fb_stop")
        sizePolicy.setHeightForWidth(self.fb_stop.sizePolicy().hasHeightForWidth())
        self.fb_stop.setSizePolicy(sizePolicy)
        self.fb_stop.setIcon(icon4)
        self.fb_stop.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.fb_stop)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.horizontalFrame = QFrame(self.main)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy4)
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout_9.addWidget(self.horizontalFrame, 0, Qt.AlignHCenter)

        self.container_tabwid.addTab(self.main, "")
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.verticalLayout_15 = QVBoxLayout(self.report)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.tableWidget = QTableWidget(self.report)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 300))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.tableWidget.setFont(font1)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.tableWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_5 = QGroupBox(self.report)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sortBy_cb = QComboBox(self.groupBox_5)
        self.sortBy_cb.addItem("")
        self.sortBy_cb.addItem("")
        self.sortBy_cb.addItem("")
        self.sortBy_cb.addItem("")
        self.sortBy_cb.addItem("")
        self.sortBy_cb.addItem("")
        self.sortBy_cb.setObjectName(u"sortBy_cb")

        self.horizontalLayout_5.addWidget(self.sortBy_cb)


        self.horizontalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.report)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.source_cb = QComboBox(self.groupBox_4)
        self.source_cb.addItem("")
        self.source_cb.addItem("")
        self.source_cb.addItem("")
        self.source_cb.addItem("")
        self.source_cb.setObjectName(u"source_cb")

        self.verticalLayout_3.addWidget(self.source_cb)


        self.horizontalLayout_4.addWidget(self.groupBox_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.export_btn = QPushButton(self.report)
        self.export_btn.setObjectName(u"export_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.export_btn.sizePolicy().hasHeightForWidth())
        self.export_btn.setSizePolicy(sizePolicy5)
        self.export_btn.setStyleSheet(u"padding:10px 30px")

        self.verticalLayout_4.addWidget(self.export_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addLayout(self.verticalLayout_4)

        self.horizontalFrame_2 = QFrame(self.report)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy4.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 10)

        self.verticalLayout_15.addWidget(self.horizontalFrame_2, 0, Qt.AlignHCenter)

        self.container_tabwid.addTab(self.report, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout_2 = QVBoxLayout(self.about)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.about)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.about)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.textBrowser_5 = QTextBrowser(self.about)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        font3 = QFont()
        font3.setFamily(u"arial")
        self.textBrowser_5.setFont(font3)
        self.textBrowser_5.setStyleSheet(u"background:transparent;\n"
"border:transparent\n"
"\n"
"")
        self.textBrowser_5.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.textBrowser_5)

        self.container_tabwid.addTab(self.about, "")

        self.horizontalLayout_6.addWidget(self.container_tabwid)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.verticalLayout.addWidget(self.mainwindow_frame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_13 = QHBoxLayout(self.frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 1, -1, -1)
        self.commandLinkButton = QCommandLinkButton(self.frame)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy6)
        self.commandLinkButton.setMaximumSize(QSize(16777215, 25))
        self.commandLinkButton.setFont(font3)
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"background: transparent;\n"
"border:0")
        icon5 = QIcon()
        iconThemeName = u";"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u"../Yellow Pages sg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.commandLinkButton.setIcon(icon5)

        self.horizontalLayout_13.addWidget(self.commandLinkButton, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.listWidget.currentRowChanged.connect(self.container_tabwid.setCurrentIndex)

        self.listWidget.setCurrentRow(0)
        self.container_tabwid.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText("")

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Main", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Report", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"About", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Yellow Pages", None))
        self.yp_openBrowser.setText(QCoreApplication.translate("MainWindow", u"Open Browser", None))
        self.yp_start.setText("")
        self.yp_stop.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Yelp", None))
        self.yelp_openBrowser.setText(QCoreApplication.translate("MainWindow", u"Open Browser", None))
        self.yelp_start.setText("")
        self.yelp_stop.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.fb_openBrowser.setText(QCoreApplication.translate("MainWindow", u"Open Browser", None))
        self.fb_start.setText("")
        self.fb_stop.setText("")
        self.container_tabwid.setTabText(self.container_tabwid.indexOf(self.main), QCoreApplication.translate("MainWindow", u"Main", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Website", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"FB Page", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Open Hours", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Search Keyword", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Source", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Sort By:", None))
        self.sortBy_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"name", None))
        self.sortBy_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"address", None))
        self.sortBy_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"state", None))
        self.sortBy_cb.setItemText(3, QCoreApplication.translate("MainWindow", u"city", None))
        self.sortBy_cb.setItemText(4, QCoreApplication.translate("MainWindow", u"open hours", None))
        self.sortBy_cb.setItemText(5, QCoreApplication.translate("MainWindow", u"search keyword", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.source_cb.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.source_cb.setItemText(1, QCoreApplication.translate("MainWindow", u"Yelp", None))
        self.source_cb.setItemText(2, QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.source_cb.setItemText(3, QCoreApplication.translate("MainWindow", u"Yellow Pages", None))

        self.export_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.container_tabwid.setTabText(self.container_tabwid.indexOf(self.report), QCoreApplication.translate("MainWindow", u"Report", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Thanks for using the software", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"If you need any help, feel free to contact me at any time", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'arial'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600;\">- Contact Me -</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#107d41;\">Whatsapp</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://web.whatsapp.com/send?phone=201120641378\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">+201120641378</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#445bb8;\">Facebook</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://www.facebook.com/lord.ahmed110\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">fb.com/lord.ahmed110</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#db9409;\">Fiverr</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://www.fiverr.com/lordahmed\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">Fiverr.com/lordahmed</span></a></p></body></html>", None))
        self.container_tabwid.setTabText(self.container_tabwid.indexOf(self.about), QCoreApplication.translate("MainWindow", u"About", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Copyright 2021 LorDAhmeD", None))
    # retranslateUi

