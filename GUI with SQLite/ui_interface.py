# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacerhRiAi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 677)
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #ffffff;\n"
"}\n"
"#centralwidget, #homeBtn, #mainBodyContent, QLineEdit{\n"
"	background-color: #1b1b27;\n"
"}\n"
"\n"
"#header, #mainBody, #footer{\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#addEmployeeBtn{\n"
"	background-color: #cc5bce;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#logOut {\n"
"	border: 1px solid #cc5bce;\n"
"	border-radius: 19px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 3px 5px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#homeBtn{\n"
"	border-left: 3px solid #cc5bce;\n"
"	border-top: 3px solid #cc5bce;\n"
"	border-bottom: 3px solid #cc5bce;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.loginPage.setStyleSheet(u"")
        self.widget_6 = QWidget(self.loginPage)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(30, 30, 370, 480))
        self.label_2 = QLabel(self.loginPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 300, 420))
        self.label_2.setStyleSheet(u"border-image: url(:/images/th1.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;\n"
"")
        self.label_9 = QLabel(self.loginPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 60, 280, 390))
        self.label_9.setStyleSheet(u"background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.label_10 = QLabel(self.loginPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(135, 95, 90, 40))
        font = QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color:rgba(255,255,255,210);")
        self.userName = QLineEdit(self.loginPage)
        self.userName.setObjectName(u"userName")
        self.userName.setGeometry(QRect(80, 165, 200, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.userName.setFont(font1)
        self.userName.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.passCode = QLineEdit(self.loginPage)
        self.passCode.setObjectName(u"passCode")
        self.passCode.setGeometry(QRect(80, 230, 200, 40))
        self.passCode.setFont(font1)
        self.passCode.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.passCode.setEchoMode(QLineEdit.Password)
        self.loginBtn = QPushButton(self.loginPage)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(80, 310, 200, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.loginBtn.setFont(font2)
        self.loginBtn.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.loginPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayout_21 = QVBoxLayout(self.mainPage)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.header = QWidget(self.mainPage)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.frame_2)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.menuBtn, 0, Qt.AlignLeft)

        self.appName = QLabel(self.frame_2)
        self.appName.setObjectName(u"appName")
        font3 = QFont()
        font3.setPointSize(21)
        font3.setBold(True)
        font3.setWeight(75)
        self.appName.setFont(font3)
        self.appName.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.appName, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font4 = QFont()
        font4.setBold(False)
        font4.setWeight(50)
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.logOutBtn = QPushButton(self.frame)
        self.logOutBtn.setObjectName(u"logOutBtn")
        self.logOutBtn.setMinimumSize(QSize(38, 38))
        self.logOutBtn.setMaximumSize(QSize(38, 38))
        self.logOutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logOutBtn.setIcon(icon3)
        self.logOutBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.logOutBtn)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.header)

        self.mainBody = QWidget(self.mainPage)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setMinimumSize(QSize(919, 544))
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(0, 535))
        self.leftMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.widget_4 = QWidget(self.leftMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(290, 535))
        self.verticalLayout_16 = QVBoxLayout(self.widget_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 391))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_3)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"background-color: #1b1b27;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/home_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon4)
        self.homeBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.employeeBtn = QPushButton(self.frame_3)
        self.employeeBtn.setObjectName(u"employeeBtn")
        self.employeeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/users_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.employeeBtn.setIcon(icon5)
        self.employeeBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.employeeBtn)

        self.attendanceBtn = QPushButton(self.frame_3)
        self.attendanceBtn.setObjectName(u"attendanceBtn")
        self.attendanceBtn.setMinimumSize(QSize(0, 38))
        self.attendanceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/list_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.attendanceBtn.setIcon(icon6)
        self.attendanceBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.attendanceBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_16.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 144))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.settingsBtn = QPushButton(self.frame_4)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/settings_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon7)
        self.settingsBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.frame_4)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/help-circle_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon8)
        self.helpBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.helpBtn)

        self.aboutBtn = QPushButton(self.frame_4)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/info_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon9)
        self.aboutBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.aboutBtn)


        self.verticalLayout_16.addWidget(self.frame_4)

        self.frame_4.raise_()
        self.frame_3.raise_()

        self.verticalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainPages.sizePolicy().hasHeightForWidth())
        self.mainPages.setSizePolicy(sizePolicy1)
        self.mainPages.setMinimumSize(QSize(0, 0))
        self.mainPages.setMaximumSize(QSize(919, 1000))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_18 = QVBoxLayout(self.homePage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_11 = QFrame(self.homePage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.image = QLabel(self.frame_11)
        self.image.setObjectName(u"image")
        self.image.setPixmap(QPixmap(u":/icons/Icons/camera.png"))

        self.horizontalLayout_12.addWidget(self.image, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.frame_11)

        self.mainPages.addWidget(self.homePage)
        self.employeePage = QWidget()
        self.employeePage.setObjectName(u"employeePage")
        self.verticalLayout_5 = QVBoxLayout(self.employeePage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_5 = QWidget(self.employeePage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_17 = QVBoxLayout(self.widget_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_8 = QFrame(self.widget_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(26)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.label_3.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.deselectBtn = QPushButton(self.frame_9)
        self.deselectBtn.setObjectName(u"deselectBtn")
        self.deselectBtn.setFont(font2)
        self.deselectBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deselectBtn.setIcon(icon10)
        self.deselectBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.deselectBtn)

        self.fireBtn = QPushButton(self.frame_9)
        self.fireBtn.setObjectName(u"fireBtn")
        self.fireBtn.setEnabled(False)
        self.fireBtn.setFont(font2)
        self.fireBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/minus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fireBtn.setIcon(icon11)
        self.fireBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.fireBtn)

        self.editBtn = QPushButton(self.frame_9)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setEnabled(False)
        self.editBtn.setFont(font2)
        self.editBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editBtn.setIcon(icon12)
        self.editBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.editBtn, 0, Qt.AlignLeft)

        self.showEmployeeFormBtn = QPushButton(self.frame_9)
        self.showEmployeeFormBtn.setObjectName(u"showEmployeeFormBtn")
        self.showEmployeeFormBtn.setFont(font2)
        self.showEmployeeFormBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/plus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showEmployeeFormBtn.setIcon(icon13)
        self.showEmployeeFormBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.showEmployeeFormBtn)

        self.saveAttendanceBtn = QPushButton(self.frame_9)
        self.saveAttendanceBtn.setObjectName(u"saveAttendanceBtn")
        self.saveAttendanceBtn.setEnabled(False)
        self.saveAttendanceBtn.setFont(font2)
        self.saveAttendanceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveAttendanceBtn.setIcon(icon14)
        self.saveAttendanceBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.saveAttendanceBtn)


        self.horizontalLayout_10.addWidget(self.frame_9, 0, Qt.AlignRight)


        self.verticalLayout_17.addWidget(self.frame_8)

        self.tableWidget = QTableWidget(self.widget_5)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_17.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.widget_5)

        self.mainPages.addWidget(self.employeePage)
        self.attendancePage = QWidget()
        self.attendancePage.setObjectName(u"attendancePage")
        self.verticalLayout_19 = QVBoxLayout(self.attendancePage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_8 = QWidget(self.attendancePage)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setPointSize(26)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_4.setFont(font6)

        self.horizontalLayout_16.addWidget(self.label_4)

        self.frame_12 = QFrame(self.widget_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        font7 = QFont()
        font7.setPointSize(12)
        self.label_12.setFont(font7)

        self.horizontalLayout_17.addWidget(self.label_12, 0, Qt.AlignRight)

        self.aDate = QDateEdit(self.frame_12)
        self.aDate.setObjectName(u"aDate")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setWeight(50)
        self.aDate.setFont(font8)

        self.horizontalLayout_17.addWidget(self.aDate, 0, Qt.AlignLeft)


        self.horizontalLayout_16.addWidget(self.frame_12)


        self.verticalLayout_19.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.attendancePage)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_20 = QVBoxLayout(self.widget_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.attendanceTable = QTableWidget(self.widget_9)
        if (self.attendanceTable.columnCount() < 7):
            self.attendanceTable.setColumnCount(7)
        font9 = QFont()
        font9.setFamily(u"Castellar")
        font9.setPointSize(12)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font9);
        self.attendanceTable.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.attendanceTable.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.attendanceTable.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.attendanceTable.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.attendanceTable.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.attendanceTable.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.attendanceTable.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        self.attendanceTable.setObjectName(u"attendanceTable")
        self.attendanceTable.setEnabled(True)
        self.attendanceTable.setMaximumSize(QSize(883, 16777215))
        self.attendanceTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.attendanceTable.setTabKeyNavigation(False)
        self.attendanceTable.setProperty("showDropIndicator", False)
        self.attendanceTable.setDragDropOverwriteMode(False)

        self.verticalLayout_20.addWidget(self.attendanceTable)


        self.verticalLayout_19.addWidget(self.widget_9)

        self.mainPages.addWidget(self.attendancePage)
        self.saving_page = QWidget()
        self.saving_page.setObjectName(u"saving_page")
        self.verticalLayout_23 = QVBoxLayout(self.saving_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_10 = QWidget(self.saving_page)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)

        self.horizontalLayout_19.addWidget(self.label_11)

        self.frame_14 = QFrame(self.widget_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font7)

        self.horizontalLayout_20.addWidget(self.label_13, 0, Qt.AlignRight)

        self.paDate = QDateEdit(self.frame_14)
        self.paDate.setObjectName(u"paDate")
        self.paDate.setFont(font8)
        self.paDate.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_20.addWidget(self.paDate, 0, Qt.AlignLeft)


        self.horizontalLayout_19.addWidget(self.frame_14)


        self.verticalLayout_23.addWidget(self.widget_10)

        self.frame_17 = QFrame(self.saving_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_12 = QWidget(self.frame_17)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_25 = QVBoxLayout(self.widget_12)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.attendanceTable2 = QTableWidget(self.widget_12)
        if (self.attendanceTable2.columnCount() < 7):
            self.attendanceTable2.setColumnCount(7)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font9);
        self.attendanceTable2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.attendanceTable2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.attendanceTable2.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.attendanceTable2.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.attendanceTable2.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.attendanceTable2.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.attendanceTable2.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        self.attendanceTable2.setObjectName(u"attendanceTable2")
        self.attendanceTable2.setEnabled(True)
        self.attendanceTable2.setMaximumSize(QSize(883, 16777215))
        self.attendanceTable2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.attendanceTable2.setTabKeyNavigation(False)
        self.attendanceTable2.setProperty("showDropIndicator", False)
        self.attendanceTable2.setDragDropOverwriteMode(False)

        self.verticalLayout_25.addWidget(self.attendanceTable2)

        self.saveBtn = QPushButton(self.widget_12)
        self.saveBtn.setObjectName(u"saveBtn")
        font10 = QFont()
        font10.setFamily(u"MS Serif")
        font10.setPointSize(20)
        font10.setBold(True)
        font10.setWeight(75)
        self.saveBtn.setFont(font10)
        self.saveBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_25.addWidget(self.saveBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.widget_12)


        self.verticalLayout_23.addWidget(self.frame_17)

        self.mainPages.addWidget(self.saving_page)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_5 = QLabel(self.settingsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 160, 47, 13))
        self.mainPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.label_6 = QLabel(self.helpPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 100, 47, 13))
        self.mainPages.addWidget(self.helpPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.label_7 = QLabel(self.aboutPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(340, 170, 47, 13))
        self.mainPages.addWidget(self.aboutPage)

        self.horizontalLayout_8.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)

        self.rightMenu = QCustomSlideMenu(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.rightMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.rightMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 528))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 70))
        self.label.setMaximumSize(QSize(70, 70))
        self.label.setPixmap(QPixmap(u":/icons/Icons/edit_disabled.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_2 = QWidget(self.frame_5)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.idNumber = QLineEdit(self.widget_2)
        self.idNumber.setObjectName(u"idNumber")

        self.verticalLayout_8.addWidget(self.idNumber)

        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.firstName = QLineEdit(self.groupBox)
        self.firstName.setObjectName(u"firstName")

        self.verticalLayout_10.addWidget(self.firstName)

        self.middleName = QLineEdit(self.groupBox)
        self.middleName.setObjectName(u"middleName")

        self.verticalLayout_10.addWidget(self.middleName)

        self.lastName = QLineEdit(self.groupBox)
        self.lastName.setObjectName(u"lastName")

        self.verticalLayout_10.addWidget(self.lastName)

        self.prefix = QLineEdit(self.groupBox)
        self.prefix.setObjectName(u"prefix")

        self.verticalLayout_10.addWidget(self.prefix)


        self.verticalLayout_8.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.imgLbl = QLabel(self.groupBox_2)
        self.imgLbl.setObjectName(u"imgLbl")
        sizePolicy.setHeightForWidth(self.imgLbl.sizePolicy().hasHeightForWidth())
        self.imgLbl.setSizePolicy(sizePolicy)
        self.imgLbl.setMinimumSize(QSize(224, 224))
        self.imgLbl.setMaximumSize(QSize(224, 224))
        self.imgLbl.setPixmap(QPixmap(u":/icons/Icons/camera.png"))

        self.verticalLayout_11.addWidget(self.imgLbl, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.groupBox_2)


        self.horizontalLayout_5.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame_5)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_3 = QGroupBox(self.widget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_6 = QFrame(self.groupBox_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_6 = QGroupBox(self.frame_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.birthDate = QDateEdit(self.groupBox_6)
        self.birthDate.setObjectName(u"birthDate")
        self.birthDate.setCalendarPopup(True)

        self.verticalLayout_13.addWidget(self.birthDate)


        self.verticalLayout_12.addWidget(self.groupBox_6)

        self.gender = QGroupBox(self.frame_6)
        self.gender.setObjectName(u"gender")
        self.horizontalLayout_6 = QHBoxLayout(self.gender)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.male = QRadioButton(self.gender)
        self.male.setObjectName(u"male")

        self.horizontalLayout_6.addWidget(self.male)

        self.female = QRadioButton(self.gender)
        self.female.setObjectName(u"female")

        self.horizontalLayout_6.addWidget(self.female)


        self.verticalLayout_12.addWidget(self.gender)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.widget_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.email = QLineEdit(self.groupBox_4)
        self.email.setObjectName(u"email")

        self.verticalLayout_15.addWidget(self.email)

        self.mobileNumber = QLineEdit(self.groupBox_4)
        self.mobileNumber.setObjectName(u"mobileNumber")

        self.verticalLayout_15.addWidget(self.mobileNumber)


        self.verticalLayout_9.addWidget(self.groupBox_4)


        self.horizontalLayout_5.addWidget(self.widget_3)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_7.addWidget(self.progressBar)

        self.addEmployeeBtn = QPushButton(self.widget)
        self.addEmployeeBtn.setObjectName(u"addEmployeeBtn")
        self.addEmployeeBtn.setMinimumSize(QSize(0, 32))
        self.addEmployeeBtn.setMaximumSize(QSize(16777215, 32))
        font11 = QFont()
        font11.setBold(True)
        font11.setWeight(75)
        self.addEmployeeBtn.setFont(font11)
        self.addEmployeeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/file-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addEmployeeBtn.setIcon(icon15)
        self.addEmployeeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.addEmployeeBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.widget, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.rightMenu)


        self.verticalLayout_21.addWidget(self.mainBody)

        self.footer = QWidget(self.mainPage)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_9 = QHBoxLayout(self.footer)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.footer)
        self.label_8.setObjectName(u"label_8")
        font12 = QFont()
        font12.setFamily(u"MS PGothic")
        font12.setPointSize(8)
        font12.setBold(True)
        font12.setWeight(75)
        self.label_8.setFont(font12)

        self.horizontalLayout_9.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.footer)

        self.stackedWidget.addWidget(self.mainPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.userName.setText("")
        self.userName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.passCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"L o g I n", None))
        self.menuBtn.setText("")
        self.appName.setText(QCoreApplication.translate("MainWindow", u"My Application", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.logOutBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.employeeBtn.setText(QCoreApplication.translate("MainWindow", u"Employee's", None))
        self.attendanceBtn.setText(QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.image.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"EMPLOYEE", None))
        self.deselectBtn.setText(QCoreApplication.translate("MainWindow", u"Deselect", None))
        self.fireBtn.setText(QCoreApplication.translate("MainWindow", u"Fire", None))
        self.editBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.showEmployeeFormBtn.setText(QCoreApplication.translate("MainWindow", u"Hire", None))
        self.saveAttendanceBtn.setText(QCoreApplication.translate("MainWindow", u"Save Attendance", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Mobile Number", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ATTENDANCE", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        ___qtablewidgetitem4 = self.attendanceTable.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem5 = self.attendanceTable.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"AM Time-In", None));
        ___qtablewidgetitem6 = self.attendanceTable.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"AM Time-Out", None));
        ___qtablewidgetitem7 = self.attendanceTable.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"PM Time-In", None));
        ___qtablewidgetitem8 = self.attendanceTable.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"PM Time-Out", None));
        ___qtablewidgetitem9 = self.attendanceTable.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"OT Time-In", None));
        ___qtablewidgetitem10 = self.attendanceTable.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OT Time-Out", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Save Attendance", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.paDate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/yyyy", None))
        ___qtablewidgetitem11 = self.attendanceTable2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem12 = self.attendanceTable2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"AM Time-In", None));
        ___qtablewidgetitem13 = self.attendanceTable2.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"AM Time-Out", None));
        ___qtablewidgetitem14 = self.attendanceTable2.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"PM Time-In", None));
        ___qtablewidgetitem15 = self.attendanceTable2.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"PM Time-Out", None));
        ___qtablewidgetitem16 = self.attendanceTable2.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"OT Time-In", None));
        ___qtablewidgetitem17 = self.attendanceTable2.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"OT Time-Out", None));
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.label.setText("")
        self.idNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID NUMBER", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.firstName.setText("")
        self.firstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.middleName.setText("")
        self.middleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.lastName.setText("")
        self.lastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.prefix.setText("")
        self.prefix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prefix", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"IMAGES", None))
        self.imgLbl.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"OTHERS", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Birth Date", None))
        self.gender.setTitle(QCoreApplication.translate("MainWindow", u"Age", None))
        self.male.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.female.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"CONTACTS AND FOLDER ADDRESS", None))
        self.email.setText("")
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.mobileNumber.setText("")
        self.mobileNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mobile Number", None))
        self.addEmployeeBtn.setText(QCoreApplication.translate("MainWindow", u"HIRE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Marvin Caintic .... Copyright 2022", None))
    # retranslateUi

