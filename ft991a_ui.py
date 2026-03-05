# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ft991a.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QButtonGroup,
    QComboBox, QDial, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLCDNumber, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1220, 1180)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionSave_Radio_Menu = QAction(MainWindow)
        self.actionSave_Radio_Menu.setObjectName(u"actionSave_Radio_Menu")
        self.actionLoad_Radio_Menu = QAction(MainWindow)
        self.actionLoad_Radio_Menu.setObjectName(u"actionLoad_Radio_Menu")
        self.actionSave_Memory_Channel = QAction(MainWindow)
        self.actionSave_Memory_Channel.setObjectName(u"actionSave_Memory_Channel")
        self.actionLoad_Memory_Channel = QAction(MainWindow)
        self.actionLoad_Memory_Channel.setObjectName(u"actionLoad_Memory_Channel")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionRefresh_Radio_Menu = QAction(MainWindow)
        self.actionRefresh_Radio_Menu.setObjectName(u"actionRefresh_Radio_Menu")
        font = QFont()
        font.setPointSize(14)
        self.actionRefresh_Radio_Menu.setFont(font)
        self.actionRefresh_Memory_Channel = QAction(MainWindow)
        self.actionRefresh_Memory_Channel.setObjectName(u"actionRefresh_Memory_Channel")
        self.actionRefresh_Memory_Channel.setFont(font)
        self.actionRefresh_Settings = QAction(MainWindow)
        self.actionRefresh_Settings.setObjectName(u"actionRefresh_Settings")
        self.actionRefresh_Settings.setFont(font)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionRefresh_Equalizer = QAction(MainWindow)
        self.actionRefresh_Equalizer.setObjectName(u"actionRefresh_Equalizer")
        self.actionRefresh_Audio_Filter = QAction(MainWindow)
        self.actionRefresh_Audio_Filter.setObjectName(u"actionRefresh_Audio_Filter")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.Radio_tabWidget = QTabWidget(self.centralwidget)
        self.Radio_tabWidget.setObjectName(u"Radio_tabWidget")
        self.Radio_tabWidget.setGeometry(QRect(10, 5, 1201, 931))
        self.Radio_tabWidget.setFont(font)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setStyleSheet(u"QWidget{ background-color: gray}")
        self.VFO_A_groupBox = QGroupBox(self.tab_1)
        self.VFO_A_groupBox.setObjectName(u"VFO_A_groupBox")
        self.VFO_A_groupBox.setGeometry(QRect(20, 20, 651, 251))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.VFO_A_groupBox.setFont(font1)
        self.VFO_A_groupBox.setStyleSheet(u"QWidget{ border: 2px black; background-color: lightgray;border-radius: 20px;}")
        self.VFO_A_lcdNumber = QLCDNumber(self.VFO_A_groupBox)
        self.VFO_A_lcdNumber.setObjectName(u"VFO_A_lcdNumber")
        self.VFO_A_lcdNumber.setGeometry(QRect(20, 40, 401, 91))
        self.VFO_A_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;}\n"
"QLCDNumber {color: yellow;}\n"
"")
        self.VFO_A_lcdNumber.setSmallDecimalPoint(False)
        self.VFO_A_lcdNumber.setDigitCount(9)
        self.VFO_A_lcdNumber.setMode(QLCDNumber.Mode.Dec)
        self.VFO_A_lcdNumber.setProperty(u"intValue", 1800000)
        self.VFO_A_lineEdit = QLineEdit(self.VFO_A_groupBox)
        self.VFO_A_lineEdit.setObjectName(u"VFO_A_lineEdit")
        self.VFO_A_lineEdit.setGeometry(QRect(220, 140, 201, 51))
        font2 = QFont()
        font2.setPointSize(22)
        self.VFO_A_lineEdit.setFont(font2)
        self.VFO_A_lineEdit.setStyleSheet(u"QWidget{ border: 2px black; background-color: white;border-radius: 10px;}")
        self.VFO_A_lineEdit.setMaxLength(9)
        self.VFO_A_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.VFO_A_dial = QDial(self.VFO_A_groupBox)
        self.VFO_A_dial.setObjectName(u"VFO_A_dial")
        self.VFO_A_dial.setGeometry(QRect(480, 30, 151, 151))
        self.VFO_A_dial.setToolTipDuration(-1)
        self.VFO_A_dial.setTracking(True)
        self.VFO_A_dial.setWrapping(True)
        self.VFO_A_dial.setNotchesVisible(True)
        self.VFO_A_dial.setProperty(u"stored_value", 0)
        self.VFO_A_Tx_radioButton = QRadioButton(self.VFO_A_groupBox)
        self.Tx_buttonGroup = QButtonGroup(MainWindow)
        self.Tx_buttonGroup.setObjectName(u"Tx_buttonGroup")
        self.Tx_buttonGroup.addButton(self.VFO_A_Tx_radioButton)
        self.VFO_A_Tx_radioButton.setObjectName(u"VFO_A_Tx_radioButton")
        self.VFO_A_Tx_radioButton.setGeometry(QRect(20, 150, 41, 31))
        font3 = QFont()
        font3.setPointSize(16)
        self.VFO_A_Tx_radioButton.setFont(font3)
        self.VFO_A_Tx_radioButton.setStyleSheet(u"QRadioButton::indicator:checked:checked{ background-color: red;}\n"
"QRadioButton::indicator{ width: 10px; height: 10px; border-radius: 5px; border: 1px solid black; background-color: transparent;}")
        self.VFO_A_Tx_radioButton.setIconSize(QSize(32, 32))
        self.VFO_A_Tx_radioButton.setChecked(True)
        self.VFO_A_Rx_radioButton = QRadioButton(self.VFO_A_groupBox)
        self.Rx_buttonGroup = QButtonGroup(MainWindow)
        self.Rx_buttonGroup.setObjectName(u"Rx_buttonGroup")
        self.Rx_buttonGroup.addButton(self.VFO_A_Rx_radioButton)
        self.VFO_A_Rx_radioButton.setObjectName(u"VFO_A_Rx_radioButton")
        self.VFO_A_Rx_radioButton.setGeometry(QRect(70, 150, 41, 31))
        self.VFO_A_Rx_radioButton.setFont(font3)
        self.VFO_A_Rx_radioButton.setStyleSheet(u"QRadioButton::indicator:checked:checked{ background-color: green;}\n"
"QRadioButton::indicator{ width: 10px; height: 10px; border-radius: 5px; border: 1px solid black; background-color: transparent;}")
        self.VFO_A_Rx_radioButton.setIconSize(QSize(32, 32))
        self.VFO_A_Rx_radioButton.setChecked(True)
        self.VFO_A_label_1 = QLabel(self.VFO_A_groupBox)
        self.VFO_A_label_1.setObjectName(u"VFO_A_label_1")
        self.VFO_A_label_1.setGeometry(QRect(430, 100, 21, 18))
        self.VFO_A_label_1.setFont(font)
        self.VFO_A_label_2 = QLabel(self.VFO_A_groupBox)
        self.VFO_A_label_2.setObjectName(u"VFO_A_label_2")
        self.VFO_A_label_2.setGeometry(QRect(430, 165, 41, 18))
        self.VFO_A_label_2.setFont(font)
        self.VFO_A_textBrowser = QTextBrowser(self.VFO_A_groupBox)
        self.VFO_A_textBrowser.setObjectName(u"VFO_A_textBrowser")
        self.VFO_A_textBrowser.setGeometry(QRect(60, 200, 501, 41))
        font4 = QFont()
        font4.setFamilies([u"Monospace"])
        font4.setPointSize(12)
        self.VFO_A_textBrowser.setFont(font4)
        self.VFO_A_textBrowser.setStyleSheet(u"QWidget{ background-color: white;border-radius: 8px;}\n"
"QTextBrowser QScrollBar:horizontal {background-color: lightgrey;}\n"
"QTextBrowser QScrollBar::handle:horizontal {background-color: grey;margin: 0px 12px;}")
        self.VFO_A_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.VFO_A_textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.VFO_A_textBrowser.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.VFO_A_line_1 = QFrame(self.VFO_A_groupBox)
        self.VFO_A_line_1.setObjectName(u"VFO_A_line_1")
        self.VFO_A_line_1.setGeometry(QRect(145, 200, 3, 41))
        self.VFO_A_line_1.setFrameShape(QFrame.Shape.VLine)
        self.VFO_A_line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_A_line_2 = QFrame(self.VFO_A_groupBox)
        self.VFO_A_line_2.setObjectName(u"VFO_A_line_2")
        self.VFO_A_line_2.setGeometry(QRect(280, 200, 3, 41))
        self.VFO_A_line_2.setFrameShape(QFrame.Shape.VLine)
        self.VFO_A_line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_A_line_3 = QFrame(self.VFO_A_groupBox)
        self.VFO_A_line_3.setObjectName(u"VFO_A_line_3")
        self.VFO_A_line_3.setGeometry(QRect(415, 200, 3, 41))
        self.VFO_A_line_3.setFrameShape(QFrame.Shape.VLine)
        self.VFO_A_line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_A_label_3 = QLabel(self.VFO_A_groupBox)
        self.VFO_A_label_3.setObjectName(u"VFO_A_label_3")
        self.VFO_A_label_3.setGeometry(QRect(140, 145, 71, 41))
        font5 = QFont()
        font5.setPointSize(11)
        self.VFO_A_label_3.setFont(font5)
        self.VFO_A_label_3.setStyleSheet(u"QWidget{ border-radius: 0px;}")
        self.VFO_A_label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.VFO_A_label_3.setWordWrap(True)
        self.VFO_A_label_4 = QLabel(self.VFO_A_groupBox)
        self.VFO_A_label_4.setObjectName(u"VFO_A_label_4")
        self.VFO_A_label_4.setGeometry(QRect(10, 205, 41, 31))
        self.VFO_A_label_4.setFont(font5)
        self.VFO_A_label_4.setStyleSheet(u"QWidget{ border-radius: 0px;}")
        self.VFO_A_label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.VFO_A_label_4.setWordWrap(True)
        self.VFO_A_line_4 = QFrame(self.VFO_A_groupBox)
        self.VFO_A_line_4.setObjectName(u"VFO_A_line_4")
        self.VFO_A_line_4.setGeometry(QRect(283, 40, 3, 91))
        self.VFO_A_line_4.setFrameShape(QFrame.Shape.VLine)
        self.VFO_A_line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_A_line_5 = QFrame(self.VFO_A_groupBox)
        self.VFO_A_line_5.setObjectName(u"VFO_A_line_5")
        self.VFO_A_line_5.setGeometry(QRect(154, 40, 3, 91))
        self.VFO_A_line_5.setFrameShape(QFrame.Shape.VLine)
        self.VFO_A_line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_A_fast_radioButton = QRadioButton(self.VFO_A_groupBox)
        self.VFO_A_fast_radioButton.setObjectName(u"VFO_A_fast_radioButton")
        self.VFO_A_fast_radioButton.setGeometry(QRect(570, 5, 61, 31))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setItalic(True)
        self.VFO_A_fast_radioButton.setFont(font6)
        self.VFO_A_fast_radioButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.VFO_A_fast_radioButton.setStyleSheet(u"QRadioButton::indicator:checked:checked{ background-color: blue;}\n"
"QRadioButton::indicator{ width: 10px; height: 10px; border-radius: 5px; border: 1px solid black; background-color: transparent;}")
        self.VFO_A_fast_radioButton.setIconSize(QSize(32, 32))
        self.VFO_A_fast_radioButton.setChecked(False)
        self.VFO_B_groupBox = QGroupBox(self.tab_1)
        self.VFO_B_groupBox.setObjectName(u"VFO_B_groupBox")
        self.VFO_B_groupBox.setGeometry(QRect(20, 350, 651, 251))
        self.VFO_B_groupBox.setFont(font1)
        self.VFO_B_groupBox.setStyleSheet(u"QWidget{ border: 2px black; background-color: lightgray;border-radius: 20px;}")
        self.VFO_B_lcdNumber = QLCDNumber(self.VFO_B_groupBox)
        self.VFO_B_lcdNumber.setObjectName(u"VFO_B_lcdNumber")
        self.VFO_B_lcdNumber.setGeometry(QRect(20, 40, 401, 91))
        self.VFO_B_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;}\n"
"QLCDNumber {color: yellow;}\n"
"")
        self.VFO_B_lcdNumber.setDigitCount(9)
        self.VFO_B_lcdNumber.setProperty(u"intValue", 1800000)
        self.VFO_B_lineEdit = QLineEdit(self.VFO_B_groupBox)
        self.VFO_B_lineEdit.setObjectName(u"VFO_B_lineEdit")
        self.VFO_B_lineEdit.setGeometry(QRect(220, 140, 201, 51))
        self.VFO_B_lineEdit.setFont(font2)
        self.VFO_B_lineEdit.setStyleSheet(u"QWidget{ border: 2px black; background-color: white;border-radius: 10px;}")
        self.VFO_B_lineEdit.setMaxLength(9)
        self.VFO_B_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.VFO_B_dial = QDial(self.VFO_B_groupBox)
        self.VFO_B_dial.setObjectName(u"VFO_B_dial")
        self.VFO_B_dial.setGeometry(QRect(480, 30, 151, 151))
        self.VFO_B_dial.setWrapping(True)
        self.VFO_B_dial.setNotchesVisible(True)
        self.VFO_B_dial.setProperty(u"stored_value", 0)
        self.VFO_B_Tx_radioButton = QRadioButton(self.VFO_B_groupBox)
        self.Tx_buttonGroup.addButton(self.VFO_B_Tx_radioButton)
        self.VFO_B_Tx_radioButton.setObjectName(u"VFO_B_Tx_radioButton")
        self.VFO_B_Tx_radioButton.setGeometry(QRect(20, 150, 41, 31))
        self.VFO_B_Tx_radioButton.setFont(font3)
        self.VFO_B_Tx_radioButton.setStyleSheet(u"QRadioButton::indicator:checked:checked{ background-color: red;}\n"
"QRadioButton::indicator{ width: 10px; height: 10px; border-radius: 5px; border: 1px solid black; background-color: transparent;}")
        self.VFO_B_Tx_radioButton.setIconSize(QSize(32, 32))
        self.VFO_B_Rx_radioButton = QRadioButton(self.VFO_B_groupBox)
        self.Rx_buttonGroup.addButton(self.VFO_B_Rx_radioButton)
        self.VFO_B_Rx_radioButton.setObjectName(u"VFO_B_Rx_radioButton")
        self.VFO_B_Rx_radioButton.setEnabled(False)
        self.VFO_B_Rx_radioButton.setGeometry(QRect(70, 150, 41, 31))
        self.VFO_B_Rx_radioButton.setFont(font3)
        self.VFO_B_Rx_radioButton.setStyleSheet(u"QRadioButton::indicator:checked:checked{ background-color: green;}\n"
"QRadioButton::indicator{ width: 10px; height: 10px; border-radius: 5px; border: 1px solid black; background-color: transparent;}")
        self.VFO_B_Rx_radioButton.setIconSize(QSize(32, 32))
        self.VFO_B_label_1 = QLabel(self.VFO_B_groupBox)
        self.VFO_B_label_1.setObjectName(u"VFO_B_label_1")
        self.VFO_B_label_1.setGeometry(QRect(430, 100, 21, 18))
        self.VFO_B_label_1.setFont(font)
        self.VFO_B_label_2 = QLabel(self.VFO_B_groupBox)
        self.VFO_B_label_2.setObjectName(u"VFO_B_label_2")
        self.VFO_B_label_2.setGeometry(QRect(430, 165, 41, 18))
        self.VFO_B_label_2.setFont(font)
        self.VFO_B_textBrowser = QTextBrowser(self.VFO_B_groupBox)
        self.VFO_B_textBrowser.setObjectName(u"VFO_B_textBrowser")
        self.VFO_B_textBrowser.setGeometry(QRect(60, 200, 501, 41))
        self.VFO_B_textBrowser.setFont(font4)
        self.VFO_B_textBrowser.setStyleSheet(u"QWidget{ background-color: white;border-radius: 8px;}\n"
"QTextBrowser QScrollBar:horizontal {background-color: lightgrey;}\n"
"QTextBrowser QScrollBar::handle:horizontal {background-color: grey;margin: 0px 12px;}")
        self.VFO_B_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.VFO_B_textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.VFO_B_textBrowser.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.VFO_B_line_2 = QFrame(self.VFO_B_groupBox)
        self.VFO_B_line_2.setObjectName(u"VFO_B_line_2")
        self.VFO_B_line_2.setGeometry(QRect(280, 200, 3, 41))
        self.VFO_B_line_2.setFrameShape(QFrame.Shape.VLine)
        self.VFO_B_line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_B_line_3 = QFrame(self.VFO_B_groupBox)
        self.VFO_B_line_3.setObjectName(u"VFO_B_line_3")
        self.VFO_B_line_3.setGeometry(QRect(415, 200, 3, 41))
        self.VFO_B_line_3.setFrameShape(QFrame.Shape.VLine)
        self.VFO_B_line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_B_line_1 = QFrame(self.VFO_B_groupBox)
        self.VFO_B_line_1.setObjectName(u"VFO_B_line_1")
        self.VFO_B_line_1.setGeometry(QRect(145, 200, 3, 41))
        self.VFO_B_line_1.setFrameShape(QFrame.Shape.VLine)
        self.VFO_B_line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_B_label_3 = QLabel(self.VFO_B_groupBox)
        self.VFO_B_label_3.setObjectName(u"VFO_B_label_3")
        self.VFO_B_label_3.setGeometry(QRect(140, 145, 71, 41))
        self.VFO_B_label_3.setFont(font5)
        self.VFO_B_label_3.setStyleSheet(u"QWidget{ border-radius: 0px;}")
        self.VFO_B_label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.VFO_B_label_3.setWordWrap(True)
        self.VFO_B_label_4 = QLabel(self.VFO_B_groupBox)
        self.VFO_B_label_4.setObjectName(u"VFO_B_label_4")
        self.VFO_B_label_4.setGeometry(QRect(10, 205, 41, 31))
        self.VFO_B_label_4.setFont(font5)
        self.VFO_B_label_4.setStyleSheet(u"QWidget{ border-radius: 0px;}")
        self.VFO_B_label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.VFO_B_label_4.setWordWrap(True)
        self.VFO_B_line_5 = QFrame(self.VFO_B_groupBox)
        self.VFO_B_line_5.setObjectName(u"VFO_B_line_5")
        self.VFO_B_line_5.setGeometry(QRect(154, 40, 3, 91))
        self.VFO_B_line_5.setFrameShape(QFrame.Shape.VLine)
        self.VFO_B_line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_B_line_4 = QFrame(self.VFO_B_groupBox)
        self.VFO_B_line_4.setObjectName(u"VFO_B_line_4")
        self.VFO_B_line_4.setGeometry(QRect(283, 40, 3, 91))
        self.VFO_B_line_4.setFrameShape(QFrame.Shape.VLine)
        self.VFO_B_line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.VFO_B_fast_radioButton = QRadioButton(self.VFO_B_groupBox)
        self.VFO_B_fast_radioButton.setObjectName(u"VFO_B_fast_radioButton")
        self.VFO_B_fast_radioButton.setGeometry(QRect(570, 5, 61, 31))
        self.VFO_B_fast_radioButton.setFont(font6)
        self.VFO_B_fast_radioButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.VFO_B_fast_radioButton.setStyleSheet(u"QRadioButton::indicator:checked:checked {background-color: blue;}\n"
"QRadioButton::indicator {width: 10px; height: 10px; border-radius: 5px; border: 1px solid black; background-color: transparent;}")
        self.VFO_B_fast_radioButton.setIconSize(QSize(32, 32))
        self.VFO_B_fast_radioButton.setChecked(False)
        self.Band_groupBox = QGroupBox(self.tab_1)
        self.Band_groupBox.setObjectName(u"Band_groupBox")
        self.Band_groupBox.setGeometry(QRect(920, 20, 261, 301))
        self.Band_groupBox.setFont(font1)
        self.Band_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.band_pushButton_1 = QPushButton(self.Band_groupBox)
        self.band_pushButton_1.setObjectName(u"band_pushButton_1")
        self.band_pushButton_1.setGeometry(QRect(10, 40, 81, 41))
        font7 = QFont()
        font7.setPointSize(18)
        font7.setBold(True)
        self.band_pushButton_1.setFont(font7)
        self.band_pushButton_1.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_1.setCheckable(False)
        self.band_pushButton_2 = QPushButton(self.Band_groupBox)
        self.band_pushButton_2.setObjectName(u"band_pushButton_2")
        self.band_pushButton_2.setGeometry(QRect(90, 40, 81, 41))
        self.band_pushButton_2.setFont(font7)
        self.band_pushButton_2.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_2.setCheckable(False)
        self.band_pushButton_3 = QPushButton(self.Band_groupBox)
        self.band_pushButton_3.setObjectName(u"band_pushButton_3")
        self.band_pushButton_3.setGeometry(QRect(170, 40, 81, 41))
        self.band_pushButton_3.setFont(font7)
        self.band_pushButton_3.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_3.setCheckable(False)
        self.band_pushButton_4 = QPushButton(self.Band_groupBox)
        self.band_pushButton_4.setObjectName(u"band_pushButton_4")
        self.band_pushButton_4.setGeometry(QRect(10, 80, 81, 41))
        self.band_pushButton_4.setFont(font7)
        self.band_pushButton_4.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_4.setCheckable(False)
        self.band_pushButton_6 = QPushButton(self.Band_groupBox)
        self.band_pushButton_6.setObjectName(u"band_pushButton_6")
        self.band_pushButton_6.setGeometry(QRect(170, 80, 81, 41))
        self.band_pushButton_6.setFont(font7)
        self.band_pushButton_6.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_6.setCheckable(False)
        self.band_pushButton_5 = QPushButton(self.Band_groupBox)
        self.band_pushButton_5.setObjectName(u"band_pushButton_5")
        self.band_pushButton_5.setGeometry(QRect(90, 80, 81, 41))
        self.band_pushButton_5.setFont(font7)
        self.band_pushButton_5.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_5.setCheckable(False)
        self.band_pushButton_8 = QPushButton(self.Band_groupBox)
        self.band_pushButton_8.setObjectName(u"band_pushButton_8")
        self.band_pushButton_8.setGeometry(QRect(90, 120, 81, 41))
        self.band_pushButton_8.setFont(font7)
        self.band_pushButton_8.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_8.setCheckable(False)
        self.band_pushButton_7 = QPushButton(self.Band_groupBox)
        self.band_pushButton_7.setObjectName(u"band_pushButton_7")
        self.band_pushButton_7.setGeometry(QRect(10, 120, 81, 41))
        self.band_pushButton_7.setFont(font7)
        self.band_pushButton_7.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_7.setCheckable(False)
        self.band_pushButton_9 = QPushButton(self.Band_groupBox)
        self.band_pushButton_9.setObjectName(u"band_pushButton_9")
        self.band_pushButton_9.setGeometry(QRect(170, 120, 81, 41))
        self.band_pushButton_9.setFont(font7)
        self.band_pushButton_9.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_9.setCheckable(False)
        self.band_pushButton_10 = QPushButton(self.Band_groupBox)
        self.band_pushButton_10.setObjectName(u"band_pushButton_10")
        self.band_pushButton_10.setGeometry(QRect(90, 160, 81, 41))
        self.band_pushButton_10.setFont(font7)
        self.band_pushButton_10.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_10.setCheckable(False)
        self.band_pushButton_11 = QPushButton(self.Band_groupBox)
        self.band_pushButton_11.setObjectName(u"band_pushButton_11")
        self.band_pushButton_11.setGeometry(QRect(90, 200, 81, 41))
        self.band_pushButton_11.setFont(font7)
        self.band_pushButton_11.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_11.setCheckable(False)
        self.band_pushButton_12 = QPushButton(self.Band_groupBox)
        self.band_pushButton_12.setObjectName(u"band_pushButton_12")
        self.band_pushButton_12.setGeometry(QRect(170, 200, 81, 41))
        self.band_pushButton_12.setFont(font7)
        self.band_pushButton_12.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_12.setCheckable(False)
        self.band_pushButton_13 = QPushButton(self.Band_groupBox)
        self.band_pushButton_13.setObjectName(u"band_pushButton_13")
        self.band_pushButton_13.setGeometry(QRect(10, 200, 81, 41))
        self.band_pushButton_13.setFont(font7)
        self.band_pushButton_13.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_13.setCheckable(False)
        self.band_pushButton_14 = QPushButton(self.Band_groupBox)
        self.band_pushButton_14.setObjectName(u"band_pushButton_14")
        self.band_pushButton_14.setGeometry(QRect(170, 160, 81, 41))
        self.band_pushButton_14.setFont(font7)
        self.band_pushButton_14.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_14.setCheckable(False)
        self.band_pushButton_15 = QPushButton(self.Band_groupBox)
        self.band_pushButton_15.setObjectName(u"band_pushButton_15")
        self.band_pushButton_15.setGeometry(QRect(10, 160, 81, 41))
        self.band_pushButton_15.setFont(font7)
        self.band_pushButton_15.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.band_pushButton_15.setCheckable(False)
        self.PLL_lock_radioButton = QRadioButton(self.Band_groupBox)
        self.PLL_lock_radioButton.setObjectName(u"PLL_lock_radioButton")
        self.PLL_lock_radioButton.setEnabled(False)
        self.PLL_lock_radioButton.setGeometry(QRect(10, 260, 81, 31))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setItalic(False)
        self.PLL_lock_radioButton.setFont(font8)
        self.PLL_lock_radioButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.PLL_lock_radioButton.setStyleSheet(u"QRadioButton::indicator:checked:checked{ background-color: green;}\n"
"QRadioButton::indicator{ width: 10px; height: 10px; border-radius: 5px; border: 1px solid black; background-color: transparent;}")
        self.PLL_lock_radioButton.setIconSize(QSize(32, 32))
        self.PLL_lock_radioButton.setCheckable(True)
        self.PLL_lock_radioButton.setChecked(False)
        self.Mode_groupBox = QGroupBox(self.tab_1)
        self.Mode_groupBox.setObjectName(u"Mode_groupBox")
        self.Mode_groupBox.setGeometry(QRect(690, 20, 201, 301))
        self.Mode_groupBox.setFont(font1)
        self.Mode_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.mode_pushButton_1 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup = QButtonGroup(MainWindow)
        self.Mode_buttonGroup.setObjectName(u"Mode_buttonGroup")
        self.Mode_buttonGroup.addButton(self.mode_pushButton_1)
        self.mode_pushButton_1.setObjectName(u"mode_pushButton_1")
        self.mode_pushButton_1.setGeometry(QRect(20, 40, 81, 41))
        self.mode_pushButton_1.setFont(font7)
        self.mode_pushButton_1.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_1.setCheckable(True)
        self.mode_pushButton_2 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_2)
        self.mode_pushButton_2.setObjectName(u"mode_pushButton_2")
        self.mode_pushButton_2.setGeometry(QRect(100, 40, 81, 41))
        self.mode_pushButton_2.setFont(font7)
        self.mode_pushButton_2.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_2.setCheckable(True)
        self.mode_pushButton_3 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_3)
        self.mode_pushButton_3.setObjectName(u"mode_pushButton_3")
        self.mode_pushButton_3.setGeometry(QRect(20, 80, 81, 41))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.mode_pushButton_3.setFont(font9)
        self.mode_pushButton_3.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_3.setCheckable(True)
        self.mode_pushButton_4 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_4)
        self.mode_pushButton_4.setObjectName(u"mode_pushButton_4")
        self.mode_pushButton_4.setGeometry(QRect(100, 80, 81, 41))
        self.mode_pushButton_4.setFont(font9)
        self.mode_pushButton_4.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_4.setCheckable(True)
        self.mode_pushButton_5 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_5)
        self.mode_pushButton_5.setObjectName(u"mode_pushButton_5")
        self.mode_pushButton_5.setGeometry(QRect(20, 120, 81, 41))
        self.mode_pushButton_5.setFont(font9)
        self.mode_pushButton_5.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_5.setCheckable(True)
        self.mode_pushButton_6 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_6)
        self.mode_pushButton_6.setObjectName(u"mode_pushButton_6")
        self.mode_pushButton_6.setGeometry(QRect(100, 120, 81, 41))
        self.mode_pushButton_6.setFont(font9)
        self.mode_pushButton_6.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_6.setCheckable(True)
        self.mode_pushButton_7 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_7)
        self.mode_pushButton_7.setObjectName(u"mode_pushButton_7")
        self.mode_pushButton_7.setGeometry(QRect(20, 160, 81, 41))
        self.mode_pushButton_7.setFont(font9)
        self.mode_pushButton_7.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_7.setCheckable(True)
        self.mode_pushButton_8 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_8)
        self.mode_pushButton_8.setObjectName(u"mode_pushButton_8")
        self.mode_pushButton_8.setGeometry(QRect(100, 160, 81, 41))
        self.mode_pushButton_8.setFont(font9)
        self.mode_pushButton_8.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_8.setCheckable(True)
        self.mode_pushButton_9 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_9)
        self.mode_pushButton_9.setObjectName(u"mode_pushButton_9")
        self.mode_pushButton_9.setGeometry(QRect(20, 200, 81, 41))
        self.mode_pushButton_9.setFont(font7)
        self.mode_pushButton_9.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_9.setCheckable(True)
        self.mode_pushButton_10 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_10)
        self.mode_pushButton_10.setObjectName(u"mode_pushButton_10")
        self.mode_pushButton_10.setGeometry(QRect(100, 200, 81, 41))
        self.mode_pushButton_10.setFont(font7)
        self.mode_pushButton_10.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_10.setCheckable(True)
        self.mode_pushButton_11 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_11)
        self.mode_pushButton_11.setObjectName(u"mode_pushButton_11")
        self.mode_pushButton_11.setGeometry(QRect(20, 240, 81, 41))
        self.mode_pushButton_11.setFont(font7)
        self.mode_pushButton_11.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_11.setCheckable(True)
        self.mode_pushButton_12 = QPushButton(self.Mode_groupBox)
        self.Mode_buttonGroup.addButton(self.mode_pushButton_12)
        self.mode_pushButton_12.setObjectName(u"mode_pushButton_12")
        self.mode_pushButton_12.setGeometry(QRect(100, 240, 81, 41))
        self.mode_pushButton_12.setFont(font9)
        self.mode_pushButton_12.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.mode_pushButton_12.setCheckable(True)
        self.RF_groupBox = QGroupBox(self.tab_1)
        self.RF_groupBox.setObjectName(u"RF_groupBox")
        self.RF_groupBox.setGeometry(QRect(20, 610, 311, 271))
        self.RF_groupBox.setFont(font1)
        self.RF_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.RF_power_verticalSlider = QSlider(self.RF_groupBox)
        self.RF_power_verticalSlider.setObjectName(u"RF_power_verticalSlider")
        self.RF_power_verticalSlider.setGeometry(QRect(40, 80, 31, 141))
        self.RF_power_verticalSlider.setAutoFillBackground(False)
        self.RF_power_verticalSlider.setStyleSheet(u"QSlider::groove:vertical { background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: red;}")
        self.RF_power_verticalSlider.setMinimum(5)
        self.RF_power_verticalSlider.setMaximum(100)
        self.RF_power_verticalSlider.setPageStep(5)
        self.RF_power_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.RF_power_verticalSlider.setInvertedAppearance(False)
        self.RF_power_verticalSlider.setInvertedControls(False)
        self.RF_power_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.RF_power_verticalSlider.setTickInterval(5)
        self.AF_gain_verticalSlider = QSlider(self.RF_groupBox)
        self.AF_gain_verticalSlider.setObjectName(u"AF_gain_verticalSlider")
        self.AF_gain_verticalSlider.setGeometry(QRect(110, 80, 31, 141))
        self.AF_gain_verticalSlider.setAutoFillBackground(False)
        self.AF_gain_verticalSlider.setStyleSheet(u"QSlider::groove:vertical { background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: red;}")
        self.AF_gain_verticalSlider.setMinimum(0)
        self.AF_gain_verticalSlider.setMaximum(255)
        self.AF_gain_verticalSlider.setValue(0)
        self.AF_gain_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.AF_gain_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.AF_gain_verticalSlider.setTickInterval(5)
        self.RF_gain_verticalSlider = QSlider(self.RF_groupBox)
        self.RF_gain_verticalSlider.setObjectName(u"RF_gain_verticalSlider")
        self.RF_gain_verticalSlider.setGeometry(QRect(180, 80, 31, 141))
        self.RF_gain_verticalSlider.setAutoFillBackground(False)
        self.RF_gain_verticalSlider.setStyleSheet(u"QSlider::groove:vertical { background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: red;}")
        self.RF_gain_verticalSlider.setMinimum(0)
        self.RF_gain_verticalSlider.setMaximum(255)
        self.RF_gain_verticalSlider.setValue(0)
        self.RF_gain_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.RF_gain_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.RF_gain_verticalSlider.setTickInterval(5)
        self.RF_power_lcdNumber = QLCDNumber(self.RF_groupBox)
        self.RF_power_lcdNumber.setObjectName(u"RF_power_lcdNumber")
        self.RF_power_lcdNumber.setGeometry(QRect(30, 40, 51, 31))
        self.RF_power_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.RF_power_lcdNumber.setDigitCount(3)
        self.RF_power_lcdNumber.setProperty(u"intValue", 5)
        self.AF_gain_lcdNumber = QLCDNumber(self.RF_groupBox)
        self.AF_gain_lcdNumber.setObjectName(u"AF_gain_lcdNumber")
        self.AF_gain_lcdNumber.setGeometry(QRect(100, 40, 51, 31))
        self.AF_gain_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.AF_gain_lcdNumber.setDigitCount(3)
        self.RF_gain_lcdNumber = QLCDNumber(self.RF_groupBox)
        self.RF_gain_lcdNumber.setObjectName(u"RF_gain_lcdNumber")
        self.RF_gain_lcdNumber.setGeometry(QRect(170, 40, 51, 31))
        self.RF_gain_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.RF_gain_lcdNumber.setDigitCount(3)
        self.RF_label_1 = QLabel(self.RF_groupBox)
        self.RF_label_1.setObjectName(u"RF_label_1")
        self.RF_label_1.setGeometry(QRect(20, 230, 71, 21))
        self.RF_label_1.setFont(font9)
        self.RF_label_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.RF_label_1.setWordWrap(True)
        self.RF_label_2 = QLabel(self.RF_groupBox)
        self.RF_label_2.setObjectName(u"RF_label_2")
        self.RF_label_2.setGeometry(QRect(95, 230, 61, 21))
        self.RF_label_2.setFont(font9)
        self.RF_label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.RF_label_2.setWordWrap(True)
        self.RF_label_3 = QLabel(self.RF_groupBox)
        self.RF_label_3.setObjectName(u"RF_label_3")
        self.RF_label_3.setGeometry(QRect(165, 230, 61, 21))
        self.RF_label_3.setFont(font9)
        self.RF_label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.RF_label_3.setWordWrap(True)
        self.RF_squelch_verticalSlider = QSlider(self.RF_groupBox)
        self.RF_squelch_verticalSlider.setObjectName(u"RF_squelch_verticalSlider")
        self.RF_squelch_verticalSlider.setGeometry(QRect(250, 80, 31, 141))
        self.RF_squelch_verticalSlider.setAutoFillBackground(False)
        self.RF_squelch_verticalSlider.setStyleSheet(u"QSlider::groove:vertical { background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: red;}")
        self.RF_squelch_verticalSlider.setMinimum(0)
        self.RF_squelch_verticalSlider.setMaximum(100)
        self.RF_squelch_verticalSlider.setValue(0)
        self.RF_squelch_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.RF_squelch_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.RF_squelch_verticalSlider.setTickInterval(5)
        self.RF_squelch_lcdNumber = QLCDNumber(self.RF_groupBox)
        self.RF_squelch_lcdNumber.setObjectName(u"RF_squelch_lcdNumber")
        self.RF_squelch_lcdNumber.setGeometry(QRect(240, 40, 51, 31))
        self.RF_squelch_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.RF_squelch_lcdNumber.setDigitCount(3)
        self.RF_label_4 = QLabel(self.RF_groupBox)
        self.RF_label_4.setObjectName(u"RF_label_4")
        self.RF_label_4.setGeometry(QRect(230, 230, 71, 21))
        self.RF_label_4.setFont(font9)
        self.RF_label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.RF_label_4.setWordWrap(True)
        self.Meter_groupBox = QGroupBox(self.tab_1)
        self.Meter_groupBox.setObjectName(u"Meter_groupBox")
        self.Meter_groupBox.setGeometry(QRect(350, 610, 321, 271))
        self.Meter_groupBox.setFont(font1)
        self.Meter_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.S_meter_progressBar = QProgressBar(self.Meter_groupBox)
        self.S_meter_progressBar.setObjectName(u"S_meter_progressBar")
        self.S_meter_progressBar.setGeometry(QRect(41, 35, 261, 41))
        font10 = QFont()
        font10.setFamilies([u"Liberation Mono"])
        font10.setPointSize(18)
        font10.setBold(True)
        self.S_meter_progressBar.setFont(font10)
        self.S_meter_progressBar.setStyleSheet(u"QProgressBar {border: 2px solid black; border-radius: 2px; text-align: center; background: white;}\n"
"QProgressBar::chunk {background: green; border-radius: 0px; margin: 0px;}")
        self.S_meter_progressBar.setMaximum(255)
        self.S_meter_progressBar.setValue(0)
        self.S_meter_progressBar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.S_meter_progressBar.setTextVisible(True)
        self.S_meter_progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.S_meter_progressBar.setProperty(u"peak", 0)
        self.S_meter_progressBar.setProperty(u"average", 0)
        self.S_meter_progressBar.setProperty(u"hold", 0)
        self.S_meter_progressBar.setProperty(u"samples", u"")
        self.S_meter_label_1 = QLabel(self.Meter_groupBox)
        self.S_meter_label_1.setObjectName(u"S_meter_label_1")
        self.S_meter_label_1.setGeometry(QRect(40, 70, 274, 41))
        self.S_meter_label_1.setPixmap(QPixmap(u":/data/resources/meter_S_grid.png"))
        self.S_meter_label_1.setScaledContents(True)
        self.S_meter_label_2 = QLabel(self.Meter_groupBox)
        self.S_meter_label_2.setObjectName(u"S_meter_label_2")
        self.S_meter_label_2.setGeometry(QRect(5, 40, 31, 31))
        self.S_meter_label_2.setFont(font7)
        self.S_meter_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.S_meter_label_2.setWordWrap(True)
        self.PO_meter_progressBar = QProgressBar(self.Meter_groupBox)
        self.PO_meter_progressBar.setObjectName(u"PO_meter_progressBar")
        self.PO_meter_progressBar.setGeometry(QRect(40, 125, 261, 41))
        self.PO_meter_progressBar.setFont(font10)
        self.PO_meter_progressBar.setStyleSheet(u"QProgressBar {border: 2px solid black; border-radius: 2px; text-align: center; background: white;}\n"
"QProgressBar::chunk {background: green; border-radius: 0px; margin: 0px;}")
        self.PO_meter_progressBar.setMaximum(255)
        self.PO_meter_progressBar.setValue(0)
        self.PO_meter_progressBar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.PO_meter_progressBar.setTextVisible(True)
        self.PO_meter_progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.PO_meter_progressBar.setProperty(u"peak", 0)
        self.PO_meter_progressBar.setProperty(u"average", 0)
        self.PO_meter_progressBar.setProperty(u"hold", 0)
        self.PO_meter_label_2 = QLabel(self.Meter_groupBox)
        self.PO_meter_label_2.setObjectName(u"PO_meter_label_2")
        self.PO_meter_label_2.setGeometry(QRect(5, 130, 31, 31))
        self.PO_meter_label_2.setFont(font7)
        self.PO_meter_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.PO_meter_label_2.setWordWrap(True)
        self.PO_meter_label_1 = QLabel(self.Meter_groupBox)
        self.PO_meter_label_1.setObjectName(u"PO_meter_label_1")
        self.PO_meter_label_1.setGeometry(QRect(34, 160, 282, 41))
        self.PO_meter_label_1.setPixmap(QPixmap(u":/data/resources/meter_PO_grid.png"))
        self.PO_meter_label_1.setScaledContents(True)
        self.PO_meter_label_1.raise_()
        self.S_meter_label_1.raise_()
        self.S_meter_progressBar.raise_()
        self.S_meter_label_2.raise_()
        self.PO_meter_progressBar.raise_()
        self.PO_meter_label_2.raise_()
        self.Clar_groupBox = QGroupBox(self.tab_1)
        self.Clar_groupBox.setObjectName(u"Clar_groupBox")
        self.Clar_groupBox.setGeometry(QRect(690, 350, 201, 251))
        self.Clar_groupBox.setFont(font1)
        self.Clar_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Clar_lcdNumber = QLCDNumber(self.Clar_groupBox)
        self.Clar_lcdNumber.setObjectName(u"Clar_lcdNumber")
        self.Clar_lcdNumber.setGeometry(QRect(20, 55, 81, 31))
        self.Clar_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.Clar_lcdNumber.setDigitCount(5)
        self.Clar_dial = QDial(self.Clar_groupBox)
        self.Clar_dial.setObjectName(u"Clar_dial")
        self.Clar_dial.setGeometry(QRect(110, 30, 81, 81))
        self.Clar_dial.setWrapping(True)
        self.Clar_dial.setNotchesVisible(True)
        self.Clar_dial.setProperty(u"stored_value", 0)
        self.Clar_clear_pushButton = QPushButton(self.Clar_groupBox)
        self.Clar_clear_pushButton.setObjectName(u"Clar_clear_pushButton")
        self.Clar_clear_pushButton.setGeometry(QRect(115, 120, 71, 31))
        self.Clar_clear_pushButton.setFont(font1)
        self.Clar_clear_pushButton.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.Clar_comboBox = QComboBox(self.Clar_groupBox)
        self.Clar_comboBox.addItem("")
        self.Clar_comboBox.addItem("")
        self.Clar_comboBox.addItem("")
        self.Clar_comboBox.addItem("")
        self.Clar_comboBox.setObjectName(u"Clar_comboBox")
        self.Clar_comboBox.setGeometry(QRect(20, 120, 71, 31))
        self.Clar_comboBox.setEditable(False)
        self.Squelch_groupBox = QGroupBox(self.tab_1)
        self.Squelch_groupBox.setObjectName(u"Squelch_groupBox")
        self.Squelch_groupBox.setGeometry(QRect(920, 350, 261, 251))
        self.Squelch_groupBox.setFont(font1)
        self.Squelch_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Squelch_label_1 = QLabel(self.Squelch_groupBox)
        self.Squelch_label_1.setObjectName(u"Squelch_label_1")
        self.Squelch_label_1.setGeometry(QRect(10, 40, 71, 31))
        self.Squelch_label_1.setFont(font9)
        self.Squelch_label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Squelch_label_1.setWordWrap(True)
        self.Squelch_label_2 = QLabel(self.Squelch_groupBox)
        self.Squelch_label_2.setObjectName(u"Squelch_label_2")
        self.Squelch_label_2.setGeometry(QRect(10, 80, 71, 31))
        self.Squelch_label_2.setFont(font9)
        self.Squelch_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Squelch_label_2.setWordWrap(True)
        self.Squelch_CTCSS_comboBox = QComboBox(self.Squelch_groupBox)
        self.Squelch_CTCSS_comboBox.setObjectName(u"Squelch_CTCSS_comboBox")
        self.Squelch_CTCSS_comboBox.setGeometry(QRect(98, 40, 101, 31))
        self.Squelch_CTCSS_comboBox.setStyleSheet(u"")
        self.Squelch_DCS_comboBox = QComboBox(self.Squelch_groupBox)
        self.Squelch_DCS_comboBox.setObjectName(u"Squelch_DCS_comboBox")
        self.Squelch_DCS_comboBox.setGeometry(QRect(98, 80, 101, 31))
        self.Squelch_label_3 = QLabel(self.Squelch_groupBox)
        self.Squelch_label_3.setObjectName(u"Squelch_label_3")
        self.Squelch_label_3.setGeometry(QRect(10, 120, 71, 31))
        self.Squelch_label_3.setFont(font9)
        self.Squelch_label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Squelch_label_3.setWordWrap(True)
        self.Squelch_offset_comboBox = QComboBox(self.Squelch_groupBox)
        self.Squelch_offset_comboBox.addItem("")
        self.Squelch_offset_comboBox.addItem("")
        self.Squelch_offset_comboBox.addItem("")
        self.Squelch_offset_comboBox.setObjectName(u"Squelch_offset_comboBox")
        self.Squelch_offset_comboBox.setGeometry(QRect(98, 120, 141, 31))
        self.Squelch_label_4 = QLabel(self.Squelch_groupBox)
        self.Squelch_label_4.setObjectName(u"Squelch_label_4")
        self.Squelch_label_4.setGeometry(QRect(10, 160, 71, 31))
        self.Squelch_label_4.setFont(font9)
        self.Squelch_label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Squelch_label_4.setWordWrap(True)
        self.Squelch_mode_comboBox = QComboBox(self.Squelch_groupBox)
        self.Squelch_mode_comboBox.addItem("")
        self.Squelch_mode_comboBox.addItem("")
        self.Squelch_mode_comboBox.addItem("")
        self.Squelch_mode_comboBox.addItem("")
        self.Squelch_mode_comboBox.addItem("")
        self.Squelch_mode_comboBox.setObjectName(u"Squelch_mode_comboBox")
        self.Squelch_mode_comboBox.setGeometry(QRect(100, 160, 141, 31))
        self.VFO_frame = QFrame(self.tab_1)
        self.VFO_frame.setObjectName(u"VFO_frame")
        self.VFO_frame.setGeometry(QRect(20, 280, 281, 61))
        self.VFO_frame.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.VFO_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.VFO_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.A_B_pushButton_3 = QPushButton(self.VFO_frame)
        self.A_B_pushButton_3.setObjectName(u"A_B_pushButton_3")
        self.A_B_pushButton_3.setGeometry(QRect(180, 10, 81, 41))
        self.A_B_pushButton_3.setFont(font7)
        self.A_B_pushButton_3.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.A_B_pushButton_3.setCheckable(True)
        self.A_B_pushButton_3.setFlat(False)
        self.A_B_pushButton_2 = QPushButton(self.VFO_frame)
        self.A_B_pushButton_2.setObjectName(u"A_B_pushButton_2")
        self.A_B_pushButton_2.setGeometry(QRect(100, 10, 81, 41))
        self.A_B_pushButton_2.setFont(font7)
        self.A_B_pushButton_2.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.A_B_pushButton_2.setFlat(False)
        self.A_B_pushButton_1 = QPushButton(self.VFO_frame)
        self.A_B_pushButton_1.setObjectName(u"A_B_pushButton_1")
        self.A_B_pushButton_1.setGeometry(QRect(20, 10, 81, 41))
        self.A_B_pushButton_1.setFont(font7)
        self.A_B_pushButton_1.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.A_B_pushButton_1.setFlat(False)
        self.Memory_groupBox = QGroupBox(self.tab_1)
        self.Memory_groupBox.setObjectName(u"Memory_groupBox")
        self.Memory_groupBox.setGeometry(QRect(689, 610, 491, 271))
        self.Memory_groupBox.setFont(font1)
        self.Memory_groupBox.setToolTipDuration(-1)
        self.Memory_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Memory_tableWidget = QTableWidget(self.Memory_groupBox)
        if (self.Memory_tableWidget.columnCount() < 8):
            self.Memory_tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Memory_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Memory_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Memory_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Memory_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Memory_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Memory_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Memory_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Memory_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.Memory_tableWidget.rowCount() < 99):
            self.Memory_tableWidget.setRowCount(99)
        self.Memory_tableWidget.setObjectName(u"Memory_tableWidget")
        self.Memory_tableWidget.setGeometry(QRect(10, 30, 471, 181))
        font11 = QFont()
        font11.setFamilies([u"Monospace"])
        self.Memory_tableWidget.setFont(font11)
        self.Memory_tableWidget.setStyleSheet(u"")
        self.Memory_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Memory_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Memory_tableWidget.setAutoScroll(False)
        self.Memory_tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.Memory_tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.Memory_tableWidget.setRowCount(99)
        self.Memory_tableWidget.setColumnCount(8)
        self.Memory_tableWidget.horizontalHeader().setVisible(True)
        self.Memory_AM_pushButton = QPushButton(self.Memory_groupBox)
        self.Memory_AM_pushButton.setObjectName(u"Memory_AM_pushButton")
        self.Memory_AM_pushButton.setGeometry(QRect(70, 220, 61, 41))
        font12 = QFont()
        font12.setPointSize(16)
        font12.setBold(True)
        self.Memory_AM_pushButton.setFont(font12)
        self.Memory_AM_pushButton.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.Memory_AM_pushButton.setCheckable(False)
        self.Memory_AM_pushButton.setFlat(False)
        self.Memory_VM_pushButton = QPushButton(self.Memory_groupBox)
        self.Memory_VM_pushButton.setObjectName(u"Memory_VM_pushButton")
        self.Memory_VM_pushButton.setGeometry(QRect(10, 220, 61, 41))
        self.Memory_VM_pushButton.setFont(font12)
        self.Memory_VM_pushButton.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.Memory_VM_pushButton.setCheckable(True)
        self.Memory_VM_pushButton.setFlat(False)
        self.Memory_scan_up_pushButton = QPushButton(self.Memory_groupBox)
        self.Memory_scan_up_pushButton.setObjectName(u"Memory_scan_up_pushButton")
        self.Memory_scan_up_pushButton.setGeometry(QRect(290, 220, 61, 41))
        self.Memory_scan_up_pushButton.setFont(font1)
        self.Memory_scan_up_pushButton.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.Memory_scan_up_pushButton.setCheckable(False)
        self.Memory_scan_up_pushButton.setFlat(False)
        self.Memory_scan_down_pushButton = QPushButton(self.Memory_groupBox)
        self.Memory_scan_down_pushButton.setObjectName(u"Memory_scan_down_pushButton")
        self.Memory_scan_down_pushButton.setGeometry(QRect(350, 220, 61, 41))
        self.Memory_scan_down_pushButton.setFont(font1)
        self.Memory_scan_down_pushButton.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.Memory_scan_down_pushButton.setCheckable(False)
        self.Memory_scan_down_pushButton.setFlat(False)
        self.Memory_scan_stop_pushButton = QPushButton(self.Memory_groupBox)
        self.Memory_scan_stop_pushButton.setObjectName(u"Memory_scan_stop_pushButton")
        self.Memory_scan_stop_pushButton.setGeometry(QRect(410, 220, 61, 41))
        self.Memory_scan_stop_pushButton.setFont(font1)
        self.Memory_scan_stop_pushButton.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::pressed {background-color: red;}")
        self.Memory_scan_stop_pushButton.setCheckable(False)
        self.Memory_scan_stop_pushButton.setFlat(False)
        self.Radio_tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"QWidget{ background-color: gray}")
        self.Notch_groupBox = QGroupBox(self.tab_2)
        self.Notch_groupBox.setObjectName(u"Notch_groupBox")
        self.Notch_groupBox.setGeometry(QRect(750, 20, 421, 141))
        self.Notch_groupBox.setFont(font1)
        self.Notch_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Notch_freq_horizontalSlider = QSlider(self.Notch_groupBox)
        self.Notch_freq_horizontalSlider.setObjectName(u"Notch_freq_horizontalSlider")
        self.Notch_freq_horizontalSlider.setGeometry(QRect(70, 40, 201, 31))
        self.Notch_freq_horizontalSlider.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Notch_freq_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}\n"
"QSlider:disabled{color: darkgrey;}\n"
"QSlider:handle:disabled{background-color: darkgrey;  color: darkgrey;}")
        self.Notch_freq_horizontalSlider.setMinimum(1)
        self.Notch_freq_horizontalSlider.setMaximum(320)
        self.Notch_freq_horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.Notch_pushButton = QPushButton(self.Notch_groupBox)
        self.Notch_pushButton.setObjectName(u"Notch_pushButton")
        self.Notch_pushButton.setGeometry(QRect(290, 40, 91, 31))
        self.Notch_pushButton.setFont(font1)
        self.Notch_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.Notch_pushButton.setCheckable(True)
        self.Notch_freq_lcdNumber = QLCDNumber(self.Notch_groupBox)
        self.Notch_freq_lcdNumber.setObjectName(u"Notch_freq_lcdNumber")
        self.Notch_freq_lcdNumber.setGeometry(QRect(290, 80, 81, 41))
        self.Notch_freq_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.Notch_freq_lcdNumber.setDigitCount(4)
        self.Notch_label_1 = QLabel(self.Notch_groupBox)
        self.Notch_label_1.setObjectName(u"Notch_label_1")
        self.Notch_label_1.setGeometry(QRect(380, 105, 21, 18))
        self.Notch_label_1.setFont(font)
        self.Notch_line = QFrame(self.Notch_groupBox)
        self.Notch_line.setObjectName(u"Notch_line")
        self.Notch_line.setGeometry(QRect(290, 130, 80, 3))
        self.Notch_line.setStyleSheet(u"QFrame{ border: none; background-color: red;}")
        self.Notch_line.setFrameShape(QFrame.Shape.HLine)
        self.Notch_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.Notch_label_2 = QLabel(self.Notch_groupBox)
        self.Notch_label_2.setObjectName(u"Notch_label_2")
        self.Notch_label_2.setGeometry(QRect(10, 40, 41, 31))
        self.Notch_label_2.setFont(font9)
        self.Notch_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Contour_groupBox = QGroupBox(self.tab_2)
        self.Contour_groupBox.setObjectName(u"Contour_groupBox")
        self.Contour_groupBox.setGeometry(QRect(750, 180, 421, 141))
        self.Contour_groupBox.setFont(font1)
        self.Contour_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Contour_freq_horizontalSlider = QSlider(self.Contour_groupBox)
        self.Contour_freq_horizontalSlider.setObjectName(u"Contour_freq_horizontalSlider")
        self.Contour_freq_horizontalSlider.setGeometry(QRect(70, 40, 201, 31))
        self.Contour_freq_horizontalSlider.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Contour_freq_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}\n"
"QSlider:disabled{color: darkgrey;}\n"
"QSlider:handle:disabled{background-color: darkgrey;  color: darkgrey;}")
        self.Contour_freq_horizontalSlider.setMinimum(1)
        self.Contour_freq_horizontalSlider.setMaximum(320)
        self.Contour_freq_horizontalSlider.setValue(1)
        self.Contour_freq_horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.Contour_pushButton = QPushButton(self.Contour_groupBox)
        self.Contour_pushButton.setObjectName(u"Contour_pushButton")
        self.Contour_pushButton.setGeometry(QRect(290, 40, 91, 31))
        self.Contour_pushButton.setFont(font1)
        self.Contour_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.Contour_pushButton.setCheckable(True)
        self.Contour_freq_lcdNumber = QLCDNumber(self.Contour_groupBox)
        self.Contour_freq_lcdNumber.setObjectName(u"Contour_freq_lcdNumber")
        self.Contour_freq_lcdNumber.setGeometry(QRect(290, 80, 81, 41))
        self.Contour_freq_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.Contour_freq_lcdNumber.setDigitCount(4)
        self.Contour_label_1 = QLabel(self.Contour_groupBox)
        self.Contour_label_1.setObjectName(u"Contour_label_1")
        self.Contour_label_1.setGeometry(QRect(380, 105, 21, 18))
        self.Contour_label_1.setFont(font)
        self.Contour_line = QFrame(self.Contour_groupBox)
        self.Contour_line.setObjectName(u"Contour_line")
        self.Contour_line.setGeometry(QRect(290, 130, 80, 3))
        self.Contour_line.setStyleSheet(u"QFrame{ border: none; background-color: blue;}")
        self.Contour_line.setFrameShape(QFrame.Shape.HLine)
        self.Contour_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.Contour_BW_spinBox = QSpinBox(self.Contour_groupBox)
        self.Contour_BW_spinBox.setObjectName(u"Contour_BW_spinBox")
        self.Contour_BW_spinBox.setGeometry(QRect(60, 90, 61, 41))
        self.Contour_BW_spinBox.setFont(font)
        self.Contour_BW_spinBox.setStyleSheet(u"QSpinBox{ background-color: white;}\n"
"#QSpinBox::up-button{  background-color: lightgreen; min-width: 20px; min-height: 15px;}\n"
"#QSpinBox::down-button{ background-color: lightgreen; min-width: 20px; min-height: 15px;}\n"
"#QSpinBox::up-button:hover{ background-color: red;}\n"
"#QSpinBox::down-button:hover{ background-color: red;}\n"
"#QSpinBox::up-arrow{ border-left: 5px solid none; border-right: 5px solid none; border-bottom: 5px solid black; width: 0px; height: 0px;}\n"
"#QSpinBox::down-arrow{ border-left: 5px solid none; border-right: 5px solid none; border-top: 5px solid black; width: 0px; height: 0px;}")
        self.Contour_BW_spinBox.setMinimum(1)
        self.Contour_BW_spinBox.setMaximum(11)
        self.Contour_level_spinBox = QSpinBox(self.Contour_groupBox)
        self.Contour_level_spinBox.setObjectName(u"Contour_level_spinBox")
        self.Contour_level_spinBox.setGeometry(QRect(210, 90, 61, 41))
        self.Contour_level_spinBox.setFont(font)
        self.Contour_level_spinBox.setStyleSheet(u"QSpinBox{ background-color: white;}\n"
"#QSpinBox::up-button{ background-color: lightgreen;  min-width: 20px; min-height: 15px;}\n"
"#QSpinBox::up-button:hover{ background-color: red;}\n"
"#QSpinBox::down-button{ background-color: lightgreen; min-width: 20px; min-height: 15px;}\n"
"#QSpinBox::down-button:hover{ background-color: red;}\n"
"#QSpinBox::up-arrow{ border-left: 5px solid none; border-right: 5px solid none; border-bottom: 5px solid black; width: 0px; height: 0px;}\n"
"#QSpinBox::down-arrow{ border-left: 5px solid none; border-right: 5px solid none; border-top: 5px solid black; width: 0px; height: 0px;}")
        self.Contour_level_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.Contour_level_spinBox.setAccelerated(True)
        self.Contour_level_spinBox.setMinimum(-40)
        self.Contour_level_spinBox.setMaximum(20)
        self.Contour_label_2 = QLabel(self.Contour_groupBox)
        self.Contour_label_2.setObjectName(u"Contour_label_2")
        self.Contour_label_2.setGeometry(QRect(20, 95, 31, 31))
        self.Contour_label_2.setFont(font9)
        self.Contour_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Contour_label_3 = QLabel(self.Contour_groupBox)
        self.Contour_label_3.setObjectName(u"Contour_label_3")
        self.Contour_label_3.setGeometry(QRect(150, 95, 51, 31))
        self.Contour_label_3.setFont(font9)
        self.Contour_label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Contour_label_4 = QLabel(self.Contour_groupBox)
        self.Contour_label_4.setObjectName(u"Contour_label_4")
        self.Contour_label_4.setGeometry(QRect(10, 40, 41, 31))
        self.Contour_label_4.setFont(font9)
        self.Contour_label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.IF_filter_groupBox = QGroupBox(self.tab_2)
        self.IF_filter_groupBox.setObjectName(u"IF_filter_groupBox")
        self.IF_filter_groupBox.setGeometry(QRect(750, 340, 421, 201))
        self.IF_filter_groupBox.setFont(font1)
        self.IF_filter_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.IF_filter_shift_horizontalSlider = QSlider(self.IF_filter_groupBox)
        self.IF_filter_shift_horizontalSlider.setObjectName(u"IF_filter_shift_horizontalSlider")
        self.IF_filter_shift_horizontalSlider.setGeometry(QRect(70, 40, 201, 31))
        self.IF_filter_shift_horizontalSlider.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IF_filter_shift_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}\n"
"QSlider:disabled{color: darkgrey;}\n"
"QSlider:handle:disabled{background-color: darkgrey;  color: darkgrey;}")
        self.IF_filter_shift_horizontalSlider.setMinimum(-60)
        self.IF_filter_shift_horizontalSlider.setMaximum(60)
        self.IF_filter_shift_horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.IF_filter_BW_wide_pushButton = QPushButton(self.IF_filter_groupBox)
        self.IF_buttonGroup = QButtonGroup(MainWindow)
        self.IF_buttonGroup.setObjectName(u"IF_buttonGroup")
        self.IF_buttonGroup.addButton(self.IF_filter_BW_wide_pushButton)
        self.IF_filter_BW_wide_pushButton.setObjectName(u"IF_filter_BW_wide_pushButton")
        self.IF_filter_BW_wide_pushButton.setGeometry(QRect(40, 155, 91, 31))
        self.IF_filter_BW_wide_pushButton.setFont(font1)
        self.IF_filter_BW_wide_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.IF_filter_BW_wide_pushButton.setCheckable(True)
        self.IF_filter_shift_lcdNumber = QLCDNumber(self.IF_filter_groupBox)
        self.IF_filter_shift_lcdNumber.setObjectName(u"IF_filter_shift_lcdNumber")
        self.IF_filter_shift_lcdNumber.setGeometry(QRect(290, 35, 81, 41))
        self.IF_filter_shift_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.IF_filter_shift_lcdNumber.setDigitCount(5)
        self.IF_filter_label_3 = QLabel(self.IF_filter_groupBox)
        self.IF_filter_label_3.setObjectName(u"IF_filter_label_3")
        self.IF_filter_label_3.setGeometry(QRect(380, 60, 21, 18))
        self.IF_filter_label_3.setFont(font)
        self.IF_filter_BW_horizontalSlider = QSlider(self.IF_filter_groupBox)
        self.IF_filter_BW_horizontalSlider.setObjectName(u"IF_filter_BW_horizontalSlider")
        self.IF_filter_BW_horizontalSlider.setGeometry(QRect(70, 95, 201, 31))
        self.IF_filter_BW_horizontalSlider.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.IF_filter_BW_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}\n"
"QSlider:disabled{color: darkgrey;}\n"
"QSlider:handle:disabled{background-color: darkgrey;  color: darkgrey;}")
        self.IF_filter_BW_horizontalSlider.setMinimum(0)
        self.IF_filter_BW_horizontalSlider.setMaximum(21)
        self.IF_filter_BW_horizontalSlider.setPageStep(1)
        self.IF_filter_BW_horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.IF_filter_label_1 = QLabel(self.IF_filter_groupBox)
        self.IF_filter_label_1.setObjectName(u"IF_filter_label_1")
        self.IF_filter_label_1.setGeometry(QRect(10, 40, 41, 31))
        self.IF_filter_label_1.setFont(font9)
        self.IF_filter_label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.IF_filter_label_2 = QLabel(self.IF_filter_groupBox)
        self.IF_filter_label_2.setObjectName(u"IF_filter_label_2")
        self.IF_filter_label_2.setGeometry(QRect(20, 95, 31, 31))
        self.IF_filter_label_2.setFont(font9)
        self.IF_filter_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.IF_filter_label_4 = QLabel(self.IF_filter_groupBox)
        self.IF_filter_label_4.setObjectName(u"IF_filter_label_4")
        self.IF_filter_label_4.setGeometry(QRect(380, 115, 21, 18))
        self.IF_filter_label_4.setFont(font)
        self.IF_filter_BW_lcdNumber = QLCDNumber(self.IF_filter_groupBox)
        self.IF_filter_BW_lcdNumber.setObjectName(u"IF_filter_BW_lcdNumber")
        self.IF_filter_BW_lcdNumber.setGeometry(QRect(290, 90, 81, 41))
        self.IF_filter_BW_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.IF_filter_BW_lcdNumber.setDigitCount(5)
        self.IF_filter_BW_narrow_pushButton = QPushButton(self.IF_filter_groupBox)
        self.IF_buttonGroup.addButton(self.IF_filter_BW_narrow_pushButton)
        self.IF_filter_BW_narrow_pushButton.setObjectName(u"IF_filter_BW_narrow_pushButton")
        self.IF_filter_BW_narrow_pushButton.setGeometry(QRect(150, 155, 91, 31))
        self.IF_filter_BW_narrow_pushButton.setFont(font1)
        self.IF_filter_BW_narrow_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.IF_filter_BW_narrow_pushButton.setCheckable(True)
        self.IF_filter_line = QFrame(self.IF_filter_groupBox)
        self.IF_filter_line.setObjectName(u"IF_filter_line")
        self.IF_filter_line.setGeometry(QRect(290, 140, 80, 3))
        self.IF_filter_line.setStyleSheet(u"QFrame{ border: none; background-color: lightblue;}")
        self.IF_filter_line.setFrameShape(QFrame.Shape.HLine)
        self.IF_filter_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.FrontEnd_groupBox = QGroupBox(self.tab_2)
        self.FrontEnd_groupBox.setObjectName(u"FrontEnd_groupBox")
        self.FrontEnd_groupBox.setGeometry(QRect(20, 560, 181, 141))
        self.FrontEnd_groupBox.setFont(font1)
        self.FrontEnd_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.FrontEnd_label_1 = QLabel(self.FrontEnd_groupBox)
        self.FrontEnd_label_1.setObjectName(u"FrontEnd_label_1")
        self.FrontEnd_label_1.setGeometry(QRect(10, 35, 51, 31))
        self.FrontEnd_label_1.setFont(font9)
        self.FrontEnd_label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.FrontEnd_label_2 = QLabel(self.FrontEnd_groupBox)
        self.FrontEnd_label_2.setObjectName(u"FrontEnd_label_2")
        self.FrontEnd_label_2.setGeometry(QRect(20, 90, 41, 31))
        self.FrontEnd_label_2.setFont(font9)
        self.FrontEnd_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.FrontEnd_ATT_pushButton = QPushButton(self.FrontEnd_groupBox)
        self.FrontEnd_ATT_pushButton.setObjectName(u"FrontEnd_ATT_pushButton")
        self.FrontEnd_ATT_pushButton.setGeometry(QRect(70, 35, 91, 31))
        self.FrontEnd_ATT_pushButton.setFont(font1)
        self.FrontEnd_ATT_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.FrontEnd_ATT_pushButton.setCheckable(True)
        self.FrontEnd_IPO_comboBox = QComboBox(self.FrontEnd_groupBox)
        self.FrontEnd_IPO_comboBox.addItem("")
        self.FrontEnd_IPO_comboBox.addItem("")
        self.FrontEnd_IPO_comboBox.addItem("")
        self.FrontEnd_IPO_comboBox.setObjectName(u"FrontEnd_IPO_comboBox")
        self.FrontEnd_IPO_comboBox.setGeometry(QRect(70, 90, 91, 31))
        self.Noise_groupBox = QGroupBox(self.tab_2)
        self.Noise_groupBox.setObjectName(u"Noise_groupBox")
        self.Noise_groupBox.setGeometry(QRect(220, 560, 511, 141))
        self.Noise_groupBox.setFont(font1)
        self.Noise_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Noise_label_1 = QLabel(self.Noise_groupBox)
        self.Noise_label_1.setObjectName(u"Noise_label_1")
        self.Noise_label_1.setGeometry(QRect(10, 50, 41, 31))
        self.Noise_label_1.setFont(font9)
        self.Noise_label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Noise_DNF_pushButton = QPushButton(self.Noise_groupBox)
        self.Noise_DNF_pushButton.setObjectName(u"Noise_DNF_pushButton")
        self.Noise_DNF_pushButton.setGeometry(QRect(60, 50, 91, 31))
        self.Noise_DNF_pushButton.setFont(font1)
        self.Noise_DNF_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.Noise_DNF_pushButton.setCheckable(True)
        self.Noise_frame_1 = QFrame(self.Noise_groupBox)
        self.Noise_frame_1.setObjectName(u"Noise_frame_1")
        self.Noise_frame_1.setGeometry(QRect(340, 40, 151, 91))
        self.Noise_frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Noise_frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.Noise_NB_pushButton = QPushButton(self.Noise_frame_1)
        self.Noise_NB_pushButton.setObjectName(u"Noise_NB_pushButton")
        self.Noise_NB_pushButton.setGeometry(QRect(50, 10, 91, 31))
        self.Noise_NB_pushButton.setFont(font1)
        self.Noise_NB_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.Noise_NB_pushButton.setCheckable(True)
        self.Noise_NB_comboBox = QComboBox(self.Noise_frame_1)
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.addItem("")
        self.Noise_NB_comboBox.setObjectName(u"Noise_NB_comboBox")
        self.Noise_NB_comboBox.setGeometry(QRect(50, 50, 91, 31))
        self.Noise_NB_comboBox.setStyleSheet(u"QComboBox{combobox-popup: 0;}")
        self.Noise_label_3 = QLabel(self.Noise_frame_1)
        self.Noise_label_3.setObjectName(u"Noise_label_3")
        self.Noise_label_3.setGeometry(QRect(10, 10, 31, 31))
        self.Noise_label_3.setFont(font9)
        self.Noise_label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Noise_frame_2 = QFrame(self.Noise_groupBox)
        self.Noise_frame_2.setObjectName(u"Noise_frame_2")
        self.Noise_frame_2.setGeometry(QRect(170, 40, 161, 91))
        self.Noise_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Noise_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.Noise_DNR_comboBox = QComboBox(self.Noise_frame_2)
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.addItem("")
        self.Noise_DNR_comboBox.setObjectName(u"Noise_DNR_comboBox")
        self.Noise_DNR_comboBox.setGeometry(QRect(60, 50, 91, 31))
        self.Noise_DNR_comboBox.setStyleSheet(u"QComboBox{combobox-popup: 0;}")
        self.Noise_DNR_pushButton = QPushButton(self.Noise_frame_2)
        self.Noise_DNR_pushButton.setObjectName(u"Noise_DNR_pushButton")
        self.Noise_DNR_pushButton.setGeometry(QRect(60, 10, 91, 31))
        self.Noise_DNR_pushButton.setFont(font1)
        self.Noise_DNR_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.Noise_DNR_pushButton.setCheckable(True)
        self.Noise_label_2 = QLabel(self.Noise_frame_2)
        self.Noise_label_2.setObjectName(u"Noise_label_2")
        self.Noise_label_2.setGeometry(QRect(10, 10, 41, 31))
        self.Noise_label_2.setFont(font9)
        self.Noise_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Noise_frame_2.raise_()
        self.Noise_frame_1.raise_()
        self.Noise_label_1.raise_()
        self.Noise_DNF_pushButton.raise_()
        self.IF_spectrum_groupBox = QGroupBox(self.tab_2)
        self.IF_spectrum_groupBox.setObjectName(u"IF_spectrum_groupBox")
        self.IF_spectrum_groupBox.setGeometry(QRect(20, 20, 711, 521))
        self.IF_spectrum_groupBox.setFont(font1)
        self.IF_spectrum_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.IF_spectrum_frame = QFrame(self.IF_spectrum_groupBox)
        self.IF_spectrum_frame.setObjectName(u"IF_spectrum_frame")
        self.IF_spectrum_frame.setGeometry(QRect(20, 40, 671, 411))
        self.IF_spectrum_frame.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 10px;}")
        self.IF_spectrum_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.IF_spectrum_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.FFT_frame = QFrame(self.IF_spectrum_groupBox)
        self.FFT_frame.setObjectName(u"FFT_frame")
        self.FFT_frame.setGeometry(QRect(20, 460, 671, 51))
        self.FFT_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FFT_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.FFT_pushButton_3 = QPushButton(self.FFT_frame)
        self.FFT_buttonGroup = QButtonGroup(MainWindow)
        self.FFT_buttonGroup.setObjectName(u"FFT_buttonGroup")
        self.FFT_buttonGroup.addButton(self.FFT_pushButton_3)
        self.FFT_pushButton_3.setObjectName(u"FFT_pushButton_3")
        self.FFT_pushButton_3.setGeometry(QRect(160, 10, 51, 31))
        self.FFT_pushButton_3.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.FFT_pushButton_3.setCheckable(True)
        self.FFT_pushButton_1 = QPushButton(self.FFT_frame)
        self.FFT_buttonGroup.addButton(self.FFT_pushButton_1)
        self.FFT_pushButton_1.setObjectName(u"FFT_pushButton_1")
        self.FFT_pushButton_1.setGeometry(QRect(60, 10, 51, 31))
        self.FFT_pushButton_1.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.FFT_pushButton_1.setCheckable(True)
        self.FFT_pushButton_1.setChecked(True)
        self.FFT_label_2 = QLabel(self.FFT_frame)
        self.FFT_label_2.setObjectName(u"FFT_label_2")
        self.FFT_label_2.setGeometry(QRect(10, 10, 41, 31))
        self.FFT_label_2.setFont(font9)
        self.FFT_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.FFT_window_comboBox = QComboBox(self.FFT_frame)
        self.FFT_window_comboBox.addItem("")
        self.FFT_window_comboBox.addItem("")
        self.FFT_window_comboBox.addItem("")
        self.FFT_window_comboBox.addItem("")
        self.FFT_window_comboBox.addItem("")
        self.FFT_window_comboBox.setObjectName(u"FFT_window_comboBox")
        self.FFT_window_comboBox.setGeometry(QRect(570, 10, 91, 31))
        self.FFT_pushButton_2 = QPushButton(self.FFT_frame)
        self.FFT_buttonGroup.addButton(self.FFT_pushButton_2)
        self.FFT_pushButton_2.setObjectName(u"FFT_pushButton_2")
        self.FFT_pushButton_2.setGeometry(QRect(110, 10, 51, 31))
        self.FFT_pushButton_2.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.FFT_pushButton_2.setCheckable(True)
        self.FFT_label_1 = QLabel(self.FFT_frame)
        self.FFT_label_1.setObjectName(u"FFT_label_1")
        self.FFT_label_1.setGeometry(QRect(490, 10, 71, 31))
        self.FFT_label_1.setFont(font9)
        self.FFT_label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.FFT_label_3 = QLabel(self.FFT_frame)
        self.FFT_label_3.setObjectName(u"FFT_label_3")
        self.FFT_label_3.setGeometry(QRect(230, 10, 41, 31))
        self.FFT_label_3.setFont(font9)
        self.FFT_label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.FFT_gain_comboBox = QComboBox(self.FFT_frame)
        self.FFT_gain_comboBox.addItem("")
        self.FFT_gain_comboBox.addItem("")
        self.FFT_gain_comboBox.addItem("")
        self.FFT_gain_comboBox.addItem("")
        self.FFT_gain_comboBox.addItem("")
        self.FFT_gain_comboBox.setObjectName(u"FFT_gain_comboBox")
        self.FFT_gain_comboBox.setGeometry(QRect(280, 10, 71, 31))
        self.FFT_label_4 = QLabel(self.FFT_frame)
        self.FFT_label_4.setObjectName(u"FFT_label_4")
        self.FFT_label_4.setGeometry(QRect(380, 10, 31, 31))
        self.FFT_label_4.setFont(font9)
        self.FFT_label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.FFT_block_comboBox = QComboBox(self.FFT_frame)
        self.FFT_block_comboBox.addItem("")
        self.FFT_block_comboBox.addItem("")
        self.FFT_block_comboBox.addItem("")
        self.FFT_block_comboBox.setObjectName(u"FFT_block_comboBox")
        self.FFT_block_comboBox.setGeometry(QRect(420, 10, 61, 31))
        self.Radio_tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"QWidget{ background-color: gray}")
        self.EQ_groupBox = QGroupBox(self.tab_3)
        self.EQ_groupBox.setObjectName(u"EQ_groupBox")
        self.EQ_groupBox.setGeometry(QRect(20, 20, 721, 491))
        self.EQ_groupBox.setFont(font1)
        self.EQ_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.EQ_1_center_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_1_center_verticalSlider.setObjectName(u"EQ_1_center_verticalSlider")
        self.EQ_1_center_verticalSlider.setGeometry(QRect(60, 310, 31, 101))
        self.EQ_1_center_verticalSlider.setAutoFillBackground(False)
        self.EQ_1_center_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_1_center_verticalSlider.setMinimum(0)
        self.EQ_1_center_verticalSlider.setMaximum(7)
        self.EQ_1_center_verticalSlider.setPageStep(1)
        self.EQ_1_center_verticalSlider.setValue(0)
        self.EQ_1_center_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_1_center_verticalSlider.setInvertedAppearance(False)
        self.EQ_1_center_verticalSlider.setInvertedControls(False)
        self.EQ_1_center_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_1_center_verticalSlider.setTickInterval(5)
        self.EQ_1_label_1 = QLabel(self.EQ_groupBox)
        self.EQ_1_label_1.setObjectName(u"EQ_1_label_1")
        self.EQ_1_label_1.setGeometry(QRect(45, 420, 61, 21))
        self.EQ_1_label_1.setFont(font9)
        self.EQ_1_label_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_1_label_1.setWordWrap(True)
        self.EQ_1_label_2 = QLabel(self.EQ_groupBox)
        self.EQ_1_label_2.setObjectName(u"EQ_1_label_2")
        self.EQ_1_label_2.setGeometry(QRect(100, 420, 51, 21))
        self.EQ_1_label_2.setFont(font9)
        self.EQ_1_label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_1_label_2.setWordWrap(True)
        self.EQ_1_gain_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_1_gain_verticalSlider.setObjectName(u"EQ_1_gain_verticalSlider")
        self.EQ_1_gain_verticalSlider.setGeometry(QRect(110, 310, 31, 101))
        self.EQ_1_gain_verticalSlider.setAutoFillBackground(False)
        self.EQ_1_gain_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_1_gain_verticalSlider.setMinimum(-20)
        self.EQ_1_gain_verticalSlider.setMaximum(10)
        self.EQ_1_gain_verticalSlider.setPageStep(1)
        self.EQ_1_gain_verticalSlider.setValue(5)
        self.EQ_1_gain_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_1_gain_verticalSlider.setInvertedAppearance(False)
        self.EQ_1_gain_verticalSlider.setInvertedControls(False)
        self.EQ_1_gain_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_1_gain_verticalSlider.setTickInterval(5)
        self.EQ_1_label_3 = QLabel(self.EQ_groupBox)
        self.EQ_1_label_3.setObjectName(u"EQ_1_label_3")
        self.EQ_1_label_3.setGeometry(QRect(155, 420, 41, 21))
        self.EQ_1_label_3.setFont(font9)
        self.EQ_1_label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_1_label_3.setWordWrap(True)
        self.EQ_1_BW_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_1_BW_verticalSlider.setObjectName(u"EQ_1_BW_verticalSlider")
        self.EQ_1_BW_verticalSlider.setGeometry(QRect(160, 310, 31, 101))
        self.EQ_1_BW_verticalSlider.setAutoFillBackground(False)
        self.EQ_1_BW_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_1_BW_verticalSlider.setMinimum(1)
        self.EQ_1_BW_verticalSlider.setMaximum(10)
        self.EQ_1_BW_verticalSlider.setPageStep(1)
        self.EQ_1_BW_verticalSlider.setValue(10)
        self.EQ_1_BW_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_1_BW_verticalSlider.setInvertedAppearance(False)
        self.EQ_1_BW_verticalSlider.setInvertedControls(False)
        self.EQ_1_BW_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_1_BW_verticalSlider.setTickInterval(5)
        self.EQ_filter_frame = QFrame(self.EQ_groupBox)
        self.EQ_filter_frame.setObjectName(u"EQ_filter_frame")
        self.EQ_filter_frame.setGeometry(QRect(20, 40, 561, 241))
        self.EQ_filter_frame.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 10px;}")
        self.EQ_filter_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.EQ_filter_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.EQ_2_center_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_2_center_verticalSlider.setObjectName(u"EQ_2_center_verticalSlider")
        self.EQ_2_center_verticalSlider.setGeometry(QRect(240, 310, 31, 101))
        self.EQ_2_center_verticalSlider.setAutoFillBackground(False)
        self.EQ_2_center_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_2_center_verticalSlider.setMinimum(0)
        self.EQ_2_center_verticalSlider.setMaximum(9)
        self.EQ_2_center_verticalSlider.setPageStep(1)
        self.EQ_2_center_verticalSlider.setValue(0)
        self.EQ_2_center_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_2_center_verticalSlider.setInvertedAppearance(False)
        self.EQ_2_center_verticalSlider.setInvertedControls(False)
        self.EQ_2_center_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_2_center_verticalSlider.setTickInterval(5)
        self.EQ_2_gain_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_2_gain_verticalSlider.setObjectName(u"EQ_2_gain_verticalSlider")
        self.EQ_2_gain_verticalSlider.setGeometry(QRect(290, 310, 31, 101))
        self.EQ_2_gain_verticalSlider.setAutoFillBackground(False)
        self.EQ_2_gain_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_2_gain_verticalSlider.setMinimum(-20)
        self.EQ_2_gain_verticalSlider.setMaximum(10)
        self.EQ_2_gain_verticalSlider.setPageStep(1)
        self.EQ_2_gain_verticalSlider.setValue(5)
        self.EQ_2_gain_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_2_gain_verticalSlider.setInvertedAppearance(False)
        self.EQ_2_gain_verticalSlider.setInvertedControls(False)
        self.EQ_2_gain_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_2_gain_verticalSlider.setTickInterval(5)
        self.EQ_2_label_3 = QLabel(self.EQ_groupBox)
        self.EQ_2_label_3.setObjectName(u"EQ_2_label_3")
        self.EQ_2_label_3.setGeometry(QRect(335, 420, 41, 21))
        self.EQ_2_label_3.setFont(font9)
        self.EQ_2_label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_2_label_3.setWordWrap(True)
        self.EQ_2_label_1 = QLabel(self.EQ_groupBox)
        self.EQ_2_label_1.setObjectName(u"EQ_2_label_1")
        self.EQ_2_label_1.setGeometry(QRect(225, 420, 61, 21))
        self.EQ_2_label_1.setFont(font9)
        self.EQ_2_label_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_2_label_1.setWordWrap(True)
        self.EQ_2_label_2 = QLabel(self.EQ_groupBox)
        self.EQ_2_label_2.setObjectName(u"EQ_2_label_2")
        self.EQ_2_label_2.setGeometry(QRect(280, 420, 51, 21))
        self.EQ_2_label_2.setFont(font9)
        self.EQ_2_label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_2_label_2.setWordWrap(True)
        self.EQ_2_BW_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_2_BW_verticalSlider.setObjectName(u"EQ_2_BW_verticalSlider")
        self.EQ_2_BW_verticalSlider.setGeometry(QRect(340, 310, 31, 101))
        self.EQ_2_BW_verticalSlider.setAutoFillBackground(False)
        self.EQ_2_BW_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_2_BW_verticalSlider.setMinimum(1)
        self.EQ_2_BW_verticalSlider.setMaximum(10)
        self.EQ_2_BW_verticalSlider.setPageStep(1)
        self.EQ_2_BW_verticalSlider.setValue(10)
        self.EQ_2_BW_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_2_BW_verticalSlider.setInvertedAppearance(False)
        self.EQ_2_BW_verticalSlider.setInvertedControls(False)
        self.EQ_2_BW_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_2_BW_verticalSlider.setTickInterval(5)
        self.EQ_3_BW_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_3_BW_verticalSlider.setObjectName(u"EQ_3_BW_verticalSlider")
        self.EQ_3_BW_verticalSlider.setGeometry(QRect(520, 310, 31, 101))
        self.EQ_3_BW_verticalSlider.setAutoFillBackground(False)
        self.EQ_3_BW_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_3_BW_verticalSlider.setMinimum(1)
        self.EQ_3_BW_verticalSlider.setMaximum(10)
        self.EQ_3_BW_verticalSlider.setPageStep(1)
        self.EQ_3_BW_verticalSlider.setValue(10)
        self.EQ_3_BW_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_3_BW_verticalSlider.setInvertedAppearance(False)
        self.EQ_3_BW_verticalSlider.setInvertedControls(False)
        self.EQ_3_BW_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_3_BW_verticalSlider.setTickInterval(5)
        self.EQ_3_label_2 = QLabel(self.EQ_groupBox)
        self.EQ_3_label_2.setObjectName(u"EQ_3_label_2")
        self.EQ_3_label_2.setGeometry(QRect(460, 420, 51, 21))
        self.EQ_3_label_2.setFont(font9)
        self.EQ_3_label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_3_label_2.setWordWrap(True)
        self.EQ_3_label_1 = QLabel(self.EQ_groupBox)
        self.EQ_3_label_1.setObjectName(u"EQ_3_label_1")
        self.EQ_3_label_1.setGeometry(QRect(405, 420, 61, 21))
        self.EQ_3_label_1.setFont(font9)
        self.EQ_3_label_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_3_label_1.setWordWrap(True)
        self.EQ_3_label_3 = QLabel(self.EQ_groupBox)
        self.EQ_3_label_3.setObjectName(u"EQ_3_label_3")
        self.EQ_3_label_3.setGeometry(QRect(515, 420, 41, 21))
        self.EQ_3_label_3.setFont(font9)
        self.EQ_3_label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_3_label_3.setWordWrap(True)
        self.EQ_3_center_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_3_center_verticalSlider.setObjectName(u"EQ_3_center_verticalSlider")
        self.EQ_3_center_verticalSlider.setGeometry(QRect(420, 310, 31, 101))
        self.EQ_3_center_verticalSlider.setAutoFillBackground(False)
        self.EQ_3_center_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_3_center_verticalSlider.setMinimum(0)
        self.EQ_3_center_verticalSlider.setMaximum(18)
        self.EQ_3_center_verticalSlider.setPageStep(1)
        self.EQ_3_center_verticalSlider.setValue(0)
        self.EQ_3_center_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_3_center_verticalSlider.setInvertedAppearance(False)
        self.EQ_3_center_verticalSlider.setInvertedControls(False)
        self.EQ_3_center_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_3_center_verticalSlider.setTickInterval(5)
        self.EQ_3_gain_verticalSlider = QSlider(self.EQ_groupBox)
        self.EQ_3_gain_verticalSlider.setObjectName(u"EQ_3_gain_verticalSlider")
        self.EQ_3_gain_verticalSlider.setGeometry(QRect(470, 310, 31, 101))
        self.EQ_3_gain_verticalSlider.setAutoFillBackground(False)
        self.EQ_3_gain_verticalSlider.setStyleSheet(u"QSlider::groove:vertical {background: lightgray; width: 10px; border-radius: 3px;}\n"
"QSlider::handle:vertical {background: lightblue; border: 1px solid black; height: 10px; width: 30px; margin-left: -10px; margin-right: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:vertical {background: white;}\n"
"QSlider::add-page:vertical {background: white;}")
        self.EQ_3_gain_verticalSlider.setMinimum(-20)
        self.EQ_3_gain_verticalSlider.setMaximum(10)
        self.EQ_3_gain_verticalSlider.setPageStep(1)
        self.EQ_3_gain_verticalSlider.setValue(5)
        self.EQ_3_gain_verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.EQ_3_gain_verticalSlider.setInvertedAppearance(False)
        self.EQ_3_gain_verticalSlider.setInvertedControls(False)
        self.EQ_3_gain_verticalSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.EQ_3_gain_verticalSlider.setTickInterval(5)
        self.EQ_1_label_4 = QLabel(self.EQ_groupBox)
        self.EQ_1_label_4.setObjectName(u"EQ_1_label_4")
        self.EQ_1_label_4.setGeometry(QRect(100, 450, 51, 21))
        self.EQ_1_label_4.setFont(font9)
        self.EQ_1_label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_1_label_4.setWordWrap(True)
        self.EQ_2_label_4 = QLabel(self.EQ_groupBox)
        self.EQ_2_label_4.setObjectName(u"EQ_2_label_4")
        self.EQ_2_label_4.setGeometry(QRect(280, 450, 51, 21))
        self.EQ_2_label_4.setFont(font9)
        self.EQ_2_label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_2_label_4.setWordWrap(True)
        self.EQ_3_label_4 = QLabel(self.EQ_groupBox)
        self.EQ_3_label_4.setObjectName(u"EQ_3_label_4")
        self.EQ_3_label_4.setGeometry(QRect(460, 450, 51, 21))
        self.EQ_3_label_4.setFont(font9)
        self.EQ_3_label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_3_label_4.setWordWrap(True)
        self.EQ_1_line_1 = QFrame(self.EQ_groupBox)
        self.EQ_1_line_1.setObjectName(u"EQ_1_line_1")
        self.EQ_1_line_1.setGeometry(QRect(70, 460, 31, 2))
        self.EQ_1_line_1.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.EQ_1_line_1.setFrameShape(QFrame.Shape.HLine)
        self.EQ_1_line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_1_line_3 = QFrame(self.EQ_groupBox)
        self.EQ_1_line_3.setObjectName(u"EQ_1_line_3")
        self.EQ_1_line_3.setGeometry(QRect(70, 445, 2, 17))
        self.EQ_1_line_3.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.EQ_1_line_3.setFrameShape(QFrame.Shape.VLine)
        self.EQ_1_line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_1_line_2 = QFrame(self.EQ_groupBox)
        self.EQ_1_line_2.setObjectName(u"EQ_1_line_2")
        self.EQ_1_line_2.setGeometry(QRect(150, 460, 31, 2))
        self.EQ_1_line_2.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.EQ_1_line_2.setFrameShape(QFrame.Shape.HLine)
        self.EQ_1_line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_1_line_4 = QFrame(self.EQ_groupBox)
        self.EQ_1_line_4.setObjectName(u"EQ_1_line_4")
        self.EQ_1_line_4.setGeometry(QRect(180, 445, 2, 17))
        self.EQ_1_line_4.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.EQ_1_line_4.setFrameShape(QFrame.Shape.VLine)
        self.EQ_1_line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_2_line_2 = QFrame(self.EQ_groupBox)
        self.EQ_2_line_2.setObjectName(u"EQ_2_line_2")
        self.EQ_2_line_2.setGeometry(QRect(330, 460, 31, 2))
        self.EQ_2_line_2.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.EQ_2_line_2.setFrameShape(QFrame.Shape.HLine)
        self.EQ_2_line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_2_line_3 = QFrame(self.EQ_groupBox)
        self.EQ_2_line_3.setObjectName(u"EQ_2_line_3")
        self.EQ_2_line_3.setGeometry(QRect(250, 445, 2, 17))
        self.EQ_2_line_3.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.EQ_2_line_3.setFrameShape(QFrame.Shape.VLine)
        self.EQ_2_line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_2_line_1 = QFrame(self.EQ_groupBox)
        self.EQ_2_line_1.setObjectName(u"EQ_2_line_1")
        self.EQ_2_line_1.setGeometry(QRect(250, 460, 31, 2))
        self.EQ_2_line_1.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.EQ_2_line_1.setFrameShape(QFrame.Shape.HLine)
        self.EQ_2_line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_2_line_4 = QFrame(self.EQ_groupBox)
        self.EQ_2_line_4.setObjectName(u"EQ_2_line_4")
        self.EQ_2_line_4.setGeometry(QRect(360, 445, 2, 17))
        self.EQ_2_line_4.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.EQ_2_line_4.setFrameShape(QFrame.Shape.VLine)
        self.EQ_2_line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_3_line_2 = QFrame(self.EQ_groupBox)
        self.EQ_3_line_2.setObjectName(u"EQ_3_line_2")
        self.EQ_3_line_2.setGeometry(QRect(510, 460, 31, 2))
        self.EQ_3_line_2.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.EQ_3_line_2.setFrameShape(QFrame.Shape.HLine)
        self.EQ_3_line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_3_line_3 = QFrame(self.EQ_groupBox)
        self.EQ_3_line_3.setObjectName(u"EQ_3_line_3")
        self.EQ_3_line_3.setGeometry(QRect(430, 445, 2, 17))
        self.EQ_3_line_3.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.EQ_3_line_3.setFrameShape(QFrame.Shape.VLine)
        self.EQ_3_line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_3_line_1 = QFrame(self.EQ_groupBox)
        self.EQ_3_line_1.setObjectName(u"EQ_3_line_1")
        self.EQ_3_line_1.setGeometry(QRect(430, 460, 31, 2))
        self.EQ_3_line_1.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.EQ_3_line_1.setFrameShape(QFrame.Shape.HLine)
        self.EQ_3_line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_3_line_4 = QFrame(self.EQ_groupBox)
        self.EQ_3_line_4.setObjectName(u"EQ_3_line_4")
        self.EQ_3_line_4.setGeometry(QRect(540, 445, 2, 17))
        self.EQ_3_line_4.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.EQ_3_line_4.setFrameShape(QFrame.Shape.VLine)
        self.EQ_3_line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.EQ_comboBox = QComboBox(self.EQ_groupBox)
        self.EQ_comboBox.addItem("")
        self.EQ_comboBox.addItem("")
        self.EQ_comboBox.addItem("")
        self.EQ_comboBox.addItem("")
        self.EQ_comboBox.addItem("")
        self.EQ_comboBox.addItem("")
        self.EQ_comboBox.setObjectName(u"EQ_comboBox")
        self.EQ_comboBox.setGeometry(QRect(590, 340, 111, 31))
        self.EQ_label_1 = QLabel(self.EQ_groupBox)
        self.EQ_label_1.setObjectName(u"EQ_label_1")
        self.EQ_label_1.setGeometry(QRect(590, 310, 71, 21))
        self.EQ_label_1.setFont(font9)
        self.EQ_label_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.EQ_label_1.setWordWrap(True)
        self.EQ_pushButton_1 = QPushButton(self.EQ_groupBox)
        self.EQ_pushButton_1.setObjectName(u"EQ_pushButton_1")
        self.EQ_pushButton_1.setGeometry(QRect(590, 395, 111, 31))
        self.EQ_pushButton_2 = QPushButton(self.EQ_groupBox)
        self.EQ_buttonGroup = QButtonGroup(MainWindow)
        self.EQ_buttonGroup.setObjectName(u"EQ_buttonGroup")
        self.EQ_buttonGroup.addButton(self.EQ_pushButton_2)
        self.EQ_pushButton_2.setObjectName(u"EQ_pushButton_2")
        self.EQ_pushButton_2.setGeometry(QRect(610, 50, 91, 31))
        self.EQ_pushButton_2.setFont(font1)
        self.EQ_pushButton_2.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.EQ_pushButton_2.setCheckable(True)
        self.EQ_pushButton_2.setChecked(True)
        self.EQ_pushButton_3 = QPushButton(self.EQ_groupBox)
        self.EQ_buttonGroup.addButton(self.EQ_pushButton_3)
        self.EQ_pushButton_3.setObjectName(u"EQ_pushButton_3")
        self.EQ_pushButton_3.setGeometry(QRect(610, 125, 91, 31))
        self.EQ_pushButton_3.setFont(font1)
        self.EQ_pushButton_3.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.EQ_pushButton_3.setCheckable(True)
        self.EQ_1_center_label = QLabel(self.EQ_groupBox)
        self.EQ_1_center_label.setObjectName(u"EQ_1_center_label")
        self.EQ_1_center_label.setGeometry(QRect(60, 285, 31, 21))
        font13 = QFont()
        font13.setFamilies([u"Monospace"])
        font13.setPointSize(12)
        font13.setBold(False)
        self.EQ_1_center_label.setFont(font13)
        self.EQ_1_center_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_1_center_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_1_center_label.setWordWrap(True)
        self.EQ_1_gain_label = QLabel(self.EQ_groupBox)
        self.EQ_1_gain_label.setObjectName(u"EQ_1_gain_label")
        self.EQ_1_gain_label.setGeometry(QRect(110, 285, 31, 21))
        self.EQ_1_gain_label.setFont(font13)
        self.EQ_1_gain_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_1_gain_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_1_gain_label.setWordWrap(True)
        self.EQ_1_BW_label = QLabel(self.EQ_groupBox)
        self.EQ_1_BW_label.setObjectName(u"EQ_1_BW_label")
        self.EQ_1_BW_label.setGeometry(QRect(160, 285, 31, 21))
        self.EQ_1_BW_label.setFont(font13)
        self.EQ_1_BW_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_1_BW_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_1_BW_label.setWordWrap(True)
        self.EQ_2_gain_label = QLabel(self.EQ_groupBox)
        self.EQ_2_gain_label.setObjectName(u"EQ_2_gain_label")
        self.EQ_2_gain_label.setGeometry(QRect(290, 285, 31, 21))
        self.EQ_2_gain_label.setFont(font13)
        self.EQ_2_gain_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_2_gain_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_2_gain_label.setWordWrap(True)
        self.EQ_2_center_label = QLabel(self.EQ_groupBox)
        self.EQ_2_center_label.setObjectName(u"EQ_2_center_label")
        self.EQ_2_center_label.setGeometry(QRect(240, 285, 31, 21))
        self.EQ_2_center_label.setFont(font13)
        self.EQ_2_center_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_2_center_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_2_center_label.setWordWrap(True)
        self.EQ_2_BW_label = QLabel(self.EQ_groupBox)
        self.EQ_2_BW_label.setObjectName(u"EQ_2_BW_label")
        self.EQ_2_BW_label.setGeometry(QRect(340, 285, 31, 21))
        self.EQ_2_BW_label.setFont(font13)
        self.EQ_2_BW_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_2_BW_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_2_BW_label.setWordWrap(True)
        self.EQ_3_BW_label = QLabel(self.EQ_groupBox)
        self.EQ_3_BW_label.setObjectName(u"EQ_3_BW_label")
        self.EQ_3_BW_label.setGeometry(QRect(520, 285, 31, 21))
        self.EQ_3_BW_label.setFont(font13)
        self.EQ_3_BW_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_3_BW_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_3_BW_label.setWordWrap(True)
        self.EQ_3_gain_label = QLabel(self.EQ_groupBox)
        self.EQ_3_gain_label.setObjectName(u"EQ_3_gain_label")
        self.EQ_3_gain_label.setGeometry(QRect(470, 285, 31, 21))
        self.EQ_3_gain_label.setFont(font13)
        self.EQ_3_gain_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_3_gain_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_3_gain_label.setWordWrap(True)
        self.EQ_3_center_label = QLabel(self.EQ_groupBox)
        self.EQ_3_center_label.setObjectName(u"EQ_3_center_label")
        self.EQ_3_center_label.setGeometry(QRect(420, 285, 31, 21))
        self.EQ_3_center_label.setFont(font13)
        self.EQ_3_center_label.setTextFormat(Qt.TextFormat.PlainText)
        self.EQ_3_center_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_3_center_label.setWordWrap(True)
        self.EQ_label_2 = QLabel(self.EQ_groupBox)
        self.EQ_label_2.setObjectName(u"EQ_label_2")
        self.EQ_label_2.setGeometry(QRect(600, 160, 111, 21))
        font14 = QFont()
        font14.setPointSize(11)
        font14.setBold(True)
        self.EQ_label_2.setFont(font14)
        self.EQ_label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_label_2.setWordWrap(True)
        self.EQ_label_3 = QLabel(self.EQ_groupBox)
        self.EQ_label_3.setObjectName(u"EQ_label_3")
        self.EQ_label_3.setGeometry(QRect(600, 85, 111, 21))
        self.EQ_label_3.setFont(font14)
        self.EQ_label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.EQ_label_3.setWordWrap(True)
        self.Speech_Proc_groupBox = QGroupBox(self.tab_3)
        self.Speech_Proc_groupBox.setObjectName(u"Speech_Proc_groupBox")
        self.Speech_Proc_groupBox.setGeometry(QRect(760, 20, 321, 231))
        self.Speech_Proc_groupBox.setFont(font1)
        self.Speech_Proc_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Speech_label_1 = QLabel(self.Speech_Proc_groupBox)
        self.Speech_label_1.setObjectName(u"Speech_label_1")
        self.Speech_label_1.setGeometry(QRect(30, 40, 141, 31))
        self.Speech_label_1.setFont(font9)
        self.Speech_label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Speech_label_1.setWordWrap(True)
        self.Speech_Proc_EQ_pushButton = QPushButton(self.Speech_Proc_groupBox)
        self.Speech_Proc_EQ_pushButton.setObjectName(u"Speech_Proc_EQ_pushButton")
        self.Speech_Proc_EQ_pushButton.setGeometry(QRect(190, 40, 91, 31))
        self.Speech_Proc_EQ_pushButton.setFont(font1)
        self.Speech_Proc_EQ_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.Speech_Proc_EQ_pushButton.setCheckable(True)
        self.Speech_Proc_frame = QFrame(self.Speech_Proc_groupBox)
        self.Speech_Proc_frame.setObjectName(u"Speech_Proc_frame")
        self.Speech_Proc_frame.setGeometry(QRect(20, 90, 281, 121))
        self.Speech_Proc_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Speech_Proc_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Speech_Proc_lcdNumber = QLCDNumber(self.Speech_Proc_frame)
        self.Speech_Proc_lcdNumber.setObjectName(u"Speech_Proc_lcdNumber")
        self.Speech_Proc_lcdNumber.setGeometry(QRect(210, 60, 51, 41))
        self.Speech_Proc_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.Speech_Proc_lcdNumber.setDigitCount(2)
        self.Speech_Proc_pushButton = QPushButton(self.Speech_Proc_frame)
        self.Speech_Proc_pushButton.setObjectName(u"Speech_Proc_pushButton")
        self.Speech_Proc_pushButton.setGeometry(QRect(170, 10, 91, 31))
        self.Speech_Proc_pushButton.setFont(font1)
        self.Speech_Proc_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.Speech_Proc_pushButton.setCheckable(True)
        self.Speech_Proc_horizontalSlider = QSlider(self.Speech_Proc_frame)
        self.Speech_Proc_horizontalSlider.setObjectName(u"Speech_Proc_horizontalSlider")
        self.Speech_Proc_horizontalSlider.setGeometry(QRect(20, 65, 171, 31))
        self.Speech_Proc_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}\n"
"QSlider:disabled{color: darkgrey;}\n"
"QSlider:handle:disabled{background-color: darkgrey;  color: darkgrey;}")
        self.Speech_Proc_horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.Speech_label_2 = QLabel(self.Speech_Proc_frame)
        self.Speech_label_2.setObjectName(u"Speech_label_2")
        self.Speech_label_2.setGeometry(QRect(10, 10, 141, 31))
        self.Speech_label_2.setFont(font9)
        self.Speech_label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Speech_label_2.setWordWrap(True)
        self.Speech_Proc_frame.raise_()
        self.Speech_label_1.raise_()
        self.Speech_Proc_EQ_pushButton.raise_()
        self.Tx_Audio_groupBox = QGroupBox(self.tab_3)
        self.Tx_Audio_groupBox.setObjectName(u"Tx_Audio_groupBox")
        self.Tx_Audio_groupBox.setGeometry(QRect(20, 530, 721, 171))
        self.Tx_Audio_groupBox.setFont(font1)
        self.Tx_Audio_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Tx_Audio_BW_comboBox = QComboBox(self.Tx_Audio_groupBox)
        self.Tx_Audio_BW_comboBox.addItem("")
        self.Tx_Audio_BW_comboBox.addItem("")
        self.Tx_Audio_BW_comboBox.addItem("")
        self.Tx_Audio_BW_comboBox.addItem("")
        self.Tx_Audio_BW_comboBox.addItem("")
        self.Tx_Audio_BW_comboBox.setObjectName(u"Tx_Audio_BW_comboBox")
        self.Tx_Audio_BW_comboBox.setGeometry(QRect(20, 105, 111, 31))
        self.Tx_Audio_label_1 = QLabel(self.Tx_Audio_groupBox)
        self.Tx_Audio_label_1.setObjectName(u"Tx_Audio_label_1")
        self.Tx_Audio_label_1.setGeometry(QRect(20, 50, 121, 31))
        self.Tx_Audio_label_1.setFont(font9)
        self.Tx_Audio_label_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Tx_Audio_label_1.setWordWrap(True)
        self.Tx_Audio_frame_1 = QFrame(self.Tx_Audio_groupBox)
        self.Tx_Audio_frame_1.setObjectName(u"Tx_Audio_frame_1")
        self.Tx_Audio_frame_1.setGeometry(QRect(160, 40, 251, 111))
        self.Tx_Audio_frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Tx_Audio_frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.Tx_Audio_label_2 = QLabel(self.Tx_Audio_frame_1)
        self.Tx_Audio_label_2.setObjectName(u"Tx_Audio_label_2")
        self.Tx_Audio_label_2.setGeometry(QRect(20, 10, 141, 31))
        self.Tx_Audio_label_2.setFont(font9)
        self.Tx_Audio_label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Tx_Audio_label_2.setWordWrap(True)
        self.Microphone_Gain_lcdNumber = QLCDNumber(self.Tx_Audio_frame_1)
        self.Microphone_Gain_lcdNumber.setObjectName(u"Microphone_Gain_lcdNumber")
        self.Microphone_Gain_lcdNumber.setGeometry(QRect(190, 60, 51, 41))
        self.Microphone_Gain_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.Microphone_Gain_lcdNumber.setDigitCount(2)
        self.Microphone_Gain_horizontalSlider = QSlider(self.Tx_Audio_frame_1)
        self.Microphone_Gain_horizontalSlider.setObjectName(u"Microphone_Gain_horizontalSlider")
        self.Microphone_Gain_horizontalSlider.setGeometry(QRect(20, 65, 151, 31))
        self.Microphone_Gain_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}\n"
"QSlider:disabled{color: darkgrey;}\n"
"QSlider:handle:disabled{background-color: darkgrey;  color: darkgrey;}")
        self.Microphone_Gain_horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.Tx_Audio_frame_2 = QFrame(self.Tx_Audio_groupBox)
        self.Tx_Audio_frame_2.setObjectName(u"Tx_Audio_frame_2")
        self.Tx_Audio_frame_2.setGeometry(QRect(440, 40, 251, 111))
        self.Tx_Audio_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Tx_Audio_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.Tx_Audio_label_3 = QLabel(self.Tx_Audio_frame_2)
        self.Tx_Audio_label_3.setObjectName(u"Tx_Audio_label_3")
        self.Tx_Audio_label_3.setGeometry(QRect(20, 10, 121, 31))
        self.Tx_Audio_label_3.setFont(font9)
        self.Tx_Audio_label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Tx_Audio_label_3.setWordWrap(True)
        self.Monitor_level_lcdNumber = QLCDNumber(self.Tx_Audio_frame_2)
        self.Monitor_level_lcdNumber.setObjectName(u"Monitor_level_lcdNumber")
        self.Monitor_level_lcdNumber.setGeometry(QRect(190, 60, 51, 41))
        self.Monitor_level_lcdNumber.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 4px;}\n"
"QLCDNumber {color: yellow;}")
        self.Monitor_level_lcdNumber.setDigitCount(2)
        self.Monitor_level_horizontalSlider = QSlider(self.Tx_Audio_frame_2)
        self.Monitor_level_horizontalSlider.setObjectName(u"Monitor_level_horizontalSlider")
        self.Monitor_level_horizontalSlider.setGeometry(QRect(20, 65, 151, 31))
        self.Monitor_level_horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}\n"
"QSlider:disabled{color: darkgrey;}\n"
"QSlider:handle:disabled{background-color: darkgrey;  color: darkgrey;}")
        self.Monitor_level_horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.Monitor_state_pushButton = QPushButton(self.Tx_Audio_frame_2)
        self.Monitor_state_pushButton.setObjectName(u"Monitor_state_pushButton")
        self.Monitor_state_pushButton.setGeometry(QRect(150, 10, 91, 31))
        self.Monitor_state_pushButton.setFont(font1)
        self.Monitor_state_pushButton.setStyleSheet(u"QPushButton{ background-color: lightblue; color: grey}\n"
"QPushButton::checked{ background-color: red; color: black}")
        self.Monitor_state_pushButton.setCheckable(True)
        self.Radio_tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setStyleSheet(u"QWidget{ background-color: gray}")
        self.Audio_filter_groupBox = QGroupBox(self.tab_4)
        self.Audio_filter_groupBox.setObjectName(u"Audio_filter_groupBox")
        self.Audio_filter_groupBox.setGeometry(QRect(20, 20, 721, 461))
        self.Audio_filter_groupBox.setFont(font1)
        self.Audio_filter_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.Audio_filter_frame = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_frame.setObjectName(u"Audio_filter_frame")
        self.Audio_filter_frame.setGeometry(QRect(20, 40, 561, 241))
        self.Audio_filter_frame.setStyleSheet(u"QWidget{ border: 2px black; background-color: black;border-radius: 10px;}")
        self.Audio_filter_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Audio_filter_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Audio_filter_pushButton_1 = QPushButton(self.Audio_filter_groupBox)
        self.Audio_buttonGroup = QButtonGroup(MainWindow)
        self.Audio_buttonGroup.setObjectName(u"Audio_buttonGroup")
        self.Audio_buttonGroup.addButton(self.Audio_filter_pushButton_1)
        self.Audio_filter_pushButton_1.setObjectName(u"Audio_filter_pushButton_1")
        self.Audio_filter_pushButton_1.setGeometry(QRect(610, 50, 91, 31))
        self.Audio_filter_pushButton_1.setFont(font1)
        self.Audio_filter_pushButton_1.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.Audio_filter_pushButton_1.setCheckable(True)
        self.Audio_filter_pushButton_1.setChecked(True)
        self.Audio_filter_pushButton_1.setProperty(u"bank", 1)
        self.Audio_filter_pushButton_2 = QPushButton(self.Audio_filter_groupBox)
        self.Audio_buttonGroup.addButton(self.Audio_filter_pushButton_2)
        self.Audio_filter_pushButton_2.setObjectName(u"Audio_filter_pushButton_2")
        self.Audio_filter_pushButton_2.setGeometry(QRect(610, 100, 91, 31))
        self.Audio_filter_pushButton_2.setFont(font1)
        self.Audio_filter_pushButton_2.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.Audio_filter_pushButton_2.setCheckable(True)
        self.Audio_filter_pushButton_2.setChecked(False)
        self.Audio_filter_pushButton_2.setProperty(u"bank", 2)
        self.Audio_filter_pushButton_3 = QPushButton(self.Audio_filter_groupBox)
        self.Audio_buttonGroup.addButton(self.Audio_filter_pushButton_3)
        self.Audio_filter_pushButton_3.setObjectName(u"Audio_filter_pushButton_3")
        self.Audio_filter_pushButton_3.setGeometry(QRect(610, 150, 91, 31))
        self.Audio_filter_pushButton_3.setFont(font1)
        self.Audio_filter_pushButton_3.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.Audio_filter_pushButton_3.setCheckable(True)
        self.Audio_filter_pushButton_3.setChecked(False)
        self.Audio_filter_pushButton_3.setProperty(u"bank", 3)
        self.Audio_filter_pushButton_4 = QPushButton(self.Audio_filter_groupBox)
        self.Audio_buttonGroup.addButton(self.Audio_filter_pushButton_4)
        self.Audio_filter_pushButton_4.setObjectName(u"Audio_filter_pushButton_4")
        self.Audio_filter_pushButton_4.setGeometry(QRect(610, 200, 91, 31))
        self.Audio_filter_pushButton_4.setFont(font1)
        self.Audio_filter_pushButton_4.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.Audio_filter_pushButton_4.setCheckable(True)
        self.Audio_filter_pushButton_4.setChecked(False)
        self.Audio_filter_pushButton_4.setProperty(u"bank", 4)
        self.Audio_filter_pushButton_5 = QPushButton(self.Audio_filter_groupBox)
        self.Audio_buttonGroup.addButton(self.Audio_filter_pushButton_5)
        self.Audio_filter_pushButton_5.setObjectName(u"Audio_filter_pushButton_5")
        self.Audio_filter_pushButton_5.setGeometry(QRect(610, 250, 91, 31))
        self.Audio_filter_pushButton_5.setFont(font1)
        self.Audio_filter_pushButton_5.setStyleSheet(u"QPushButton {background-color: lightblue;}\n"
"QPushButton::checked {background-color: red;}")
        self.Audio_filter_pushButton_5.setCheckable(True)
        self.Audio_filter_pushButton_5.setChecked(False)
        self.Audio_filter_pushButton_5.setProperty(u"bank", 5)
        self.Audio_filter_label_12 = QLabel(self.Audio_filter_groupBox)
        self.Audio_filter_label_12.setObjectName(u"Audio_filter_label_12")
        self.Audio_filter_label_12.setGeometry(QRect(30, 315, 41, 21))
        self.Audio_filter_label_12.setFont(font9)
        self.Audio_filter_label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.Audio_filter_label_12.setWordWrap(True)
        self.Audio_filter_horizontalSlider_1 = QSlider(self.Audio_filter_groupBox)
        self.Audio_filter_horizontalSlider_1.setObjectName(u"Audio_filter_horizontalSlider_1")
        self.Audio_filter_horizontalSlider_1.setGeometry(QRect(80, 300, 161, 51))
        self.Audio_filter_horizontalSlider_1.setAutoFillBackground(False)
        self.Audio_filter_horizontalSlider_1.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}")
        self.Audio_filter_horizontalSlider_1.setMinimum(0)
        self.Audio_filter_horizontalSlider_1.setMaximum(19)
        self.Audio_filter_horizontalSlider_1.setPageStep(1)
        self.Audio_filter_horizontalSlider_1.setValue(0)
        self.Audio_filter_horizontalSlider_1.setOrientation(Qt.Orientation.Horizontal)
        self.Audio_filter_horizontalSlider_1.setInvertedAppearance(False)
        self.Audio_filter_horizontalSlider_1.setInvertedControls(False)
        self.Audio_filter_horizontalSlider_1.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.Audio_filter_horizontalSlider_1.setTickInterval(5)
        self.Audio_filter_horizontalSlider_1.setProperty(u"side", 1)
        self.Audio_filter_label_13 = QLabel(self.Audio_filter_groupBox)
        self.Audio_filter_label_13.setObjectName(u"Audio_filter_label_13")
        self.Audio_filter_label_13.setGeometry(QRect(20, 370, 51, 21))
        self.Audio_filter_label_13.setFont(font9)
        self.Audio_filter_label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.Audio_filter_label_13.setWordWrap(True)
        self.Audio_filter_line_13 = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_line_13.setObjectName(u"Audio_filter_line_13")
        self.Audio_filter_line_13.setGeometry(QRect(65, 420, 2, 17))
        self.Audio_filter_line_13.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.Audio_filter_line_13.setFrameShape(QFrame.Shape.VLine)
        self.Audio_filter_line_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.Audio_filter_line_12 = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_line_12.setObjectName(u"Audio_filter_line_12")
        self.Audio_filter_line_12.setGeometry(QRect(185, 435, 61, 2))
        self.Audio_filter_line_12.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.Audio_filter_line_12.setFrameShape(QFrame.Shape.HLine)
        self.Audio_filter_line_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.Audio_filter_line_11 = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_line_11.setObjectName(u"Audio_filter_line_11")
        self.Audio_filter_line_11.setGeometry(QRect(65, 435, 61, 2))
        self.Audio_filter_line_11.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.Audio_filter_line_11.setFrameShape(QFrame.Shape.HLine)
        self.Audio_filter_line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.Audio_filter_line_14 = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_line_14.setObjectName(u"Audio_filter_line_14")
        self.Audio_filter_line_14.setGeometry(QRect(245, 420, 2, 17))
        self.Audio_filter_line_14.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.Audio_filter_line_14.setFrameShape(QFrame.Shape.VLine)
        self.Audio_filter_line_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.Audio_filter_label_11 = QLabel(self.Audio_filter_groupBox)
        self.Audio_filter_label_11.setObjectName(u"Audio_filter_label_11")
        self.Audio_filter_label_11.setGeometry(QRect(110, 425, 91, 21))
        self.Audio_filter_label_11.setFont(font9)
        self.Audio_filter_label_11.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.Audio_filter_label_11.setWordWrap(True)
        self.Audio_filter_comboBox_1 = QComboBox(self.Audio_filter_groupBox)
        self.Audio_filter_comboBox_1.addItem("")
        self.Audio_filter_comboBox_1.addItem("")
        self.Audio_filter_comboBox_1.setObjectName(u"Audio_filter_comboBox_1")
        self.Audio_filter_comboBox_1.setGeometry(QRect(80, 365, 91, 31))
        self.Audio_filter_comboBox_1.setProperty(u"side", 1)
        self.Audio_filter_line_21 = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_line_21.setObjectName(u"Audio_filter_line_21")
        self.Audio_filter_line_21.setGeometry(QRect(365, 435, 61, 2))
        self.Audio_filter_line_21.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.Audio_filter_line_21.setFrameShape(QFrame.Shape.HLine)
        self.Audio_filter_line_21.setFrameShadow(QFrame.Shadow.Sunken)
        self.Audio_filter_line_23 = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_line_23.setObjectName(u"Audio_filter_line_23")
        self.Audio_filter_line_23.setGeometry(QRect(365, 420, 2, 17))
        self.Audio_filter_line_23.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.Audio_filter_line_23.setFrameShape(QFrame.Shape.VLine)
        self.Audio_filter_line_23.setFrameShadow(QFrame.Shadow.Sunken)
        self.Audio_filter_label_22 = QLabel(self.Audio_filter_groupBox)
        self.Audio_filter_label_22.setObjectName(u"Audio_filter_label_22")
        self.Audio_filter_label_22.setGeometry(QRect(330, 315, 41, 21))
        self.Audio_filter_label_22.setFont(font9)
        self.Audio_filter_label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.Audio_filter_label_22.setWordWrap(True)
        self.Audio_filter_horizontalSlider_2 = QSlider(self.Audio_filter_groupBox)
        self.Audio_filter_horizontalSlider_2.setObjectName(u"Audio_filter_horizontalSlider_2")
        self.Audio_filter_horizontalSlider_2.setGeometry(QRect(380, 300, 161, 51))
        self.Audio_filter_horizontalSlider_2.setAutoFillBackground(False)
        self.Audio_filter_horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal{background: lightgray; height: 10px; border-radius: 3px;}\n"
"QSlider::handle:horizontal{background: lightblue; border: 1px solid black; width: 10px; height: 30px; margin-top: -10px; margin-bottom: -10px; border-radius: 5px;}\n"
"QSlider::sub-page:horizontal{background: white;}\n"
"QSlider::add-page:horizontal{background: white;}")
        self.Audio_filter_horizontalSlider_2.setMinimum(0)
        self.Audio_filter_horizontalSlider_2.setMaximum(67)
        self.Audio_filter_horizontalSlider_2.setPageStep(1)
        self.Audio_filter_horizontalSlider_2.setValue(0)
        self.Audio_filter_horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.Audio_filter_horizontalSlider_2.setInvertedAppearance(False)
        self.Audio_filter_horizontalSlider_2.setInvertedControls(False)
        self.Audio_filter_horizontalSlider_2.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.Audio_filter_horizontalSlider_2.setTickInterval(5)
        self.Audio_filter_horizontalSlider_2.setProperty(u"side", 2)
        self.Audio_filter_label_23 = QLabel(self.Audio_filter_groupBox)
        self.Audio_filter_label_23.setObjectName(u"Audio_filter_label_23")
        self.Audio_filter_label_23.setGeometry(QRect(320, 370, 51, 21))
        self.Audio_filter_label_23.setFont(font9)
        self.Audio_filter_label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.Audio_filter_label_23.setWordWrap(True)
        self.Audio_filter_line_22 = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_line_22.setObjectName(u"Audio_filter_line_22")
        self.Audio_filter_line_22.setGeometry(QRect(485, 435, 61, 2))
        self.Audio_filter_line_22.setStyleSheet(u"QFrame{border: none; background-color: black;  max-height: 2px;}")
        self.Audio_filter_line_22.setFrameShape(QFrame.Shape.HLine)
        self.Audio_filter_line_22.setFrameShadow(QFrame.Shadow.Sunken)
        self.Audio_filter_comboBox_2 = QComboBox(self.Audio_filter_groupBox)
        self.Audio_filter_comboBox_2.addItem("")
        self.Audio_filter_comboBox_2.addItem("")
        self.Audio_filter_comboBox_2.setObjectName(u"Audio_filter_comboBox_2")
        self.Audio_filter_comboBox_2.setGeometry(QRect(380, 365, 91, 31))
        self.Audio_filter_comboBox_2.setProperty(u"side", 2)
        self.Audio_filter_line_24 = QFrame(self.Audio_filter_groupBox)
        self.Audio_filter_line_24.setObjectName(u"Audio_filter_line_24")
        self.Audio_filter_line_24.setGeometry(QRect(545, 420, 2, 17))
        self.Audio_filter_line_24.setStyleSheet(u"QFrame{border: none; background-color: black; max-width: 2px;}")
        self.Audio_filter_line_24.setFrameShape(QFrame.Shape.VLine)
        self.Audio_filter_line_24.setFrameShadow(QFrame.Shadow.Sunken)
        self.Audio_filter_label_21 = QLabel(self.Audio_filter_groupBox)
        self.Audio_filter_label_21.setObjectName(u"Audio_filter_label_21")
        self.Audio_filter_label_21.setGeometry(QRect(410, 425, 91, 21))
        self.Audio_filter_label_21.setFont(font9)
        self.Audio_filter_label_21.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.Audio_filter_label_21.setWordWrap(True)
        self.Audio_filter_freq_label_1 = QLabel(self.Audio_filter_groupBox)
        self.Audio_filter_freq_label_1.setObjectName(u"Audio_filter_freq_label_1")
        self.Audio_filter_freq_label_1.setGeometry(QRect(250, 315, 31, 21))
        self.Audio_filter_freq_label_1.setFont(font13)
        self.Audio_filter_freq_label_1.setTextFormat(Qt.TextFormat.PlainText)
        self.Audio_filter_freq_label_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.Audio_filter_freq_label_1.setWordWrap(True)
        self.Audio_filter_freq_label_2 = QLabel(self.Audio_filter_groupBox)
        self.Audio_filter_freq_label_2.setObjectName(u"Audio_filter_freq_label_2")
        self.Audio_filter_freq_label_2.setGeometry(QRect(550, 315, 31, 21))
        self.Audio_filter_freq_label_2.setFont(font13)
        self.Audio_filter_freq_label_2.setTextFormat(Qt.TextFormat.PlainText)
        self.Audio_filter_freq_label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.Audio_filter_freq_label_2.setWordWrap(True)
        self.Radio_tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_5.setStyleSheet(u"QWidget{ background-color: gray}")
        self.menu_groupBox = QGroupBox(self.tab_5)
        self.menu_groupBox.setObjectName(u"menu_groupBox")
        self.menu_groupBox.setGeometry(QRect(20, 20, 771, 851))
        self.menu_groupBox.setFont(font1)
        self.menu_groupBox.setStyleSheet(u"QWidget{ background-color: lightgray;}")
        self.menu_scroll_area = QScrollArea(self.menu_groupBox)
        self.menu_scroll_area.setObjectName(u"menu_scroll_area")
        self.menu_scroll_area.setGeometry(QRect(10, 27, 751, 801))
        sizePolicy.setHeightForWidth(self.menu_scroll_area.sizePolicy().hasHeightForWidth())
        self.menu_scroll_area.setSizePolicy(sizePolicy)
        self.menu_scroll_area.setStyleSheet(u"QWidget{ background-color: lightgray}\n"
"QScrollArea{ padding: 20px;border-radius: 5px}\n"
"QScrollBar:vertical {width: 20px;}")
        self.menu_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.menu_scroll_area.setWidgetResizable(True)
        self.menu_scroll_area_contents = QWidget()
        self.menu_scroll_area_contents.setObjectName(u"menu_scroll_area_contents")
        self.menu_scroll_area_contents.setGeometry(QRect(0, 0, 691, 4910))
        sizePolicy.setHeightForWidth(self.menu_scroll_area_contents.sizePolicy().hasHeightForWidth())
        self.menu_scroll_area_contents.setSizePolicy(sizePolicy)
        self.menu_scroll_area_contents.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.menu_scroll_area_contents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.menu_grid = QGridLayout()
        self.menu_grid.setSpacing(6)
        self.menu_grid.setObjectName(u"menu_grid")
        self.menu_grid.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.menu_comboBox_46 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_46.setObjectName(u"menu_comboBox_46")

        self.menu_grid.addWidget(self.menu_comboBox_46, 45, 2, 1, 1)

        self.menu_comboBox_60 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_60.setObjectName(u"menu_comboBox_60")

        self.menu_grid.addWidget(self.menu_comboBox_60, 59, 2, 1, 1)

        self.menu_pushButton_2 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_2.setObjectName(u"menu_pushButton_2")

        self.menu_grid.addWidget(self.menu_pushButton_2, 1, 3, 1, 1)

        self.menu_pushButton_105 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_105.setObjectName(u"menu_pushButton_105")

        self.menu_grid.addWidget(self.menu_pushButton_105, 104, 3, 1, 1)

        self.menu_pushButton_52 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_52.setObjectName(u"menu_pushButton_52")

        self.menu_grid.addWidget(self.menu_pushButton_52, 51, 3, 1, 1)

        self.menu_pushButton_153 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_153.setObjectName(u"menu_pushButton_153")

        self.menu_grid.addWidget(self.menu_pushButton_153, 152, 3, 1, 1)

        self.menu_comboBox_130 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_130.setObjectName(u"menu_comboBox_130")

        self.menu_grid.addWidget(self.menu_comboBox_130, 129, 2, 1, 1)

        self.menu_comboBox_50 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_50.setObjectName(u"menu_comboBox_50")

        self.menu_grid.addWidget(self.menu_comboBox_50, 49, 2, 1, 1)

        self.menu_pushButton_140 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_140.setObjectName(u"menu_pushButton_140")

        self.menu_grid.addWidget(self.menu_pushButton_140, 139, 3, 1, 1)

        self.menu_label_57 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_57.setObjectName(u"menu_label_57")

        self.menu_grid.addWidget(self.menu_label_57, 28, 0, 1, 1)

        self.menu_label_55 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_55.setObjectName(u"menu_label_55")

        self.menu_grid.addWidget(self.menu_label_55, 27, 0, 1, 1)

        self.menu_label_56 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_56.setObjectName(u"menu_label_56")

        self.menu_grid.addWidget(self.menu_label_56, 27, 1, 1, 1)

        self.menu_comboBox_134 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_134.setObjectName(u"menu_comboBox_134")

        self.menu_grid.addWidget(self.menu_comboBox_134, 133, 2, 1, 1)

        self.menu_label_67 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_67.setObjectName(u"menu_label_67")

        self.menu_grid.addWidget(self.menu_label_67, 33, 0, 1, 1)

        self.menu_pushButton_95 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_95.setObjectName(u"menu_pushButton_95")

        self.menu_grid.addWidget(self.menu_pushButton_95, 94, 3, 1, 1)

        self.menu_pushButton_27 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_27.setObjectName(u"menu_pushButton_27")

        self.menu_grid.addWidget(self.menu_pushButton_27, 26, 3, 1, 1)

        self.menu_label_126 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_126.setObjectName(u"menu_label_126")

        self.menu_grid.addWidget(self.menu_label_126, 62, 1, 1, 1)

        self.menu_comboBox_139 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_139.setObjectName(u"menu_comboBox_139")

        self.menu_grid.addWidget(self.menu_comboBox_139, 138, 2, 1, 1)

        self.menu_pushButton_147 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_147.setObjectName(u"menu_pushButton_147")

        self.menu_grid.addWidget(self.menu_pushButton_147, 146, 3, 1, 1)

        self.menu_comboBox_145 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_145.setObjectName(u"menu_comboBox_145")

        self.menu_grid.addWidget(self.menu_comboBox_145, 144, 2, 1, 1)

        self.menu_label_28 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_28.setObjectName(u"menu_label_28")

        self.menu_grid.addWidget(self.menu_label_28, 13, 1, 1, 1)

        self.menu_label_46 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_46.setObjectName(u"menu_label_46")

        self.menu_grid.addWidget(self.menu_label_46, 22, 1, 1, 1)

        self.menu_pushButton_3 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_3.setObjectName(u"menu_pushButton_3")

        self.menu_grid.addWidget(self.menu_pushButton_3, 2, 3, 1, 1)

        self.menu_pushButton_40 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_40.setObjectName(u"menu_pushButton_40")

        self.menu_grid.addWidget(self.menu_pushButton_40, 39, 3, 1, 1)

        self.menu_comboBox_150 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_150.setObjectName(u"menu_comboBox_150")

        self.menu_grid.addWidget(self.menu_comboBox_150, 149, 2, 1, 1)

        self.menu_pushButton_134 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_134.setObjectName(u"menu_pushButton_134")

        self.menu_grid.addWidget(self.menu_pushButton_134, 133, 3, 1, 1)

        self.menu_label_49 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_49.setObjectName(u"menu_label_49")

        self.menu_grid.addWidget(self.menu_label_49, 24, 0, 1, 1)

        self.menu_label_14 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_14.setObjectName(u"menu_label_14")

        self.menu_grid.addWidget(self.menu_label_14, 6, 1, 1, 1)

        self.menu_pushButton_44 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_44.setObjectName(u"menu_pushButton_44")

        self.menu_grid.addWidget(self.menu_pushButton_44, 43, 3, 1, 1)

        self.menu_label_63 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_63.setObjectName(u"menu_label_63")

        self.menu_grid.addWidget(self.menu_label_63, 31, 0, 1, 1)

        self.menu_comboBox_87 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_87.setObjectName(u"menu_comboBox_87")

        self.menu_grid.addWidget(self.menu_comboBox_87, 86, 2, 1, 1)

        self.menu_pushButton_64 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_64.setObjectName(u"menu_pushButton_64")

        self.menu_grid.addWidget(self.menu_pushButton_64, 63, 3, 1, 1)

        self.menu_comboBox_42 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_42.setObjectName(u"menu_comboBox_42")

        self.menu_grid.addWidget(self.menu_comboBox_42, 41, 2, 1, 1)

        self.menu_label_99 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_99.setObjectName(u"menu_label_99")

        self.menu_grid.addWidget(self.menu_label_99, 49, 0, 1, 1)

        self.menu_pushButton_76 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_76.setObjectName(u"menu_pushButton_76")

        self.menu_grid.addWidget(self.menu_pushButton_76, 75, 3, 1, 1)

        self.menu_pushButton_109 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_109.setObjectName(u"menu_pushButton_109")

        self.menu_grid.addWidget(self.menu_pushButton_109, 108, 3, 1, 1)

        self.menu_label_174 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_174.setObjectName(u"menu_label_174")

        self.menu_grid.addWidget(self.menu_label_174, 86, 1, 1, 1)

        self.menu_pushButton_61 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_61.setObjectName(u"menu_pushButton_61")

        self.menu_grid.addWidget(self.menu_pushButton_61, 60, 3, 1, 1)

        self.menu_label_18 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_18.setObjectName(u"menu_label_18")

        self.menu_grid.addWidget(self.menu_label_18, 8, 1, 1, 1)

        self.menu_comboBox_96 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_96.setObjectName(u"menu_comboBox_96")

        self.menu_grid.addWidget(self.menu_comboBox_96, 95, 2, 1, 1)

        self.menu_pushButton_7 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_7.setObjectName(u"menu_pushButton_7")

        self.menu_grid.addWidget(self.menu_pushButton_7, 6, 3, 1, 1)

        self.menu_label_50 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_50.setObjectName(u"menu_label_50")

        self.menu_grid.addWidget(self.menu_label_50, 24, 1, 1, 1)

        self.menu_pushButton_84 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_84.setObjectName(u"menu_pushButton_84")

        self.menu_grid.addWidget(self.menu_pushButton_84, 83, 3, 1, 1)

        self.menu_pushButton_142 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_142.setObjectName(u"menu_pushButton_142")

        self.menu_grid.addWidget(self.menu_pushButton_142, 141, 3, 1, 1)

        self.menu_comboBox_56 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_56.setObjectName(u"menu_comboBox_56")

        self.menu_grid.addWidget(self.menu_comboBox_56, 55, 2, 1, 1)

        self.menu_pushButton_127 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_127.setObjectName(u"menu_pushButton_127")

        self.menu_grid.addWidget(self.menu_pushButton_127, 126, 3, 1, 1)

        self.menu_comboBox_52 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_52.setObjectName(u"menu_comboBox_52")

        self.menu_grid.addWidget(self.menu_comboBox_52, 51, 2, 1, 1)

        self.menu_label_162 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_162.setObjectName(u"menu_label_162")

        self.menu_grid.addWidget(self.menu_label_162, 80, 1, 1, 1)

        self.menu_comboBox_92 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_92.setObjectName(u"menu_comboBox_92")

        self.menu_grid.addWidget(self.menu_comboBox_92, 91, 2, 1, 1)

        self.menu_label_23 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_23.setObjectName(u"menu_label_23")

        self.menu_grid.addWidget(self.menu_label_23, 11, 0, 1, 1)

        self.menu_label_43 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_43.setObjectName(u"menu_label_43")

        self.menu_grid.addWidget(self.menu_label_43, 21, 0, 1, 1)

        self.menu_label_112 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_112.setObjectName(u"menu_label_112")

        self.menu_grid.addWidget(self.menu_label_112, 55, 1, 1, 1)

        self.menu_label_34 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_34.setObjectName(u"menu_label_34")

        self.menu_grid.addWidget(self.menu_label_34, 16, 1, 1, 1)

        self.menu_pushButton_50 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_50.setObjectName(u"menu_pushButton_50")

        self.menu_grid.addWidget(self.menu_pushButton_50, 49, 3, 1, 1)

        self.menu_pushButton_133 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_133.setObjectName(u"menu_pushButton_133")

        self.menu_grid.addWidget(self.menu_pushButton_133, 132, 3, 1, 1)

        self.menu_label_70 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_70.setObjectName(u"menu_label_70")

        self.menu_grid.addWidget(self.menu_label_70, 34, 1, 1, 1)

        self.menu_comboBox_133 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_133.setObjectName(u"menu_comboBox_133")

        self.menu_grid.addWidget(self.menu_comboBox_133, 132, 2, 1, 1)

        self.menu_comboBox_67 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_67.setObjectName(u"menu_comboBox_67")

        self.menu_grid.addWidget(self.menu_comboBox_67, 66, 2, 1, 1)

        self.menu_label_173 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_173.setObjectName(u"menu_label_173")

        self.menu_grid.addWidget(self.menu_label_173, 86, 0, 1, 1)

        self.menu_pushButton_42 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_42.setObjectName(u"menu_pushButton_42")

        self.menu_grid.addWidget(self.menu_pushButton_42, 41, 3, 1, 1)

        self.menu_comboBox_65 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_65.setObjectName(u"menu_comboBox_65")

        self.menu_grid.addWidget(self.menu_comboBox_65, 64, 2, 1, 1)

        self.menu_pushButton_66 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_66.setObjectName(u"menu_pushButton_66")

        self.menu_grid.addWidget(self.menu_pushButton_66, 65, 3, 1, 1)

        self.menu_label_96 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_96.setObjectName(u"menu_label_96")

        self.menu_grid.addWidget(self.menu_label_96, 47, 1, 1, 1)

        self.menu_pushButton_10 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_10.setObjectName(u"menu_pushButton_10")

        self.menu_grid.addWidget(self.menu_pushButton_10, 9, 3, 1, 1)

        self.menu_label_10 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_10.setObjectName(u"menu_label_10")

        self.menu_grid.addWidget(self.menu_label_10, 4, 1, 1, 1)

        self.menu_comboBox_15 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_15.setObjectName(u"menu_comboBox_15")

        self.menu_grid.addWidget(self.menu_comboBox_15, 14, 2, 1, 1)

        self.menu_comboBox_13 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_13.setObjectName(u"menu_comboBox_13")

        self.menu_grid.addWidget(self.menu_comboBox_13, 12, 2, 1, 1)

        self.menu_label_4 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_4.setObjectName(u"menu_label_4")

        self.menu_grid.addWidget(self.menu_label_4, 1, 1, 1, 1)

        self.menu_comboBox_152 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_152.setObjectName(u"menu_comboBox_152")

        self.menu_grid.addWidget(self.menu_comboBox_152, 151, 2, 1, 1)

        self.menu_comboBox_68 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_68.setObjectName(u"menu_comboBox_68")

        self.menu_grid.addWidget(self.menu_comboBox_68, 67, 2, 1, 1)

        self.menu_pushButton_90 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_90.setObjectName(u"menu_pushButton_90")

        self.menu_grid.addWidget(self.menu_pushButton_90, 89, 3, 1, 1)

        self.menu_comboBox_102 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_102.setObjectName(u"menu_comboBox_102")

        self.menu_grid.addWidget(self.menu_comboBox_102, 101, 2, 1, 1)

        self.menu_pushButton_122 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_122.setObjectName(u"menu_pushButton_122")

        self.menu_grid.addWidget(self.menu_pushButton_122, 121, 3, 1, 1)

        self.menu_comboBox_108 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_108.setObjectName(u"menu_comboBox_108")

        self.menu_grid.addWidget(self.menu_comboBox_108, 107, 2, 1, 1)

        self.menu_label_89 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_89.setObjectName(u"menu_label_89")

        self.menu_grid.addWidget(self.menu_label_89, 44, 0, 1, 1)

        self.menu_label_146 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_146.setObjectName(u"menu_label_146")

        self.menu_grid.addWidget(self.menu_label_146, 72, 1, 1, 1)

        self.menu_label_8 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_8.setObjectName(u"menu_label_8")

        self.menu_grid.addWidget(self.menu_label_8, 3, 1, 1, 1)

        self.menu_pushButton_114 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_114.setObjectName(u"menu_pushButton_114")

        self.menu_grid.addWidget(self.menu_pushButton_114, 113, 3, 1, 1)

        self.menu_label_128 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_128.setObjectName(u"menu_label_128")

        self.menu_grid.addWidget(self.menu_label_128, 63, 1, 1, 1)

        self.menu_comboBox_118 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_118.setObjectName(u"menu_comboBox_118")

        self.menu_grid.addWidget(self.menu_comboBox_118, 117, 2, 1, 1)

        self.menu_comboBox_49 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_49.setObjectName(u"menu_comboBox_49")

        self.menu_grid.addWidget(self.menu_comboBox_49, 48, 2, 1, 1)

        self.menu_pushButton_80 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_80.setObjectName(u"menu_pushButton_80")

        self.menu_grid.addWidget(self.menu_pushButton_80, 79, 3, 1, 1)

        self.menu_pushButton_25 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_25.setObjectName(u"menu_pushButton_25")

        self.menu_grid.addWidget(self.menu_pushButton_25, 24, 3, 1, 1)

        self.menu_label_31 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_31.setObjectName(u"menu_label_31")

        self.menu_grid.addWidget(self.menu_label_31, 15, 0, 1, 1)

        self.menu_label_150 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_150.setObjectName(u"menu_label_150")

        self.menu_grid.addWidget(self.menu_label_150, 74, 1, 1, 1)

        self.menu_pushButton_71 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_71.setObjectName(u"menu_pushButton_71")

        self.menu_grid.addWidget(self.menu_pushButton_71, 70, 3, 1, 1)

        self.menu_pushButton_83 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_83.setObjectName(u"menu_pushButton_83")

        self.menu_grid.addWidget(self.menu_pushButton_83, 82, 3, 1, 1)

        self.menu_label_107 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_107.setObjectName(u"menu_label_107")

        self.menu_grid.addWidget(self.menu_label_107, 53, 0, 1, 1)

        self.menu_label_61 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_61.setObjectName(u"menu_label_61")

        self.menu_grid.addWidget(self.menu_label_61, 30, 0, 1, 1)

        self.menu_label_144 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_144.setObjectName(u"menu_label_144")

        self.menu_grid.addWidget(self.menu_label_144, 71, 1, 1, 1)

        self.menu_label_148 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_148.setObjectName(u"menu_label_148")

        self.menu_grid.addWidget(self.menu_label_148, 73, 1, 1, 1)

        self.menu_label_101 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_101.setObjectName(u"menu_label_101")

        self.menu_grid.addWidget(self.menu_label_101, 50, 0, 1, 1)

        self.menu_pushButton_137 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_137.setObjectName(u"menu_pushButton_137")

        self.menu_grid.addWidget(self.menu_pushButton_137, 136, 3, 1, 1)

        self.menu_comboBox_75 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_75.setObjectName(u"menu_comboBox_75")

        self.menu_grid.addWidget(self.menu_comboBox_75, 74, 2, 1, 1)

        self.menu_label_51 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_51.setObjectName(u"menu_label_51")

        self.menu_grid.addWidget(self.menu_label_51, 25, 0, 1, 1)

        self.menu_pushButton_56 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_56.setObjectName(u"menu_pushButton_56")

        self.menu_grid.addWidget(self.menu_pushButton_56, 55, 3, 1, 1)

        self.menu_label_36 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_36.setObjectName(u"menu_label_36")

        self.menu_grid.addWidget(self.menu_label_36, 17, 1, 1, 1)

        self.menu_pushButton_135 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_135.setObjectName(u"menu_pushButton_135")

        self.menu_grid.addWidget(self.menu_pushButton_135, 134, 3, 1, 1)

        self.menu_pushButton_129 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_129.setObjectName(u"menu_pushButton_129")

        self.menu_grid.addWidget(self.menu_pushButton_129, 128, 3, 1, 1)

        self.menu_label_69 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_69.setObjectName(u"menu_label_69")

        self.menu_grid.addWidget(self.menu_label_69, 34, 0, 1, 1)

        self.menu_label_140 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_140.setObjectName(u"menu_label_140")

        self.menu_grid.addWidget(self.menu_label_140, 69, 1, 1, 1)

        self.menu_comboBox_73 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_73.setObjectName(u"menu_comboBox_73")

        self.menu_grid.addWidget(self.menu_comboBox_73, 72, 2, 1, 1)

        self.menu_pushButton_93 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_93.setObjectName(u"menu_pushButton_93")

        self.menu_grid.addWidget(self.menu_pushButton_93, 92, 3, 1, 1)

        self.menu_label_47 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_47.setObjectName(u"menu_label_47")

        self.menu_grid.addWidget(self.menu_label_47, 23, 0, 1, 1)

        self.menu_label_75 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_75.setObjectName(u"menu_label_75")

        self.menu_grid.addWidget(self.menu_label_75, 37, 0, 1, 1)

        self.menu_pushButton_77 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_77.setObjectName(u"menu_pushButton_77")

        self.menu_grid.addWidget(self.menu_pushButton_77, 76, 3, 1, 1)

        self.menu_pushButton_130 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_130.setObjectName(u"menu_pushButton_130")

        self.menu_grid.addWidget(self.menu_pushButton_130, 129, 3, 1, 1)

        self.menu_pushButton_67 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_67.setObjectName(u"menu_pushButton_67")

        self.menu_grid.addWidget(self.menu_pushButton_67, 66, 3, 1, 1)

        self.menu_comboBox_8 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_8.setObjectName(u"menu_comboBox_8")

        self.menu_grid.addWidget(self.menu_comboBox_8, 7, 2, 1, 1)

        self.menu_comboBox_127 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_127.setObjectName(u"menu_comboBox_127")

        self.menu_grid.addWidget(self.menu_comboBox_127, 126, 2, 1, 1)

        self.menu_comboBox_74 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_74.setObjectName(u"menu_comboBox_74")

        self.menu_grid.addWidget(self.menu_comboBox_74, 73, 2, 1, 1)

        self.menu_comboBox_57 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_57.setObjectName(u"menu_comboBox_57")

        self.menu_grid.addWidget(self.menu_comboBox_57, 56, 2, 1, 1)

        self.menu_pushButton_69 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_69.setObjectName(u"menu_pushButton_69")

        self.menu_grid.addWidget(self.menu_pushButton_69, 68, 3, 1, 1)

        self.menu_label_54 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_54.setObjectName(u"menu_label_54")

        self.menu_grid.addWidget(self.menu_label_54, 26, 1, 1, 1)

        self.menu_comboBox_140 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_140.setObjectName(u"menu_comboBox_140")

        self.menu_grid.addWidget(self.menu_comboBox_140, 139, 2, 1, 1)

        self.menu_comboBox_38 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_38.setObjectName(u"menu_comboBox_38")

        self.menu_grid.addWidget(self.menu_comboBox_38, 37, 2, 1, 1)

        self.menu_pushButton_82 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_82.setObjectName(u"menu_pushButton_82")

        self.menu_grid.addWidget(self.menu_pushButton_82, 81, 3, 1, 1)

        self.menu_pushButton_117 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_117.setObjectName(u"menu_pushButton_117")

        self.menu_grid.addWidget(self.menu_pushButton_117, 116, 3, 1, 1)

        self.menu_pushButton_68 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_68.setObjectName(u"menu_pushButton_68")

        self.menu_grid.addWidget(self.menu_pushButton_68, 67, 3, 1, 1)

        self.menu_label_109 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_109.setObjectName(u"menu_label_109")

        self.menu_grid.addWidget(self.menu_label_109, 54, 0, 1, 1)

        self.menu_label_154 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_154.setObjectName(u"menu_label_154")

        self.menu_grid.addWidget(self.menu_label_154, 76, 1, 1, 1)

        self.menu_comboBox_33 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_33.setObjectName(u"menu_comboBox_33")

        self.menu_grid.addWidget(self.menu_comboBox_33, 32, 2, 1, 1)

        self.menu_pushButton_48 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_48.setObjectName(u"menu_pushButton_48")

        self.menu_grid.addWidget(self.menu_pushButton_48, 47, 3, 1, 1)

        self.menu_pushButton_79 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_79.setObjectName(u"menu_pushButton_79")

        self.menu_grid.addWidget(self.menu_pushButton_79, 78, 3, 1, 1)

        self.menu_label_21 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_21.setObjectName(u"menu_label_21")

        self.menu_grid.addWidget(self.menu_label_21, 10, 0, 1, 1)

        self.menu_label_135 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_135.setObjectName(u"menu_label_135")

        self.menu_grid.addWidget(self.menu_label_135, 67, 0, 1, 1)

        self.menu_comboBox_27 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_27.setObjectName(u"menu_comboBox_27")

        self.menu_grid.addWidget(self.menu_comboBox_27, 26, 2, 1, 1)

        self.menu_pushButton_112 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_112.setObjectName(u"menu_pushButton_112")

        self.menu_grid.addWidget(self.menu_pushButton_112, 111, 3, 1, 1)

        self.menu_pushButton_138 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_138.setObjectName(u"menu_pushButton_138")

        self.menu_grid.addWidget(self.menu_pushButton_138, 137, 3, 1, 1)

        self.menu_label_120 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_120.setObjectName(u"menu_label_120")

        self.menu_grid.addWidget(self.menu_label_120, 59, 1, 1, 1)

        self.menu_label_9 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_9.setObjectName(u"menu_label_9")

        self.menu_grid.addWidget(self.menu_label_9, 4, 0, 1, 1)

        self.menu_pushButton_8 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_8.setObjectName(u"menu_pushButton_8")

        self.menu_grid.addWidget(self.menu_pushButton_8, 7, 3, 1, 1)

        self.menu_pushButton_110 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_110.setObjectName(u"menu_pushButton_110")

        self.menu_grid.addWidget(self.menu_pushButton_110, 109, 3, 1, 1)

        self.menu_label_130 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_130.setObjectName(u"menu_label_130")

        self.menu_grid.addWidget(self.menu_label_130, 64, 1, 1, 1)

        self.menu_label_113 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_113.setObjectName(u"menu_label_113")

        self.menu_grid.addWidget(self.menu_label_113, 56, 0, 1, 1)

        self.menu_comboBox_47 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_47.setObjectName(u"menu_comboBox_47")

        self.menu_grid.addWidget(self.menu_comboBox_47, 46, 2, 1, 1)

        self.menu_pushButton_126 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_126.setObjectName(u"menu_pushButton_126")

        self.menu_grid.addWidget(self.menu_pushButton_126, 125, 3, 1, 1)

        self.menu_label_175 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_175.setObjectName(u"menu_label_175")

        self.menu_grid.addWidget(self.menu_label_175, 87, 0, 1, 1)

        self.menu_comboBox_123 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_123.setObjectName(u"menu_comboBox_123")

        self.menu_grid.addWidget(self.menu_comboBox_123, 122, 2, 1, 1)

        self.menu_label_42 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_42.setObjectName(u"menu_label_42")

        self.menu_grid.addWidget(self.menu_label_42, 20, 1, 1, 1)

        self.menu_pushButton_62 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_62.setObjectName(u"menu_pushButton_62")

        self.menu_grid.addWidget(self.menu_pushButton_62, 61, 3, 1, 1)

        self.menu_label_45 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_45.setObjectName(u"menu_label_45")

        self.menu_grid.addWidget(self.menu_label_45, 22, 0, 1, 1)

        self.menu_pushButton_28 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_28.setObjectName(u"menu_pushButton_28")

        self.menu_grid.addWidget(self.menu_pushButton_28, 27, 3, 1, 1)

        self.menu_pushButton_141 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_141.setObjectName(u"menu_pushButton_141")

        self.menu_grid.addWidget(self.menu_pushButton_141, 140, 3, 1, 1)

        self.menu_label_25 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_25.setObjectName(u"menu_label_25")

        self.menu_grid.addWidget(self.menu_label_25, 12, 0, 1, 1)

        self.menu_comboBox_104 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_104.setObjectName(u"menu_comboBox_104")

        self.menu_grid.addWidget(self.menu_comboBox_104, 103, 2, 1, 1)

        self.menu_comboBox_120 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_120.setObjectName(u"menu_comboBox_120")

        self.menu_grid.addWidget(self.menu_comboBox_120, 119, 2, 1, 1)

        self.menu_comboBox_126 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_126.setObjectName(u"menu_comboBox_126")

        self.menu_grid.addWidget(self.menu_comboBox_126, 125, 2, 1, 1)

        self.menu_label_65 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_65.setObjectName(u"menu_label_65")

        self.menu_grid.addWidget(self.menu_label_65, 32, 0, 1, 1)

        self.menu_comboBox_93 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_93.setObjectName(u"menu_comboBox_93")

        self.menu_grid.addWidget(self.menu_comboBox_93, 92, 2, 1, 1)

        self.menu_label_169 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_169.setObjectName(u"menu_label_169")

        self.menu_grid.addWidget(self.menu_label_169, 84, 0, 1, 1)

        self.menu_label_116 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_116.setObjectName(u"menu_label_116")

        self.menu_grid.addWidget(self.menu_label_116, 57, 1, 1, 1)

        self.menu_comboBox_143 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_143.setObjectName(u"menu_comboBox_143")

        self.menu_grid.addWidget(self.menu_comboBox_143, 142, 2, 1, 1)

        self.menu_comboBox_54 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_54.setObjectName(u"menu_comboBox_54")

        self.menu_grid.addWidget(self.menu_comboBox_54, 53, 2, 1, 1)

        self.menu_label_180 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_180.setObjectName(u"menu_label_180")

        self.menu_grid.addWidget(self.menu_label_180, 89, 1, 1, 1)

        self.menu_comboBox_59 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_59.setObjectName(u"menu_comboBox_59")

        self.menu_grid.addWidget(self.menu_comboBox_59, 58, 2, 1, 1)

        self.menu_comboBox_88 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_88.setObjectName(u"menu_comboBox_88")

        self.menu_grid.addWidget(self.menu_comboBox_88, 87, 2, 1, 1)

        self.menu_label_40 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_40.setObjectName(u"menu_label_40")

        self.menu_grid.addWidget(self.menu_label_40, 19, 1, 1, 1)

        self.menu_pushButton_43 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_43.setObjectName(u"menu_pushButton_43")

        self.menu_grid.addWidget(self.menu_pushButton_43, 42, 3, 1, 1)

        self.menu_comboBox_28 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_28.setObjectName(u"menu_comboBox_28")

        self.menu_grid.addWidget(self.menu_comboBox_28, 27, 2, 1, 1)

        self.menu_label_15 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_15.setObjectName(u"menu_label_15")

        self.menu_grid.addWidget(self.menu_label_15, 7, 0, 1, 1)

        self.menu_comboBox_6 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_6.setObjectName(u"menu_comboBox_6")

        self.menu_grid.addWidget(self.menu_comboBox_6, 5, 2, 1, 1)

        self.menu_label_158 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_158.setObjectName(u"menu_label_158")

        self.menu_grid.addWidget(self.menu_label_158, 78, 1, 1, 1)

        self.menu_label_20 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_20.setObjectName(u"menu_label_20")

        self.menu_grid.addWidget(self.menu_label_20, 9, 1, 1, 1)

        self.menu_label_35 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_35.setObjectName(u"menu_label_35")

        self.menu_grid.addWidget(self.menu_label_35, 17, 0, 1, 1)

        self.menu_label_13 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_13.setObjectName(u"menu_label_13")

        self.menu_grid.addWidget(self.menu_label_13, 6, 0, 1, 1)

        self.menu_comboBox_109 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_109.setObjectName(u"menu_comboBox_109")

        self.menu_grid.addWidget(self.menu_comboBox_109, 108, 2, 1, 1)

        self.menu_label_170 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_170.setObjectName(u"menu_label_170")

        self.menu_grid.addWidget(self.menu_label_170, 84, 1, 1, 1)

        self.menu_pushButton_5 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_5.setObjectName(u"menu_pushButton_5")

        self.menu_grid.addWidget(self.menu_pushButton_5, 4, 3, 1, 1)

        self.menu_label_143 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_143.setObjectName(u"menu_label_143")

        self.menu_grid.addWidget(self.menu_label_143, 71, 0, 1, 1)

        self.menu_comboBox_3 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_3.setObjectName(u"menu_comboBox_3")

        self.menu_grid.addWidget(self.menu_comboBox_3, 2, 2, 1, 1)

        self.menu_pushButton_148 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_148.setObjectName(u"menu_pushButton_148")

        self.menu_grid.addWidget(self.menu_pushButton_148, 147, 3, 1, 1)

        self.menu_comboBox_45 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_45.setObjectName(u"menu_comboBox_45")

        self.menu_grid.addWidget(self.menu_comboBox_45, 44, 2, 1, 1)

        self.menu_label_12 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_12.setObjectName(u"menu_label_12")

        self.menu_grid.addWidget(self.menu_label_12, 5, 1, 1, 1)

        self.menu_label_133 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_133.setObjectName(u"menu_label_133")

        self.menu_grid.addWidget(self.menu_label_133, 66, 0, 1, 1)

        self.menu_comboBox_72 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_72.setObjectName(u"menu_comboBox_72")

        self.menu_grid.addWidget(self.menu_comboBox_72, 71, 2, 1, 1)

        self.menu_comboBox_29 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_29.setObjectName(u"menu_comboBox_29")

        self.menu_grid.addWidget(self.menu_comboBox_29, 28, 2, 1, 1)

        self.menu_comboBox_25 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_25.setObjectName(u"menu_comboBox_25")

        self.menu_grid.addWidget(self.menu_comboBox_25, 24, 2, 1, 1)

        self.menu_label_141 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_141.setObjectName(u"menu_label_141")

        self.menu_grid.addWidget(self.menu_label_141, 70, 0, 1, 1)

        self.menu_label_73 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_73.setObjectName(u"menu_label_73")

        self.menu_grid.addWidget(self.menu_label_73, 36, 0, 1, 1)

        self.menu_label_183 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_183.setObjectName(u"menu_label_183")

        self.menu_grid.addWidget(self.menu_label_183, 91, 0, 1, 1)

        self.menu_pushButton_15 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_15.setObjectName(u"menu_pushButton_15")

        self.menu_grid.addWidget(self.menu_pushButton_15, 14, 3, 1, 1)

        self.menu_pushButton_38 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_38.setObjectName(u"menu_pushButton_38")

        self.menu_grid.addWidget(self.menu_pushButton_38, 37, 3, 1, 1)

        self.menu_label_147 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_147.setObjectName(u"menu_label_147")

        self.menu_grid.addWidget(self.menu_label_147, 73, 0, 1, 1)

        self.menu_pushButton_33 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_33.setObjectName(u"menu_pushButton_33")

        self.menu_grid.addWidget(self.menu_pushButton_33, 32, 3, 1, 1)

        self.menu_comboBox_9 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_9.setObjectName(u"menu_comboBox_9")

        self.menu_grid.addWidget(self.menu_comboBox_9, 8, 2, 1, 1)

        self.menu_pushButton_94 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_94.setObjectName(u"menu_pushButton_94")

        self.menu_grid.addWidget(self.menu_pushButton_94, 93, 3, 1, 1)

        self.menu_label_137 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_137.setObjectName(u"menu_label_137")

        self.menu_grid.addWidget(self.menu_label_137, 68, 0, 1, 1)

        self.menu_pushButton_20 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_20.setObjectName(u"menu_pushButton_20")

        self.menu_grid.addWidget(self.menu_pushButton_20, 19, 3, 1, 1)

        self.menu_label_59 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_59.setObjectName(u"menu_label_59")

        self.menu_grid.addWidget(self.menu_label_59, 29, 0, 1, 1)

        self.menu_label_78 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_78.setObjectName(u"menu_label_78")

        self.menu_grid.addWidget(self.menu_label_78, 38, 1, 1, 1)

        self.menu_comboBox_16 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_16.setObjectName(u"menu_comboBox_16")

        self.menu_grid.addWidget(self.menu_comboBox_16, 15, 2, 1, 1)

        self.menu_pushButton_73 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_73.setObjectName(u"menu_pushButton_73")

        self.menu_grid.addWidget(self.menu_pushButton_73, 72, 3, 1, 1)

        self.menu_pushButton_88 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_88.setObjectName(u"menu_pushButton_88")

        self.menu_grid.addWidget(self.menu_pushButton_88, 87, 3, 1, 1)

        self.menu_pushButton_47 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_47.setObjectName(u"menu_pushButton_47")

        self.menu_grid.addWidget(self.menu_pushButton_47, 46, 3, 1, 1)

        self.menu_pushButton_23 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_23.setObjectName(u"menu_pushButton_23")

        self.menu_grid.addWidget(self.menu_pushButton_23, 22, 3, 1, 1)

        self.menu_label_124 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_124.setObjectName(u"menu_label_124")

        self.menu_grid.addWidget(self.menu_label_124, 61, 1, 1, 1)

        self.menu_label_19 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_19.setObjectName(u"menu_label_19")

        self.menu_grid.addWidget(self.menu_label_19, 9, 0, 1, 1)

        self.menu_pushButton_118 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_118.setObjectName(u"menu_pushButton_118")

        self.menu_grid.addWidget(self.menu_pushButton_118, 117, 3, 1, 1)

        self.menu_label_127 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_127.setObjectName(u"menu_label_127")

        self.menu_grid.addWidget(self.menu_label_127, 63, 0, 1, 1)

        self.menu_label_85 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_85.setObjectName(u"menu_label_85")

        self.menu_grid.addWidget(self.menu_label_85, 42, 0, 1, 1)

        self.menu_label_33 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_33.setObjectName(u"menu_label_33")

        self.menu_grid.addWidget(self.menu_label_33, 16, 0, 1, 1)

        self.menu_pushButton_19 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_19.setObjectName(u"menu_pushButton_19")

        self.menu_grid.addWidget(self.menu_pushButton_19, 18, 3, 1, 1)

        self.menu_pushButton_53 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_53.setObjectName(u"menu_pushButton_53")

        self.menu_grid.addWidget(self.menu_pushButton_53, 52, 3, 1, 1)

        self.menu_pushButton_36 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_36.setObjectName(u"menu_pushButton_36")

        self.menu_grid.addWidget(self.menu_pushButton_36, 35, 3, 1, 1)

        self.menu_pushButton_104 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_104.setObjectName(u"menu_pushButton_104")

        self.menu_grid.addWidget(self.menu_pushButton_104, 103, 3, 1, 1)

        self.menu_pushButton_34 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_34.setObjectName(u"menu_pushButton_34")

        self.menu_grid.addWidget(self.menu_pushButton_34, 33, 3, 1, 1)

        self.menu_comboBox_103 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_103.setObjectName(u"menu_comboBox_103")

        self.menu_grid.addWidget(self.menu_comboBox_103, 102, 2, 1, 1)

        self.menu_comboBox_70 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_70.setObjectName(u"menu_comboBox_70")

        self.menu_grid.addWidget(self.menu_comboBox_70, 69, 2, 1, 1)

        self.menu_comboBox_5 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_5.setObjectName(u"menu_comboBox_5")

        self.menu_grid.addWidget(self.menu_comboBox_5, 4, 2, 1, 1)

        self.menu_comboBox_117 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_117.setObjectName(u"menu_comboBox_117")

        self.menu_grid.addWidget(self.menu_comboBox_117, 116, 2, 1, 1)

        self.menu_comboBox_31 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_31.setObjectName(u"menu_comboBox_31")

        self.menu_grid.addWidget(self.menu_comboBox_31, 30, 2, 1, 1)

        self.menu_label_185 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_185.setObjectName(u"menu_label_185")

        self.menu_grid.addWidget(self.menu_label_185, 92, 0, 1, 1)

        self.menu_label_29 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_29.setObjectName(u"menu_label_29")

        self.menu_grid.addWidget(self.menu_label_29, 14, 0, 1, 1)

        self.menu_pushButton_37 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_37.setObjectName(u"menu_pushButton_37")

        self.menu_grid.addWidget(self.menu_pushButton_37, 36, 3, 1, 1)

        self.menu_label_121 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_121.setObjectName(u"menu_label_121")

        self.menu_grid.addWidget(self.menu_label_121, 60, 0, 1, 1)

        self.menu_label_105 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_105.setObjectName(u"menu_label_105")

        self.menu_grid.addWidget(self.menu_label_105, 52, 0, 1, 1)

        self.menu_comboBox_22 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_22.setObjectName(u"menu_comboBox_22")

        self.menu_grid.addWidget(self.menu_comboBox_22, 21, 2, 1, 1)

        self.menu_pushButton_26 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_26.setObjectName(u"menu_pushButton_26")

        self.menu_grid.addWidget(self.menu_pushButton_26, 25, 3, 1, 1)

        self.menu_comboBox_147 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_147.setObjectName(u"menu_comboBox_147")

        self.menu_grid.addWidget(self.menu_comboBox_147, 146, 2, 1, 1)

        self.menu_label_155 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_155.setObjectName(u"menu_label_155")

        self.menu_grid.addWidget(self.menu_label_155, 77, 0, 1, 1)

        self.menu_comboBox_89 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_89.setObjectName(u"menu_comboBox_89")

        self.menu_grid.addWidget(self.menu_comboBox_89, 88, 2, 1, 1)

        self.menu_label_163 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_163.setObjectName(u"menu_label_163")

        self.menu_grid.addWidget(self.menu_label_163, 81, 0, 1, 1)

        self.menu_label_83 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_83.setObjectName(u"menu_label_83")

        self.menu_grid.addWidget(self.menu_label_83, 41, 0, 1, 1)

        self.menu_comboBox_81 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_81.setObjectName(u"menu_comboBox_81")

        self.menu_grid.addWidget(self.menu_comboBox_81, 80, 2, 1, 1)

        self.menu_pushButton_85 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_85.setObjectName(u"menu_pushButton_85")

        self.menu_grid.addWidget(self.menu_pushButton_85, 84, 3, 1, 1)

        self.menu_comboBox_86 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_86.setObjectName(u"menu_comboBox_86")

        self.menu_grid.addWidget(self.menu_comboBox_86, 85, 2, 1, 1)

        self.menu_label_39 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_39.setObjectName(u"menu_label_39")

        self.menu_grid.addWidget(self.menu_label_39, 19, 0, 1, 1)

        self.menu_label_38 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_38.setObjectName(u"menu_label_38")

        self.menu_grid.addWidget(self.menu_label_38, 18, 1, 1, 1)

        self.menu_comboBox_91 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_91.setObjectName(u"menu_comboBox_91")

        self.menu_grid.addWidget(self.menu_comboBox_91, 90, 2, 1, 1)

        self.menu_label_93 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_93.setObjectName(u"menu_label_93")

        self.menu_grid.addWidget(self.menu_label_93, 46, 0, 1, 1)

        self.menu_label_64 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_64.setObjectName(u"menu_label_64")

        self.menu_grid.addWidget(self.menu_label_64, 31, 1, 1, 1)

        self.menu_comboBox_4 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_4.setObjectName(u"menu_comboBox_4")

        self.menu_grid.addWidget(self.menu_comboBox_4, 3, 2, 1, 1)

        self.menu_pushButton_113 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_113.setObjectName(u"menu_pushButton_113")

        self.menu_grid.addWidget(self.menu_pushButton_113, 112, 3, 1, 1)

        self.menu_label_182 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_182.setObjectName(u"menu_label_182")

        self.menu_grid.addWidget(self.menu_label_182, 90, 1, 1, 1)

        self.menu_pushButton_58 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_58.setObjectName(u"menu_pushButton_58")

        self.menu_grid.addWidget(self.menu_pushButton_58, 57, 3, 1, 1)

        self.menu_comboBox_115 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_115.setObjectName(u"menu_comboBox_115")

        self.menu_grid.addWidget(self.menu_comboBox_115, 114, 2, 1, 1)

        self.menu_label_114 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_114.setObjectName(u"menu_label_114")

        self.menu_grid.addWidget(self.menu_label_114, 56, 1, 1, 1)

        self.menu_label_117 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_117.setObjectName(u"menu_label_117")

        self.menu_grid.addWidget(self.menu_label_117, 58, 0, 1, 1)

        self.menu_label_145 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_145.setObjectName(u"menu_label_145")

        self.menu_grid.addWidget(self.menu_label_145, 72, 0, 1, 1)

        self.menu_pushButton_149 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_149.setObjectName(u"menu_pushButton_149")

        self.menu_grid.addWidget(self.menu_pushButton_149, 148, 3, 1, 1)

        self.menu_label_71 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_71.setObjectName(u"menu_label_71")

        self.menu_grid.addWidget(self.menu_label_71, 35, 0, 1, 1)

        self.menu_pushButton_14 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_14.setObjectName(u"menu_pushButton_14")

        self.menu_grid.addWidget(self.menu_pushButton_14, 13, 3, 1, 1)

        self.menu_label_44 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_44.setObjectName(u"menu_label_44")

        self.menu_grid.addWidget(self.menu_label_44, 21, 1, 1, 1)

        self.menu_label_115 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_115.setObjectName(u"menu_label_115")

        self.menu_grid.addWidget(self.menu_label_115, 57, 0, 1, 1)

        self.menu_label_66 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_66.setObjectName(u"menu_label_66")

        self.menu_grid.addWidget(self.menu_label_66, 32, 1, 1, 1)

        self.menu_comboBox_141 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_141.setObjectName(u"menu_comboBox_141")

        self.menu_grid.addWidget(self.menu_comboBox_141, 140, 2, 1, 1)

        self.menu_label_62 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_62.setObjectName(u"menu_label_62")

        self.menu_grid.addWidget(self.menu_label_62, 30, 1, 1, 1)

        self.menu_pushButton_39 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_39.setObjectName(u"menu_pushButton_39")

        self.menu_grid.addWidget(self.menu_pushButton_39, 38, 3, 1, 1)

        self.menu_comboBox_12 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_12.setObjectName(u"menu_comboBox_12")

        self.menu_grid.addWidget(self.menu_comboBox_12, 11, 2, 1, 1)

        self.menu_comboBox_97 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_97.setObjectName(u"menu_comboBox_97")

        self.menu_grid.addWidget(self.menu_comboBox_97, 96, 2, 1, 1)

        self.menu_label_91 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_91.setObjectName(u"menu_label_91")

        self.menu_grid.addWidget(self.menu_label_91, 45, 0, 1, 1)

        self.menu_comboBox_69 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_69.setObjectName(u"menu_comboBox_69")

        self.menu_grid.addWidget(self.menu_comboBox_69, 68, 2, 1, 1)

        self.menu_pushButton_123 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_123.setObjectName(u"menu_pushButton_123")

        self.menu_grid.addWidget(self.menu_pushButton_123, 122, 3, 1, 1)

        self.menu_label_167 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_167.setObjectName(u"menu_label_167")

        self.menu_grid.addWidget(self.menu_label_167, 83, 0, 1, 1)

        self.menu_comboBox_61 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_61.setObjectName(u"menu_comboBox_61")

        self.menu_grid.addWidget(self.menu_comboBox_61, 60, 2, 1, 1)

        self.menu_comboBox_90 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_90.setObjectName(u"menu_comboBox_90")

        self.menu_grid.addWidget(self.menu_comboBox_90, 89, 2, 1, 1)

        self.menu_label_53 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_53.setObjectName(u"menu_label_53")

        self.menu_grid.addWidget(self.menu_label_53, 26, 0, 1, 1)

        self.menu_comboBox_142 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_142.setObjectName(u"menu_comboBox_142")

        self.menu_grid.addWidget(self.menu_comboBox_142, 141, 2, 1, 1)

        self.menu_label_32 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_32.setObjectName(u"menu_label_32")

        self.menu_grid.addWidget(self.menu_label_32, 15, 1, 1, 1)

        self.menu_pushButton_75 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_75.setObjectName(u"menu_pushButton_75")

        self.menu_grid.addWidget(self.menu_pushButton_75, 74, 3, 1, 1)

        self.menu_label_60 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_60.setObjectName(u"menu_label_60")

        self.menu_grid.addWidget(self.menu_label_60, 29, 1, 1, 1)

        self.menu_pushButton_31 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_31.setObjectName(u"menu_pushButton_31")

        self.menu_grid.addWidget(self.menu_pushButton_31, 30, 3, 1, 1)

        self.menu_pushButton_35 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_35.setObjectName(u"menu_pushButton_35")

        self.menu_grid.addWidget(self.menu_pushButton_35, 34, 3, 1, 1)

        self.menu_pushButton_144 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_144.setObjectName(u"menu_pushButton_144")

        self.menu_grid.addWidget(self.menu_pushButton_144, 143, 3, 1, 1)

        self.menu_label_125 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_125.setObjectName(u"menu_label_125")

        self.menu_grid.addWidget(self.menu_label_125, 62, 0, 1, 1)

        self.menu_pushButton_100 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_100.setObjectName(u"menu_pushButton_100")

        self.menu_grid.addWidget(self.menu_pushButton_100, 99, 3, 1, 1)

        self.menu_comboBox_95 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_95.setObjectName(u"menu_comboBox_95")

        self.menu_grid.addWidget(self.menu_comboBox_95, 94, 2, 1, 1)

        self.menu_comboBox_151 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_151.setObjectName(u"menu_comboBox_151")

        self.menu_grid.addWidget(self.menu_comboBox_151, 150, 2, 1, 1)

        self.menu_pushButton_128 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_128.setObjectName(u"menu_pushButton_128")

        self.menu_grid.addWidget(self.menu_pushButton_128, 127, 3, 1, 1)

        self.menu_label_139 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_139.setObjectName(u"menu_label_139")

        self.menu_grid.addWidget(self.menu_label_139, 69, 0, 1, 1)

        self.menu_label_94 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_94.setObjectName(u"menu_label_94")

        self.menu_grid.addWidget(self.menu_label_94, 46, 1, 1, 1)

        self.menu_label_87 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_87.setObjectName(u"menu_label_87")

        self.menu_grid.addWidget(self.menu_label_87, 43, 0, 1, 1)

        self.menu_comboBox_2 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_2.setObjectName(u"menu_comboBox_2")

        self.menu_grid.addWidget(self.menu_comboBox_2, 1, 2, 1, 1)

        self.menu_label_166 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_166.setObjectName(u"menu_label_166")

        self.menu_grid.addWidget(self.menu_label_166, 82, 1, 1, 1)

        self.menu_pushButton_16 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_16.setObjectName(u"menu_pushButton_16")

        self.menu_grid.addWidget(self.menu_pushButton_16, 15, 3, 1, 1)

        self.menu_comboBox_17 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_17.setObjectName(u"menu_comboBox_17")

        self.menu_grid.addWidget(self.menu_comboBox_17, 16, 2, 1, 1)

        self.menu_label_11 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_11.setObjectName(u"menu_label_11")

        self.menu_grid.addWidget(self.menu_label_11, 5, 0, 1, 1)

        self.menu_comboBox_121 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_121.setObjectName(u"menu_comboBox_121")

        self.menu_grid.addWidget(self.menu_comboBox_121, 120, 2, 1, 1)

        self.menu_pushButton_45 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_45.setObjectName(u"menu_pushButton_45")

        self.menu_grid.addWidget(self.menu_pushButton_45, 44, 3, 1, 1)

        self.menu_label_111 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_111.setObjectName(u"menu_label_111")

        self.menu_grid.addWidget(self.menu_label_111, 55, 0, 1, 1)

        self.menu_comboBox_112 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_112.setObjectName(u"menu_comboBox_112")

        self.menu_grid.addWidget(self.menu_comboBox_112, 111, 2, 1, 1)

        self.menu_pushButton_59 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_59.setObjectName(u"menu_pushButton_59")

        self.menu_grid.addWidget(self.menu_pushButton_59, 58, 3, 1, 1)

        self.menu_pushButton_111 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_111.setObjectName(u"menu_pushButton_111")

        self.menu_grid.addWidget(self.menu_pushButton_111, 110, 3, 1, 1)

        self.menu_comboBox_18 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_18.setObjectName(u"menu_comboBox_18")

        self.menu_grid.addWidget(self.menu_comboBox_18, 17, 2, 1, 1)

        self.menu_pushButton_124 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_124.setObjectName(u"menu_pushButton_124")

        self.menu_grid.addWidget(self.menu_pushButton_124, 123, 3, 1, 1)

        self.menu_comboBox_11 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_11.setObjectName(u"menu_comboBox_11")

        self.menu_grid.addWidget(self.menu_comboBox_11, 10, 2, 1, 1)

        self.menu_comboBox_148 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_148.setObjectName(u"menu_comboBox_148")

        self.menu_grid.addWidget(self.menu_comboBox_148, 147, 2, 1, 1)

        self.menu_comboBox_80 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_80.setObjectName(u"menu_comboBox_80")

        self.menu_grid.addWidget(self.menu_comboBox_80, 79, 2, 1, 1)

        self.menu_comboBox_64 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_64.setObjectName(u"menu_comboBox_64")

        self.menu_grid.addWidget(self.menu_comboBox_64, 63, 2, 1, 1)

        self.menu_pushButton_1 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_1.setObjectName(u"menu_pushButton_1")
        self.menu_pushButton_1.setMaximumSize(QSize(16777215, 16777215))

        self.menu_grid.addWidget(self.menu_pushButton_1, 0, 3, 1, 1)

        self.menu_pushButton_24 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_24.setObjectName(u"menu_pushButton_24")

        self.menu_grid.addWidget(self.menu_pushButton_24, 23, 3, 1, 1)

        self.menu_pushButton_12 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_12.setObjectName(u"menu_pushButton_12")

        self.menu_grid.addWidget(self.menu_pushButton_12, 11, 3, 1, 1)

        self.menu_comboBox_40 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_40.setObjectName(u"menu_comboBox_40")

        self.menu_grid.addWidget(self.menu_comboBox_40, 39, 2, 1, 1)

        self.menu_pushButton_22 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_22.setObjectName(u"menu_pushButton_22")

        self.menu_grid.addWidget(self.menu_pushButton_22, 21, 3, 1, 1)

        self.menu_pushButton_32 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_32.setObjectName(u"menu_pushButton_32")

        self.menu_grid.addWidget(self.menu_pushButton_32, 31, 3, 1, 1)

        self.menu_comboBox_55 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_55.setObjectName(u"menu_comboBox_55")

        self.menu_grid.addWidget(self.menu_comboBox_55, 54, 2, 1, 1)

        self.menu_pushButton_87 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_87.setObjectName(u"menu_pushButton_87")

        self.menu_grid.addWidget(self.menu_pushButton_87, 86, 3, 1, 1)

        self.menu_comboBox_14 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_14.setObjectName(u"menu_comboBox_14")

        self.menu_grid.addWidget(self.menu_comboBox_14, 13, 2, 1, 1)

        self.menu_label_142 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_142.setObjectName(u"menu_label_142")

        self.menu_grid.addWidget(self.menu_label_142, 70, 1, 1, 1)

        self.menu_pushButton_41 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_41.setObjectName(u"menu_pushButton_41")

        self.menu_grid.addWidget(self.menu_pushButton_41, 40, 3, 1, 1)

        self.menu_comboBox_41 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_41.setObjectName(u"menu_comboBox_41")

        self.menu_grid.addWidget(self.menu_comboBox_41, 40, 2, 1, 1)

        self.menu_pushButton_131 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_131.setObjectName(u"menu_pushButton_131")

        self.menu_grid.addWidget(self.menu_pushButton_131, 130, 3, 1, 1)

        self.menu_comboBox_36 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_36.setObjectName(u"menu_comboBox_36")

        self.menu_grid.addWidget(self.menu_comboBox_36, 35, 2, 1, 1)

        self.menu_label_179 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_179.setObjectName(u"menu_label_179")

        self.menu_grid.addWidget(self.menu_label_179, 89, 0, 1, 1)

        self.menu_label_97 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_97.setObjectName(u"menu_label_97")

        self.menu_grid.addWidget(self.menu_label_97, 48, 0, 1, 1)

        self.menu_comboBox_48 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_48.setObjectName(u"menu_comboBox_48")

        self.menu_grid.addWidget(self.menu_comboBox_48, 47, 2, 1, 1)

        self.menu_label_17 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_17.setObjectName(u"menu_label_17")

        self.menu_grid.addWidget(self.menu_label_17, 8, 0, 1, 1)

        self.menu_comboBox_136 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_136.setObjectName(u"menu_comboBox_136")

        self.menu_grid.addWidget(self.menu_comboBox_136, 135, 2, 1, 1)

        self.menu_pushButton_51 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_51.setObjectName(u"menu_pushButton_51")

        self.menu_grid.addWidget(self.menu_pushButton_51, 50, 3, 1, 1)

        self.menu_pushButton_97 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_97.setObjectName(u"menu_pushButton_97")

        self.menu_grid.addWidget(self.menu_pushButton_97, 96, 3, 1, 1)

        self.menu_comboBox_144 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_144.setObjectName(u"menu_comboBox_144")

        self.menu_grid.addWidget(self.menu_comboBox_144, 143, 2, 1, 1)

        self.menu_pushButton_143 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_143.setObjectName(u"menu_pushButton_143")

        self.menu_grid.addWidget(self.menu_pushButton_143, 142, 3, 1, 1)

        self.menu_label_131 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_131.setObjectName(u"menu_label_131")

        self.menu_grid.addWidget(self.menu_label_131, 65, 0, 1, 1)

        self.menu_label_161 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_161.setObjectName(u"menu_label_161")

        self.menu_grid.addWidget(self.menu_label_161, 80, 0, 1, 1)

        self.menu_label_79 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_79.setObjectName(u"menu_label_79")

        self.menu_grid.addWidget(self.menu_label_79, 39, 0, 1, 1)

        self.menu_label_176 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_176.setObjectName(u"menu_label_176")

        self.menu_grid.addWidget(self.menu_label_176, 87, 1, 1, 1)

        self.menu_pushButton_108 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_108.setObjectName(u"menu_pushButton_108")

        self.menu_grid.addWidget(self.menu_pushButton_108, 107, 3, 1, 1)

        self.menu_label_5 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_5.setObjectName(u"menu_label_5")

        self.menu_grid.addWidget(self.menu_label_5, 2, 0, 1, 1)

        self.menu_comboBox_58 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_58.setObjectName(u"menu_comboBox_58")

        self.menu_grid.addWidget(self.menu_comboBox_58, 57, 2, 1, 1)

        self.menu_comboBox_106 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_106.setObjectName(u"menu_comboBox_106")

        self.menu_grid.addWidget(self.menu_comboBox_106, 105, 2, 1, 1)

        self.menu_label_82 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_82.setObjectName(u"menu_label_82")

        self.menu_grid.addWidget(self.menu_label_82, 40, 1, 1, 1)

        self.menu_label_102 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_102.setObjectName(u"menu_label_102")

        self.menu_grid.addWidget(self.menu_label_102, 50, 1, 1, 1)

        self.menu_pushButton_99 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_99.setObjectName(u"menu_pushButton_99")

        self.menu_grid.addWidget(self.menu_pushButton_99, 98, 3, 1, 1)

        self.menu_label_149 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_149.setObjectName(u"menu_label_149")

        self.menu_grid.addWidget(self.menu_label_149, 74, 0, 1, 1)

        self.menu_comboBox_100 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_100.setObjectName(u"menu_comboBox_100")

        self.menu_grid.addWidget(self.menu_comboBox_100, 99, 2, 1, 1)

        self.menu_label_58 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_58.setObjectName(u"menu_label_58")

        self.menu_grid.addWidget(self.menu_label_58, 28, 1, 1, 1)

        self.menu_pushButton_4 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_4.setObjectName(u"menu_pushButton_4")

        self.menu_grid.addWidget(self.menu_pushButton_4, 3, 3, 1, 1)

        self.menu_label_153 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_153.setObjectName(u"menu_label_153")

        self.menu_grid.addWidget(self.menu_label_153, 76, 0, 1, 1)

        self.menu_comboBox_30 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_30.setObjectName(u"menu_comboBox_30")

        self.menu_grid.addWidget(self.menu_comboBox_30, 29, 2, 1, 1)

        self.menu_pushButton_150 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_150.setObjectName(u"menu_pushButton_150")

        self.menu_grid.addWidget(self.menu_pushButton_150, 149, 3, 1, 1)

        self.menu_comboBox_20 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_20.setObjectName(u"menu_comboBox_20")

        self.menu_grid.addWidget(self.menu_comboBox_20, 19, 2, 1, 1)

        self.menu_pushButton_29 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_29.setObjectName(u"menu_pushButton_29")

        self.menu_grid.addWidget(self.menu_pushButton_29, 28, 3, 1, 1)

        self.menu_label_181 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_181.setObjectName(u"menu_label_181")

        self.menu_grid.addWidget(self.menu_label_181, 90, 0, 1, 1)

        self.menu_label_80 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_80.setObjectName(u"menu_label_80")

        self.menu_grid.addWidget(self.menu_label_80, 39, 1, 1, 1)

        self.menu_label_90 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_90.setObjectName(u"menu_label_90")

        self.menu_grid.addWidget(self.menu_label_90, 44, 1, 1, 1)

        self.menu_comboBox_19 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_19.setObjectName(u"menu_comboBox_19")

        self.menu_grid.addWidget(self.menu_comboBox_19, 18, 2, 1, 1)

        self.menu_pushButton_91 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_91.setObjectName(u"menu_pushButton_91")

        self.menu_grid.addWidget(self.menu_pushButton_91, 90, 3, 1, 1)

        self.menu_comboBox_125 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_125.setObjectName(u"menu_comboBox_125")

        self.menu_grid.addWidget(self.menu_comboBox_125, 124, 2, 1, 1)

        self.menu_comboBox_137 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_137.setObjectName(u"menu_comboBox_137")

        self.menu_grid.addWidget(self.menu_comboBox_137, 136, 2, 1, 1)

        self.menu_label_22 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_22.setObjectName(u"menu_label_22")

        self.menu_grid.addWidget(self.menu_label_22, 10, 1, 1, 1)

        self.menu_label_88 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_88.setObjectName(u"menu_label_88")

        self.menu_grid.addWidget(self.menu_label_88, 43, 1, 1, 1)

        self.menu_comboBox_113 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_113.setObjectName(u"menu_comboBox_113")

        self.menu_grid.addWidget(self.menu_comboBox_113, 112, 2, 1, 1)

        self.menu_pushButton_101 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_101.setObjectName(u"menu_pushButton_101")

        self.menu_grid.addWidget(self.menu_pushButton_101, 100, 3, 1, 1)

        self.menu_label_48 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_48.setObjectName(u"menu_label_48")

        self.menu_grid.addWidget(self.menu_label_48, 23, 1, 1, 1)

        self.menu_pushButton_6 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_6.setObjectName(u"menu_pushButton_6")

        self.menu_grid.addWidget(self.menu_pushButton_6, 5, 3, 1, 1)

        self.menu_comboBox_35 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_35.setObjectName(u"menu_comboBox_35")

        self.menu_grid.addWidget(self.menu_comboBox_35, 34, 2, 1, 1)

        self.menu_comboBox_124 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_124.setObjectName(u"menu_comboBox_124")

        self.menu_grid.addWidget(self.menu_comboBox_124, 123, 2, 1, 1)

        self.menu_label_81 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_81.setObjectName(u"menu_label_81")

        self.menu_grid.addWidget(self.menu_label_81, 40, 0, 1, 1)

        self.menu_comboBox_119 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_119.setObjectName(u"menu_comboBox_119")

        self.menu_grid.addWidget(self.menu_comboBox_119, 118, 2, 1, 1)

        self.menu_comboBox_39 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_39.setObjectName(u"menu_comboBox_39")

        self.menu_grid.addWidget(self.menu_comboBox_39, 38, 2, 1, 1)

        self.menu_label_132 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_132.setObjectName(u"menu_label_132")

        self.menu_grid.addWidget(self.menu_label_132, 65, 1, 1, 1)

        self.menu_comboBox_62 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_62.setObjectName(u"menu_comboBox_62")

        self.menu_grid.addWidget(self.menu_comboBox_62, 61, 2, 1, 1)

        self.menu_label_30 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_30.setObjectName(u"menu_label_30")

        self.menu_grid.addWidget(self.menu_label_30, 14, 1, 1, 1)

        self.menu_label_52 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_52.setObjectName(u"menu_label_52")

        self.menu_grid.addWidget(self.menu_label_52, 25, 1, 1, 1)

        self.menu_label_123 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_123.setObjectName(u"menu_label_123")

        self.menu_grid.addWidget(self.menu_label_123, 61, 0, 1, 1)

        self.menu_comboBox_79 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_79.setObjectName(u"menu_comboBox_79")

        self.menu_grid.addWidget(self.menu_comboBox_79, 78, 2, 1, 1)

        self.menu_comboBox_78 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_78.setObjectName(u"menu_comboBox_78")

        self.menu_grid.addWidget(self.menu_comboBox_78, 77, 2, 1, 1)

        self.menu_comboBox_101 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_101.setObjectName(u"menu_comboBox_101")

        self.menu_grid.addWidget(self.menu_comboBox_101, 100, 2, 1, 1)

        self.menu_comboBox_21 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_21.setObjectName(u"menu_comboBox_21")

        self.menu_grid.addWidget(self.menu_comboBox_21, 20, 2, 1, 1)

        self.menu_label_177 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_177.setObjectName(u"menu_label_177")

        self.menu_grid.addWidget(self.menu_label_177, 88, 0, 1, 1)

        self.menu_pushButton_89 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_89.setObjectName(u"menu_pushButton_89")

        self.menu_grid.addWidget(self.menu_pushButton_89, 88, 3, 1, 1)

        self.menu_pushButton_65 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_65.setObjectName(u"menu_pushButton_65")

        self.menu_grid.addWidget(self.menu_pushButton_65, 64, 3, 1, 1)

        self.menu_label_27 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_27.setObjectName(u"menu_label_27")

        self.menu_grid.addWidget(self.menu_label_27, 13, 0, 1, 1)

        self.menu_comboBox_82 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_82.setObjectName(u"menu_comboBox_82")

        self.menu_grid.addWidget(self.menu_comboBox_82, 81, 2, 1, 1)

        self.menu_comboBox_26 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_26.setObjectName(u"menu_comboBox_26")

        self.menu_grid.addWidget(self.menu_comboBox_26, 25, 2, 1, 1)

        self.menu_comboBox_24 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_24.setObjectName(u"menu_comboBox_24")

        self.menu_grid.addWidget(self.menu_comboBox_24, 23, 2, 1, 1)

        self.menu_comboBox_138 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_138.setObjectName(u"menu_comboBox_138")

        self.menu_grid.addWidget(self.menu_comboBox_138, 137, 2, 1, 1)

        self.menu_comboBox_32 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_32.setObjectName(u"menu_comboBox_32")

        self.menu_grid.addWidget(self.menu_comboBox_32, 31, 2, 1, 1)

        self.menu_comboBox_1 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_1.setObjectName(u"menu_comboBox_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_comboBox_1.sizePolicy().hasHeightForWidth())
        self.menu_comboBox_1.setSizePolicy(sizePolicy1)

        self.menu_grid.addWidget(self.menu_comboBox_1, 0, 2, 1, 1)

        self.menu_label_103 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_103.setObjectName(u"menu_label_103")

        self.menu_grid.addWidget(self.menu_label_103, 51, 0, 1, 1)

        self.menu_pushButton_49 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_49.setObjectName(u"menu_pushButton_49")

        self.menu_grid.addWidget(self.menu_pushButton_49, 48, 3, 1, 1)

        self.menu_pushButton_120 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_120.setObjectName(u"menu_pushButton_120")

        self.menu_grid.addWidget(self.menu_pushButton_120, 119, 3, 1, 1)

        self.menu_label_160 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_160.setObjectName(u"menu_label_160")

        self.menu_grid.addWidget(self.menu_label_160, 79, 1, 1, 1)

        self.menu_pushButton_106 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_106.setObjectName(u"menu_pushButton_106")

        self.menu_grid.addWidget(self.menu_pushButton_106, 105, 3, 1, 1)

        self.menu_label_2 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_2.setObjectName(u"menu_label_2")
        self.menu_label_2.setMinimumSize(QSize(0, 0))
        self.menu_label_2.setMaximumSize(QSize(16777215, 16777215))

        self.menu_grid.addWidget(self.menu_label_2, 0, 1, 1, 1)

        self.menu_comboBox_63 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_63.setObjectName(u"menu_comboBox_63")

        self.menu_grid.addWidget(self.menu_comboBox_63, 62, 2, 1, 1)

        self.menu_pushButton_81 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_81.setObjectName(u"menu_pushButton_81")

        self.menu_grid.addWidget(self.menu_pushButton_81, 80, 3, 1, 1)

        self.menu_label_178 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_178.setObjectName(u"menu_label_178")

        self.menu_grid.addWidget(self.menu_label_178, 88, 1, 1, 1)

        self.menu_comboBox_149 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_149.setObjectName(u"menu_comboBox_149")

        self.menu_grid.addWidget(self.menu_comboBox_149, 148, 2, 1, 1)

        self.menu_pushButton_119 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_119.setObjectName(u"menu_pushButton_119")

        self.menu_grid.addWidget(self.menu_pushButton_119, 118, 3, 1, 1)

        self.menu_label_156 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_156.setObjectName(u"menu_label_156")

        self.menu_grid.addWidget(self.menu_label_156, 77, 1, 1, 1)

        self.menu_comboBox_129 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_129.setObjectName(u"menu_comboBox_129")

        self.menu_grid.addWidget(self.menu_comboBox_129, 128, 2, 1, 1)

        self.menu_pushButton_13 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_13.setObjectName(u"menu_pushButton_13")

        self.menu_grid.addWidget(self.menu_pushButton_13, 12, 3, 1, 1)

        self.menu_label_26 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_26.setObjectName(u"menu_label_26")

        self.menu_grid.addWidget(self.menu_label_26, 12, 1, 1, 1)

        self.menu_comboBox_105 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_105.setObjectName(u"menu_comboBox_105")

        self.menu_grid.addWidget(self.menu_comboBox_105, 104, 2, 1, 1)

        self.menu_label_106 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_106.setObjectName(u"menu_label_106")

        self.menu_grid.addWidget(self.menu_label_106, 52, 1, 1, 1)

        self.menu_pushButton_54 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_54.setObjectName(u"menu_pushButton_54")

        self.menu_grid.addWidget(self.menu_pushButton_54, 53, 3, 1, 1)

        self.menu_label_108 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_108.setObjectName(u"menu_label_108")

        self.menu_grid.addWidget(self.menu_label_108, 53, 1, 1, 1)

        self.menu_label_100 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_100.setObjectName(u"menu_label_100")

        self.menu_grid.addWidget(self.menu_label_100, 49, 1, 1, 1)

        self.menu_comboBox_34 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_34.setObjectName(u"menu_comboBox_34")

        self.menu_grid.addWidget(self.menu_comboBox_34, 33, 2, 1, 1)

        self.menu_pushButton_57 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_57.setObjectName(u"menu_pushButton_57")

        self.menu_grid.addWidget(self.menu_pushButton_57, 56, 3, 1, 1)

        self.menu_comboBox_85 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_85.setObjectName(u"menu_comboBox_85")

        self.menu_grid.addWidget(self.menu_comboBox_85, 84, 2, 1, 1)

        self.menu_label_98 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_98.setObjectName(u"menu_label_98")

        self.menu_grid.addWidget(self.menu_label_98, 48, 1, 1, 1)

        self.menu_pushButton_74 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_74.setObjectName(u"menu_pushButton_74")

        self.menu_grid.addWidget(self.menu_pushButton_74, 73, 3, 1, 1)

        self.menu_pushButton_103 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_103.setObjectName(u"menu_pushButton_103")

        self.menu_grid.addWidget(self.menu_pushButton_103, 102, 3, 1, 1)

        self.menu_label_7 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_7.setObjectName(u"menu_label_7")

        self.menu_grid.addWidget(self.menu_label_7, 3, 0, 1, 1)

        self.menu_comboBox_153 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_153.setObjectName(u"menu_comboBox_153")

        self.menu_grid.addWidget(self.menu_comboBox_153, 152, 2, 1, 1)

        self.menu_label_77 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_77.setObjectName(u"menu_label_77")

        self.menu_grid.addWidget(self.menu_label_77, 38, 0, 1, 1)

        self.menu_label_84 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_84.setObjectName(u"menu_label_84")

        self.menu_grid.addWidget(self.menu_label_84, 41, 1, 1, 1)

        self.menu_label_104 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_104.setObjectName(u"menu_label_104")

        self.menu_grid.addWidget(self.menu_label_104, 51, 1, 1, 1)

        self.menu_pushButton_151 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_151.setObjectName(u"menu_pushButton_151")

        self.menu_grid.addWidget(self.menu_pushButton_151, 150, 3, 1, 1)

        self.menu_pushButton_63 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_63.setObjectName(u"menu_pushButton_63")

        self.menu_grid.addWidget(self.menu_pushButton_63, 62, 3, 1, 1)

        self.menu_label_92 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_92.setObjectName(u"menu_label_92")

        self.menu_grid.addWidget(self.menu_label_92, 45, 1, 1, 1)

        self.menu_comboBox_7 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_7.setObjectName(u"menu_comboBox_7")

        self.menu_grid.addWidget(self.menu_comboBox_7, 6, 2, 1, 1)

        self.menu_label_165 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_165.setObjectName(u"menu_label_165")

        self.menu_grid.addWidget(self.menu_label_165, 82, 0, 1, 1)

        self.menu_pushButton_146 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_146.setObjectName(u"menu_pushButton_146")

        self.menu_grid.addWidget(self.menu_pushButton_146, 145, 3, 1, 1)

        self.menu_comboBox_76 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_76.setObjectName(u"menu_comboBox_76")

        self.menu_grid.addWidget(self.menu_comboBox_76, 75, 2, 1, 1)

        self.menu_comboBox_114 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_114.setObjectName(u"menu_comboBox_114")

        self.menu_grid.addWidget(self.menu_comboBox_114, 113, 2, 1, 1)

        self.menu_pushButton_152 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_152.setObjectName(u"menu_pushButton_152")

        self.menu_grid.addWidget(self.menu_pushButton_152, 151, 3, 1, 1)

        self.menu_pushButton_107 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_107.setObjectName(u"menu_pushButton_107")

        self.menu_grid.addWidget(self.menu_pushButton_107, 106, 3, 1, 1)

        self.menu_pushButton_136 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_136.setObjectName(u"menu_pushButton_136")

        self.menu_grid.addWidget(self.menu_pushButton_136, 135, 3, 1, 1)

        self.menu_comboBox_84 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_84.setObjectName(u"menu_comboBox_84")

        self.menu_grid.addWidget(self.menu_comboBox_84, 83, 2, 1, 1)

        self.menu_comboBox_77 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_77.setObjectName(u"menu_comboBox_77")

        self.menu_grid.addWidget(self.menu_comboBox_77, 76, 2, 1, 1)

        self.menu_pushButton_78 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_78.setObjectName(u"menu_pushButton_78")

        self.menu_grid.addWidget(self.menu_pushButton_78, 77, 3, 1, 1)

        self.menu_label_24 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_24.setObjectName(u"menu_label_24")

        self.menu_grid.addWidget(self.menu_label_24, 11, 1, 1, 1)

        self.menu_comboBox_128 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_128.setObjectName(u"menu_comboBox_128")

        self.menu_grid.addWidget(self.menu_comboBox_128, 127, 2, 1, 1)

        self.menu_pushButton_46 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_46.setObjectName(u"menu_pushButton_46")

        self.menu_grid.addWidget(self.menu_pushButton_46, 45, 3, 1, 1)

        self.menu_label_74 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_74.setObjectName(u"menu_label_74")

        self.menu_grid.addWidget(self.menu_label_74, 36, 1, 1, 1)

        self.menu_label_76 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_76.setObjectName(u"menu_label_76")

        self.menu_grid.addWidget(self.menu_label_76, 37, 1, 1, 1)

        self.menu_comboBox_110 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_110.setObjectName(u"menu_comboBox_110")

        self.menu_grid.addWidget(self.menu_comboBox_110, 109, 2, 1, 1)

        self.menu_label_1 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_1.setObjectName(u"menu_label_1")
        self.menu_label_1.setMaximumSize(QSize(16777215, 16777215))

        self.menu_grid.addWidget(self.menu_label_1, 0, 0, 1, 1)

        self.menu_label_157 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_157.setObjectName(u"menu_label_157")

        self.menu_grid.addWidget(self.menu_label_157, 78, 0, 1, 1)

        self.menu_comboBox_23 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_23.setObjectName(u"menu_comboBox_23")

        self.menu_grid.addWidget(self.menu_comboBox_23, 22, 2, 1, 1)

        self.menu_comboBox_99 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_99.setObjectName(u"menu_comboBox_99")

        self.menu_grid.addWidget(self.menu_comboBox_99, 98, 2, 1, 1)

        self.menu_label_37 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_37.setObjectName(u"menu_label_37")

        self.menu_grid.addWidget(self.menu_label_37, 18, 0, 1, 1)

        self.menu_pushButton_21 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_21.setObjectName(u"menu_pushButton_21")

        self.menu_grid.addWidget(self.menu_pushButton_21, 20, 3, 1, 1)

        self.menu_label_119 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_119.setObjectName(u"menu_label_119")

        self.menu_grid.addWidget(self.menu_label_119, 59, 0, 1, 1)

        self.menu_comboBox_94 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_94.setObjectName(u"menu_comboBox_94")

        self.menu_grid.addWidget(self.menu_comboBox_94, 93, 2, 1, 1)

        self.menu_label_68 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_68.setObjectName(u"menu_label_68")

        self.menu_grid.addWidget(self.menu_label_68, 33, 1, 1, 1)

        self.menu_comboBox_37 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_37.setObjectName(u"menu_comboBox_37")

        self.menu_grid.addWidget(self.menu_comboBox_37, 36, 2, 1, 1)

        self.menu_label_118 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_118.setObjectName(u"menu_label_118")

        self.menu_grid.addWidget(self.menu_label_118, 58, 1, 1, 1)

        self.menu_label_159 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_159.setObjectName(u"menu_label_159")

        self.menu_grid.addWidget(self.menu_label_159, 79, 0, 1, 1)

        self.menu_label_122 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_122.setObjectName(u"menu_label_122")

        self.menu_grid.addWidget(self.menu_label_122, 60, 1, 1, 1)

        self.menu_label_172 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_172.setObjectName(u"menu_label_172")

        self.menu_grid.addWidget(self.menu_label_172, 85, 1, 1, 1)

        self.menu_comboBox_116 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_116.setObjectName(u"menu_comboBox_116")

        self.menu_grid.addWidget(self.menu_comboBox_116, 115, 2, 1, 1)

        self.menu_pushButton_102 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_102.setObjectName(u"menu_pushButton_102")

        self.menu_grid.addWidget(self.menu_pushButton_102, 101, 3, 1, 1)

        self.menu_pushButton_116 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_116.setObjectName(u"menu_pushButton_116")

        self.menu_grid.addWidget(self.menu_pushButton_116, 115, 3, 1, 1)

        self.menu_comboBox_43 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_43.setObjectName(u"menu_comboBox_43")

        self.menu_grid.addWidget(self.menu_comboBox_43, 42, 2, 1, 1)

        self.menu_comboBox_111 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_111.setObjectName(u"menu_comboBox_111")

        self.menu_grid.addWidget(self.menu_comboBox_111, 110, 2, 1, 1)

        self.menu_pushButton_139 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_139.setObjectName(u"menu_pushButton_139")

        self.menu_grid.addWidget(self.menu_pushButton_139, 138, 3, 1, 1)

        self.menu_comboBox_51 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_51.setObjectName(u"menu_comboBox_51")

        self.menu_grid.addWidget(self.menu_comboBox_51, 50, 2, 1, 1)

        self.menu_label_152 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_152.setObjectName(u"menu_label_152")

        self.menu_grid.addWidget(self.menu_label_152, 75, 1, 1, 1)

        self.menu_label_136 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_136.setObjectName(u"menu_label_136")

        self.menu_grid.addWidget(self.menu_label_136, 67, 1, 1, 1)

        self.menu_label_134 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_134.setObjectName(u"menu_label_134")

        self.menu_grid.addWidget(self.menu_label_134, 66, 1, 1, 1)

        self.menu_comboBox_131 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_131.setObjectName(u"menu_comboBox_131")

        self.menu_grid.addWidget(self.menu_comboBox_131, 130, 2, 1, 1)

        self.menu_pushButton_115 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_115.setObjectName(u"menu_pushButton_115")

        self.menu_grid.addWidget(self.menu_pushButton_115, 114, 3, 1, 1)

        self.menu_label_72 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_72.setObjectName(u"menu_label_72")

        self.menu_grid.addWidget(self.menu_label_72, 35, 1, 1, 1)

        self.menu_pushButton_86 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_86.setObjectName(u"menu_pushButton_86")

        self.menu_grid.addWidget(self.menu_pushButton_86, 85, 3, 1, 1)

        self.menu_label_151 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_151.setObjectName(u"menu_label_151")

        self.menu_grid.addWidget(self.menu_label_151, 75, 0, 1, 1)

        self.menu_label_6 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_6.setObjectName(u"menu_label_6")

        self.menu_grid.addWidget(self.menu_label_6, 2, 1, 1, 1)

        self.menu_pushButton_98 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_98.setObjectName(u"menu_pushButton_98")

        self.menu_grid.addWidget(self.menu_pushButton_98, 97, 3, 1, 1)

        self.menu_label_16 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_16.setObjectName(u"menu_label_16")

        self.menu_grid.addWidget(self.menu_label_16, 7, 1, 1, 1)

        self.menu_pushButton_70 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_70.setObjectName(u"menu_pushButton_70")

        self.menu_grid.addWidget(self.menu_pushButton_70, 69, 3, 1, 1)

        self.menu_comboBox_98 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_98.setObjectName(u"menu_comboBox_98")

        self.menu_grid.addWidget(self.menu_comboBox_98, 97, 2, 1, 1)

        self.menu_label_129 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_129.setObjectName(u"menu_label_129")

        self.menu_grid.addWidget(self.menu_label_129, 64, 0, 1, 1)

        self.menu_label_164 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_164.setObjectName(u"menu_label_164")

        self.menu_grid.addWidget(self.menu_label_164, 81, 1, 1, 1)

        self.menu_pushButton_121 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_121.setObjectName(u"menu_pushButton_121")

        self.menu_grid.addWidget(self.menu_pushButton_121, 120, 3, 1, 1)

        self.menu_pushButton_132 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_132.setObjectName(u"menu_pushButton_132")

        self.menu_grid.addWidget(self.menu_pushButton_132, 131, 3, 1, 1)

        self.menu_comboBox_135 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_135.setObjectName(u"menu_comboBox_135")

        self.menu_grid.addWidget(self.menu_comboBox_135, 134, 2, 1, 1)

        self.menu_comboBox_10 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_10.setObjectName(u"menu_comboBox_10")

        self.menu_grid.addWidget(self.menu_comboBox_10, 9, 2, 1, 1)

        self.menu_label_171 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_171.setObjectName(u"menu_label_171")

        self.menu_grid.addWidget(self.menu_label_171, 85, 0, 1, 1)

        self.menu_label_138 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_138.setObjectName(u"menu_label_138")

        self.menu_grid.addWidget(self.menu_label_138, 68, 1, 1, 1)

        self.menu_pushButton_18 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_18.setObjectName(u"menu_pushButton_18")

        self.menu_grid.addWidget(self.menu_pushButton_18, 17, 3, 1, 1)

        self.menu_comboBox_146 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_146.setObjectName(u"menu_comboBox_146")

        self.menu_grid.addWidget(self.menu_comboBox_146, 145, 2, 1, 1)

        self.menu_label_184 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_184.setObjectName(u"menu_label_184")

        self.menu_grid.addWidget(self.menu_label_184, 91, 1, 1, 1)

        self.menu_label_41 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_41.setObjectName(u"menu_label_41")

        self.menu_grid.addWidget(self.menu_label_41, 20, 0, 1, 1)

        self.menu_label_168 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_168.setObjectName(u"menu_label_168")

        self.menu_grid.addWidget(self.menu_label_168, 83, 1, 1, 1)

        self.menu_pushButton_72 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_72.setObjectName(u"menu_pushButton_72")

        self.menu_grid.addWidget(self.menu_pushButton_72, 71, 3, 1, 1)

        self.menu_label_110 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_110.setObjectName(u"menu_label_110")

        self.menu_grid.addWidget(self.menu_label_110, 54, 1, 1, 1)

        self.menu_pushButton_60 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_60.setObjectName(u"menu_pushButton_60")

        self.menu_grid.addWidget(self.menu_pushButton_60, 59, 3, 1, 1)

        self.menu_comboBox_66 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_66.setObjectName(u"menu_comboBox_66")

        self.menu_grid.addWidget(self.menu_comboBox_66, 65, 2, 1, 1)

        self.menu_pushButton_11 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_11.setObjectName(u"menu_pushButton_11")

        self.menu_grid.addWidget(self.menu_pushButton_11, 10, 3, 1, 1)

        self.menu_pushButton_145 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_145.setObjectName(u"menu_pushButton_145")

        self.menu_grid.addWidget(self.menu_pushButton_145, 144, 3, 1, 1)

        self.menu_pushButton_55 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_55.setObjectName(u"menu_pushButton_55")

        self.menu_grid.addWidget(self.menu_pushButton_55, 54, 3, 1, 1)

        self.menu_pushButton_96 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_96.setObjectName(u"menu_pushButton_96")

        self.menu_grid.addWidget(self.menu_pushButton_96, 95, 3, 1, 1)

        self.menu_comboBox_44 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_44.setObjectName(u"menu_comboBox_44")

        self.menu_grid.addWidget(self.menu_comboBox_44, 43, 2, 1, 1)

        self.menu_comboBox_83 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_83.setObjectName(u"menu_comboBox_83")

        self.menu_grid.addWidget(self.menu_comboBox_83, 82, 2, 1, 1)

        self.menu_pushButton_125 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_125.setObjectName(u"menu_pushButton_125")

        self.menu_grid.addWidget(self.menu_pushButton_125, 124, 3, 1, 1)

        self.menu_label_3 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_3.setObjectName(u"menu_label_3")

        self.menu_grid.addWidget(self.menu_label_3, 1, 0, 1, 1)

        self.menu_comboBox_71 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_71.setObjectName(u"menu_comboBox_71")

        self.menu_grid.addWidget(self.menu_comboBox_71, 70, 2, 1, 1)

        self.menu_comboBox_107 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_107.setObjectName(u"menu_comboBox_107")

        self.menu_grid.addWidget(self.menu_comboBox_107, 106, 2, 1, 1)

        self.menu_label_95 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_95.setObjectName(u"menu_label_95")

        self.menu_grid.addWidget(self.menu_label_95, 47, 0, 1, 1)

        self.menu_pushButton_30 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_30.setObjectName(u"menu_pushButton_30")

        self.menu_grid.addWidget(self.menu_pushButton_30, 29, 3, 1, 1)

        self.menu_comboBox_53 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_53.setObjectName(u"menu_comboBox_53")

        self.menu_grid.addWidget(self.menu_comboBox_53, 52, 2, 1, 1)

        self.menu_pushButton_92 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_92.setObjectName(u"menu_pushButton_92")

        self.menu_grid.addWidget(self.menu_pushButton_92, 91, 3, 1, 1)

        self.menu_comboBox_122 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_122.setObjectName(u"menu_comboBox_122")

        self.menu_grid.addWidget(self.menu_comboBox_122, 121, 2, 1, 1)

        self.menu_comboBox_132 = QComboBox(self.menu_scroll_area_contents)
        self.menu_comboBox_132.setObjectName(u"menu_comboBox_132")

        self.menu_grid.addWidget(self.menu_comboBox_132, 131, 2, 1, 1)

        self.menu_pushButton_17 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_17.setObjectName(u"menu_pushButton_17")

        self.menu_grid.addWidget(self.menu_pushButton_17, 16, 3, 1, 1)

        self.menu_label_86 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_86.setObjectName(u"menu_label_86")

        self.menu_grid.addWidget(self.menu_label_86, 42, 1, 1, 1)

        self.menu_pushButton_9 = QPushButton(self.menu_scroll_area_contents)
        self.menu_pushButton_9.setObjectName(u"menu_pushButton_9")

        self.menu_grid.addWidget(self.menu_pushButton_9, 8, 3, 1, 1)

        self.menu_label_186 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_186.setObjectName(u"menu_label_186")

        self.menu_grid.addWidget(self.menu_label_186, 92, 1, 1, 1)

        self.menu_label_187 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_187.setObjectName(u"menu_label_187")

        self.menu_grid.addWidget(self.menu_label_187, 93, 0, 1, 1)

        self.menu_label_188 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_188.setObjectName(u"menu_label_188")

        self.menu_grid.addWidget(self.menu_label_188, 93, 1, 1, 1)

        self.menu_label_189 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_189.setObjectName(u"menu_label_189")

        self.menu_grid.addWidget(self.menu_label_189, 94, 0, 1, 1)

        self.menu_label_190 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_190.setObjectName(u"menu_label_190")

        self.menu_grid.addWidget(self.menu_label_190, 94, 1, 1, 1)

        self.menu_label_191 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_191.setObjectName(u"menu_label_191")

        self.menu_grid.addWidget(self.menu_label_191, 95, 0, 1, 1)

        self.menu_label_192 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_192.setObjectName(u"menu_label_192")

        self.menu_grid.addWidget(self.menu_label_192, 95, 1, 1, 1)

        self.menu_label_193 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_193.setObjectName(u"menu_label_193")

        self.menu_grid.addWidget(self.menu_label_193, 96, 0, 1, 1)

        self.menu_label_194 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_194.setObjectName(u"menu_label_194")

        self.menu_grid.addWidget(self.menu_label_194, 96, 1, 1, 1)

        self.menu_label_195 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_195.setObjectName(u"menu_label_195")

        self.menu_grid.addWidget(self.menu_label_195, 97, 0, 1, 1)

        self.menu_label_196 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_196.setObjectName(u"menu_label_196")

        self.menu_grid.addWidget(self.menu_label_196, 97, 1, 1, 1)

        self.menu_label_197 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_197.setObjectName(u"menu_label_197")

        self.menu_grid.addWidget(self.menu_label_197, 98, 0, 1, 1)

        self.menu_label_198 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_198.setObjectName(u"menu_label_198")

        self.menu_grid.addWidget(self.menu_label_198, 98, 1, 1, 1)

        self.menu_label_199 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_199.setObjectName(u"menu_label_199")

        self.menu_grid.addWidget(self.menu_label_199, 99, 0, 1, 1)

        self.menu_label_200 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_200.setObjectName(u"menu_label_200")

        self.menu_grid.addWidget(self.menu_label_200, 99, 1, 1, 1)

        self.menu_label_201 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_201.setObjectName(u"menu_label_201")

        self.menu_grid.addWidget(self.menu_label_201, 100, 0, 1, 1)

        self.menu_label_202 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_202.setObjectName(u"menu_label_202")

        self.menu_grid.addWidget(self.menu_label_202, 100, 1, 1, 1)

        self.menu_label_203 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_203.setObjectName(u"menu_label_203")

        self.menu_grid.addWidget(self.menu_label_203, 101, 0, 1, 1)

        self.menu_label_204 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_204.setObjectName(u"menu_label_204")

        self.menu_grid.addWidget(self.menu_label_204, 101, 1, 1, 1)

        self.menu_label_205 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_205.setObjectName(u"menu_label_205")

        self.menu_grid.addWidget(self.menu_label_205, 102, 0, 1, 1)

        self.menu_label_206 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_206.setObjectName(u"menu_label_206")

        self.menu_grid.addWidget(self.menu_label_206, 102, 1, 1, 1)

        self.menu_label_207 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_207.setObjectName(u"menu_label_207")

        self.menu_grid.addWidget(self.menu_label_207, 103, 0, 1, 1)

        self.menu_label_208 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_208.setObjectName(u"menu_label_208")

        self.menu_grid.addWidget(self.menu_label_208, 103, 1, 1, 1)

        self.menu_label_209 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_209.setObjectName(u"menu_label_209")

        self.menu_grid.addWidget(self.menu_label_209, 104, 0, 1, 1)

        self.menu_label_210 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_210.setObjectName(u"menu_label_210")

        self.menu_grid.addWidget(self.menu_label_210, 104, 1, 1, 1)

        self.menu_label_211 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_211.setObjectName(u"menu_label_211")

        self.menu_grid.addWidget(self.menu_label_211, 105, 0, 1, 1)

        self.menu_label_212 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_212.setObjectName(u"menu_label_212")

        self.menu_grid.addWidget(self.menu_label_212, 105, 1, 1, 1)

        self.menu_label_213 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_213.setObjectName(u"menu_label_213")

        self.menu_grid.addWidget(self.menu_label_213, 106, 0, 1, 1)

        self.menu_label_214 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_214.setObjectName(u"menu_label_214")

        self.menu_grid.addWidget(self.menu_label_214, 106, 1, 1, 1)

        self.menu_label_215 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_215.setObjectName(u"menu_label_215")

        self.menu_grid.addWidget(self.menu_label_215, 107, 0, 1, 1)

        self.menu_label_216 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_216.setObjectName(u"menu_label_216")

        self.menu_grid.addWidget(self.menu_label_216, 107, 1, 1, 1)

        self.menu_label_217 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_217.setObjectName(u"menu_label_217")

        self.menu_grid.addWidget(self.menu_label_217, 108, 0, 1, 1)

        self.menu_label_218 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_218.setObjectName(u"menu_label_218")

        self.menu_grid.addWidget(self.menu_label_218, 108, 1, 1, 1)

        self.menu_label_219 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_219.setObjectName(u"menu_label_219")

        self.menu_grid.addWidget(self.menu_label_219, 109, 0, 1, 1)

        self.menu_label_220 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_220.setObjectName(u"menu_label_220")

        self.menu_grid.addWidget(self.menu_label_220, 109, 1, 1, 1)

        self.menu_label_221 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_221.setObjectName(u"menu_label_221")

        self.menu_grid.addWidget(self.menu_label_221, 110, 0, 1, 1)

        self.menu_label_222 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_222.setObjectName(u"menu_label_222")

        self.menu_grid.addWidget(self.menu_label_222, 110, 1, 1, 1)

        self.menu_label_223 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_223.setObjectName(u"menu_label_223")

        self.menu_grid.addWidget(self.menu_label_223, 111, 0, 1, 1)

        self.menu_label_224 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_224.setObjectName(u"menu_label_224")

        self.menu_grid.addWidget(self.menu_label_224, 111, 1, 1, 1)

        self.menu_label_225 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_225.setObjectName(u"menu_label_225")

        self.menu_grid.addWidget(self.menu_label_225, 112, 0, 1, 1)

        self.menu_label_226 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_226.setObjectName(u"menu_label_226")

        self.menu_grid.addWidget(self.menu_label_226, 112, 1, 1, 1)

        self.menu_label_227 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_227.setObjectName(u"menu_label_227")

        self.menu_grid.addWidget(self.menu_label_227, 113, 0, 1, 1)

        self.menu_label_228 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_228.setObjectName(u"menu_label_228")

        self.menu_grid.addWidget(self.menu_label_228, 113, 1, 1, 1)

        self.menu_label_229 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_229.setObjectName(u"menu_label_229")

        self.menu_grid.addWidget(self.menu_label_229, 114, 0, 1, 1)

        self.menu_label_230 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_230.setObjectName(u"menu_label_230")

        self.menu_grid.addWidget(self.menu_label_230, 114, 1, 1, 1)

        self.menu_label_231 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_231.setObjectName(u"menu_label_231")

        self.menu_grid.addWidget(self.menu_label_231, 115, 0, 1, 1)

        self.menu_label_232 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_232.setObjectName(u"menu_label_232")

        self.menu_grid.addWidget(self.menu_label_232, 115, 1, 1, 1)

        self.menu_label_233 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_233.setObjectName(u"menu_label_233")

        self.menu_grid.addWidget(self.menu_label_233, 116, 0, 1, 1)

        self.menu_label_234 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_234.setObjectName(u"menu_label_234")

        self.menu_grid.addWidget(self.menu_label_234, 116, 1, 1, 1)

        self.menu_label_235 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_235.setObjectName(u"menu_label_235")

        self.menu_grid.addWidget(self.menu_label_235, 117, 0, 1, 1)

        self.menu_label_236 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_236.setObjectName(u"menu_label_236")

        self.menu_grid.addWidget(self.menu_label_236, 117, 1, 1, 1)

        self.menu_label_237 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_237.setObjectName(u"menu_label_237")

        self.menu_grid.addWidget(self.menu_label_237, 118, 0, 1, 1)

        self.menu_label_238 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_238.setObjectName(u"menu_label_238")

        self.menu_grid.addWidget(self.menu_label_238, 118, 1, 1, 1)

        self.menu_label_239 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_239.setObjectName(u"menu_label_239")

        self.menu_grid.addWidget(self.menu_label_239, 119, 0, 1, 1)

        self.menu_label_240 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_240.setObjectName(u"menu_label_240")

        self.menu_grid.addWidget(self.menu_label_240, 119, 1, 1, 1)

        self.menu_label_241 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_241.setObjectName(u"menu_label_241")

        self.menu_grid.addWidget(self.menu_label_241, 120, 0, 1, 1)

        self.menu_label_242 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_242.setObjectName(u"menu_label_242")

        self.menu_grid.addWidget(self.menu_label_242, 120, 1, 1, 1)

        self.menu_label_243 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_243.setObjectName(u"menu_label_243")

        self.menu_grid.addWidget(self.menu_label_243, 121, 0, 1, 1)

        self.menu_label_244 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_244.setObjectName(u"menu_label_244")

        self.menu_grid.addWidget(self.menu_label_244, 121, 1, 1, 1)

        self.menu_label_245 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_245.setObjectName(u"menu_label_245")

        self.menu_grid.addWidget(self.menu_label_245, 122, 0, 1, 1)

        self.menu_label_246 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_246.setObjectName(u"menu_label_246")

        self.menu_grid.addWidget(self.menu_label_246, 122, 1, 1, 1)

        self.menu_label_247 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_247.setObjectName(u"menu_label_247")

        self.menu_grid.addWidget(self.menu_label_247, 123, 0, 1, 1)

        self.menu_label_248 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_248.setObjectName(u"menu_label_248")

        self.menu_grid.addWidget(self.menu_label_248, 123, 1, 1, 1)

        self.menu_label_249 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_249.setObjectName(u"menu_label_249")

        self.menu_grid.addWidget(self.menu_label_249, 124, 0, 1, 1)

        self.menu_label_250 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_250.setObjectName(u"menu_label_250")

        self.menu_grid.addWidget(self.menu_label_250, 124, 1, 1, 1)

        self.menu_label_251 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_251.setObjectName(u"menu_label_251")

        self.menu_grid.addWidget(self.menu_label_251, 125, 0, 1, 1)

        self.menu_label_252 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_252.setObjectName(u"menu_label_252")

        self.menu_grid.addWidget(self.menu_label_252, 125, 1, 1, 1)

        self.menu_label_253 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_253.setObjectName(u"menu_label_253")

        self.menu_grid.addWidget(self.menu_label_253, 126, 0, 1, 1)

        self.menu_label_254 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_254.setObjectName(u"menu_label_254")

        self.menu_grid.addWidget(self.menu_label_254, 126, 1, 1, 1)

        self.menu_label_255 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_255.setObjectName(u"menu_label_255")

        self.menu_grid.addWidget(self.menu_label_255, 127, 0, 1, 1)

        self.menu_label_256 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_256.setObjectName(u"menu_label_256")

        self.menu_grid.addWidget(self.menu_label_256, 127, 1, 1, 1)

        self.menu_label_257 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_257.setObjectName(u"menu_label_257")

        self.menu_grid.addWidget(self.menu_label_257, 128, 0, 1, 1)

        self.menu_label_258 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_258.setObjectName(u"menu_label_258")

        self.menu_grid.addWidget(self.menu_label_258, 128, 1, 1, 1)

        self.menu_label_259 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_259.setObjectName(u"menu_label_259")

        self.menu_grid.addWidget(self.menu_label_259, 129, 0, 1, 1)

        self.menu_label_260 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_260.setObjectName(u"menu_label_260")

        self.menu_grid.addWidget(self.menu_label_260, 129, 1, 1, 1)

        self.menu_label_261 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_261.setObjectName(u"menu_label_261")

        self.menu_grid.addWidget(self.menu_label_261, 130, 0, 1, 1)

        self.menu_label_262 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_262.setObjectName(u"menu_label_262")

        self.menu_grid.addWidget(self.menu_label_262, 130, 1, 1, 1)

        self.menu_label_263 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_263.setObjectName(u"menu_label_263")

        self.menu_grid.addWidget(self.menu_label_263, 131, 0, 1, 1)

        self.menu_label_264 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_264.setObjectName(u"menu_label_264")

        self.menu_grid.addWidget(self.menu_label_264, 131, 1, 1, 1)

        self.menu_label_265 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_265.setObjectName(u"menu_label_265")

        self.menu_grid.addWidget(self.menu_label_265, 132, 0, 1, 1)

        self.menu_label_266 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_266.setObjectName(u"menu_label_266")

        self.menu_grid.addWidget(self.menu_label_266, 132, 1, 1, 1)

        self.menu_label_267 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_267.setObjectName(u"menu_label_267")

        self.menu_grid.addWidget(self.menu_label_267, 133, 0, 1, 1)

        self.menu_label_268 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_268.setObjectName(u"menu_label_268")

        self.menu_grid.addWidget(self.menu_label_268, 133, 1, 1, 1)

        self.menu_label_269 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_269.setObjectName(u"menu_label_269")

        self.menu_grid.addWidget(self.menu_label_269, 134, 0, 1, 1)

        self.menu_label_270 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_270.setObjectName(u"menu_label_270")

        self.menu_grid.addWidget(self.menu_label_270, 134, 1, 1, 1)

        self.menu_label_271 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_271.setObjectName(u"menu_label_271")

        self.menu_grid.addWidget(self.menu_label_271, 135, 0, 1, 1)

        self.menu_label_272 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_272.setObjectName(u"menu_label_272")

        self.menu_grid.addWidget(self.menu_label_272, 135, 1, 1, 1)

        self.menu_label_273 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_273.setObjectName(u"menu_label_273")

        self.menu_grid.addWidget(self.menu_label_273, 136, 0, 1, 1)

        self.menu_label_274 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_274.setObjectName(u"menu_label_274")

        self.menu_grid.addWidget(self.menu_label_274, 136, 1, 1, 1)

        self.menu_label_275 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_275.setObjectName(u"menu_label_275")

        self.menu_grid.addWidget(self.menu_label_275, 137, 0, 1, 1)

        self.menu_label_276 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_276.setObjectName(u"menu_label_276")

        self.menu_grid.addWidget(self.menu_label_276, 137, 1, 1, 1)

        self.menu_label_277 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_277.setObjectName(u"menu_label_277")

        self.menu_grid.addWidget(self.menu_label_277, 138, 0, 1, 1)

        self.menu_label_278 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_278.setObjectName(u"menu_label_278")

        self.menu_grid.addWidget(self.menu_label_278, 138, 1, 1, 1)

        self.menu_label_279 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_279.setObjectName(u"menu_label_279")

        self.menu_grid.addWidget(self.menu_label_279, 139, 0, 1, 1)

        self.menu_label_280 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_280.setObjectName(u"menu_label_280")

        self.menu_grid.addWidget(self.menu_label_280, 139, 1, 1, 1)

        self.menu_label_281 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_281.setObjectName(u"menu_label_281")

        self.menu_grid.addWidget(self.menu_label_281, 140, 0, 1, 1)

        self.menu_label_282 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_282.setObjectName(u"menu_label_282")

        self.menu_grid.addWidget(self.menu_label_282, 140, 1, 1, 1)

        self.menu_label_283 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_283.setObjectName(u"menu_label_283")

        self.menu_grid.addWidget(self.menu_label_283, 141, 0, 1, 1)

        self.menu_label_284 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_284.setObjectName(u"menu_label_284")

        self.menu_grid.addWidget(self.menu_label_284, 141, 1, 1, 1)

        self.menu_label_285 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_285.setObjectName(u"menu_label_285")

        self.menu_grid.addWidget(self.menu_label_285, 142, 0, 1, 1)

        self.menu_label_286 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_286.setObjectName(u"menu_label_286")

        self.menu_grid.addWidget(self.menu_label_286, 142, 1, 1, 1)

        self.menu_label_287 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_287.setObjectName(u"menu_label_287")

        self.menu_grid.addWidget(self.menu_label_287, 143, 0, 1, 1)

        self.menu_label_288 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_288.setObjectName(u"menu_label_288")

        self.menu_grid.addWidget(self.menu_label_288, 143, 1, 1, 1)

        self.menu_label_289 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_289.setObjectName(u"menu_label_289")

        self.menu_grid.addWidget(self.menu_label_289, 144, 0, 1, 1)

        self.menu_label_290 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_290.setObjectName(u"menu_label_290")

        self.menu_grid.addWidget(self.menu_label_290, 144, 1, 1, 1)

        self.menu_label_291 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_291.setObjectName(u"menu_label_291")

        self.menu_grid.addWidget(self.menu_label_291, 145, 0, 1, 1)

        self.menu_label_292 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_292.setObjectName(u"menu_label_292")

        self.menu_grid.addWidget(self.menu_label_292, 145, 1, 1, 1)

        self.menu_label_293 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_293.setObjectName(u"menu_label_293")

        self.menu_grid.addWidget(self.menu_label_293, 146, 0, 1, 1)

        self.menu_label_294 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_294.setObjectName(u"menu_label_294")

        self.menu_grid.addWidget(self.menu_label_294, 146, 1, 1, 1)

        self.menu_label_295 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_295.setObjectName(u"menu_label_295")

        self.menu_grid.addWidget(self.menu_label_295, 147, 0, 1, 1)

        self.menu_label_296 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_296.setObjectName(u"menu_label_296")

        self.menu_grid.addWidget(self.menu_label_296, 147, 1, 1, 1)

        self.menu_label_297 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_297.setObjectName(u"menu_label_297")

        self.menu_grid.addWidget(self.menu_label_297, 148, 0, 1, 1)

        self.menu_label_298 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_298.setObjectName(u"menu_label_298")

        self.menu_grid.addWidget(self.menu_label_298, 148, 1, 1, 1)

        self.menu_label_299 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_299.setObjectName(u"menu_label_299")

        self.menu_grid.addWidget(self.menu_label_299, 149, 0, 1, 1)

        self.menu_label_300 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_300.setObjectName(u"menu_label_300")

        self.menu_grid.addWidget(self.menu_label_300, 149, 1, 1, 1)

        self.menu_label_301 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_301.setObjectName(u"menu_label_301")

        self.menu_grid.addWidget(self.menu_label_301, 150, 0, 1, 1)

        self.menu_label_302 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_302.setObjectName(u"menu_label_302")

        self.menu_grid.addWidget(self.menu_label_302, 150, 1, 1, 1)

        self.menu_label_303 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_303.setObjectName(u"menu_label_303")

        self.menu_grid.addWidget(self.menu_label_303, 151, 0, 1, 1)

        self.menu_label_304 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_304.setObjectName(u"menu_label_304")

        self.menu_grid.addWidget(self.menu_label_304, 151, 1, 1, 1)

        self.menu_label_305 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_305.setObjectName(u"menu_label_305")

        self.menu_grid.addWidget(self.menu_label_305, 152, 0, 1, 1)

        self.menu_label_306 = QLabel(self.menu_scroll_area_contents)
        self.menu_label_306.setObjectName(u"menu_label_306")

        self.menu_grid.addWidget(self.menu_label_306, 152, 1, 1, 1)


        self.gridLayout.addLayout(self.menu_grid, 0, 0, 1, 1)

        self.menu_scroll_area.setWidget(self.menu_scroll_area_contents)
        self.Radio_tabWidget.addTab(self.tab_5, "")
        self.Message_textBrowser = QTextBrowser(self.centralwidget)
        self.Message_textBrowser.setObjectName(u"Message_textBrowser")
        self.Message_textBrowser.setGeometry(QRect(10, 950, 671, 161))
        self.Message_textBrowser.setFont(font4)
        self.Message_textBrowser.setStyleSheet(u"QTextBrowser { background-color: black; color: yellow;}")
        self.Message_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Message_textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.Message_textBrowser.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1220, 28))
        font15 = QFont()
        font15.setPointSize(14)
        font15.setBold(False)
        self.menubar.setFont(font15)
        self.menubar.setStyleSheet(u"")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font15)
        self.menuRefresh = QMenu(self.menubar)
        self.menuRefresh.setObjectName(u"menuRefresh")
        self.menuRefresh.setFont(font15)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setFont(font15)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font1)
        self.statusbar.setStyleSheet(u"QWidget{ background-color: lightgray;}\n"
"QStatusBar{ color: red;}")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRefresh.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_Radio_Menu)
        self.menuFile.addAction(self.actionLoad_Radio_Menu)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Memory_Channel)
        self.menuFile.addAction(self.actionLoad_Memory_Channel)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuRefresh.addAction(self.actionRefresh_Radio_Menu)
        self.menuRefresh.addAction(self.actionRefresh_Memory_Channel)
        self.menuRefresh.addAction(self.actionRefresh_Settings)
        self.menuRefresh.addAction(self.actionRefresh_Equalizer)
        self.menuRefresh.addAction(self.actionRefresh_Audio_Filter)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.Audio_filter_horizontalSlider_1.valueChanged.connect(self.Audio_filter_freq_label_1.setNum)
        self.Audio_filter_horizontalSlider_2.valueChanged.connect(self.Audio_filter_freq_label_2.setNum)
        self.EQ_1_center_verticalSlider.valueChanged.connect(self.EQ_1_center_label.setNum)
        self.EQ_2_center_verticalSlider.valueChanged.connect(self.EQ_2_center_label.setNum)
        self.EQ_3_center_verticalSlider.valueChanged.connect(self.EQ_3_center_label.setNum)
        self.EQ_1_gain_verticalSlider.valueChanged.connect(self.EQ_1_gain_label.setNum)
        self.EQ_1_BW_verticalSlider.valueChanged.connect(self.EQ_1_BW_label.setNum)
        self.EQ_2_gain_verticalSlider.valueChanged.connect(self.EQ_2_gain_label.setNum)
        self.EQ_2_BW_verticalSlider.valueChanged.connect(self.EQ_2_BW_label.setNum)
        self.EQ_3_gain_verticalSlider.valueChanged.connect(self.EQ_3_gain_label.setNum)
        self.EQ_3_BW_verticalSlider.valueChanged.connect(self.EQ_3_BW_label.setNum)

        self.Radio_tabWidget.setCurrentIndex(0)
        self.FFT_window_comboBox.setCurrentIndex(2)
        self.FFT_gain_comboBox.setCurrentIndex(2)
        self.FFT_block_comboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_Radio_Menu.setText(QCoreApplication.translate("MainWindow", u"Save Radio Menu...", None))
        self.actionLoad_Radio_Menu.setText(QCoreApplication.translate("MainWindow", u"Load Radio Menu...", None))
        self.actionSave_Memory_Channel.setText(QCoreApplication.translate("MainWindow", u"Save Memory Channel...", None))
        self.actionLoad_Memory_Channel.setText(QCoreApplication.translate("MainWindow", u"Load Memory Channel...", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionRefresh_Radio_Menu.setText(QCoreApplication.translate("MainWindow", u"Radio Menu", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh_Radio_Menu.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionRefresh_Memory_Channel.setText(QCoreApplication.translate("MainWindow", u"Memory Channel", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh_Memory_Channel.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionRefresh_Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh_Settings.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionRefresh_Equalizer.setText(QCoreApplication.translate("MainWindow", u"Equalizer", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh_Equalizer.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionRefresh_Audio_Filter.setText(QCoreApplication.translate("MainWindow", u"Audio Filter", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh_Audio_Filter.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.VFO_A_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"   VFO-A Register", None))
#if QT_CONFIG(whatsthis)
        self.VFO_A_dial.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.VFO_A_Tx_radioButton.setText(QCoreApplication.translate("MainWindow", u"Tx", None))
        self.VFO_A_Rx_radioButton.setText(QCoreApplication.translate("MainWindow", u"Rx", None))
        self.VFO_A_label_1.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.VFO_A_label_2.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.VFO_A_textBrowser.setMarkdown("")
        self.VFO_A_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Monospace'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.VFO_A_label_3.setText(QCoreApplication.translate("MainWindow", u"Keyboard Entry", None))
        self.VFO_A_label_4.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.VFO_A_fast_radioButton.setText(QCoreApplication.translate("MainWindow", u"FAST", None))
        self.VFO_B_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"   VFO-B Register", None))
        self.VFO_B_Tx_radioButton.setText(QCoreApplication.translate("MainWindow", u"Tx", None))
        self.VFO_B_Rx_radioButton.setText(QCoreApplication.translate("MainWindow", u"Rx", None))
        self.VFO_B_label_1.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.VFO_B_label_2.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.VFO_B_textBrowser.setMarkdown("")
        self.VFO_B_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Monospace'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.VFO_B_label_3.setText(QCoreApplication.translate("MainWindow", u"Keyboard Entry", None))
        self.VFO_B_label_4.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.VFO_B_fast_radioButton.setText(QCoreApplication.translate("MainWindow", u"FAST", None))
        self.Band_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Band", None))
        self.band_pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1.8", None))
        self.band_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"3.5", None))
        self.band_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.band_pushButton_4.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.band_pushButton_6.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.band_pushButton_5.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.band_pushButton_8.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.band_pushButton_7.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.band_pushButton_9.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.band_pushButton_10.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.band_pushButton_11.setText(QCoreApplication.translate("MainWindow", u"144", None))
        self.band_pushButton_12.setText(QCoreApplication.translate("MainWindow", u"430", None))
        self.band_pushButton_13.setText(QCoreApplication.translate("MainWindow", u"AIR", None))
        self.band_pushButton_14.setText(QCoreApplication.translate("MainWindow", u"GEN", None))
        self.band_pushButton_15.setText(QCoreApplication.translate("MainWindow", u"MW", None))
        self.PLL_lock_radioButton.setText(QCoreApplication.translate("MainWindow", u"PLL Lock", None))
        self.Mode_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Mode", None))
        self.mode_pushButton_1.setText(QCoreApplication.translate("MainWindow", u"LSB", None))
        self.mode_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"USB", None))
        self.mode_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"CW-LSB", None))
        self.mode_pushButton_4.setText(QCoreApplication.translate("MainWindow", u"CW-USB", None))
        self.mode_pushButton_5.setText(QCoreApplication.translate("MainWindow", u"RTTY-LSB", None))
        self.mode_pushButton_6.setText(QCoreApplication.translate("MainWindow", u"RTTY-USB", None))
        self.mode_pushButton_7.setText(QCoreApplication.translate("MainWindow", u"DATA-LSB", None))
        self.mode_pushButton_8.setText(QCoreApplication.translate("MainWindow", u"DATA-USB", None))
        self.mode_pushButton_9.setText(QCoreApplication.translate("MainWindow", u"AM", None))
        self.mode_pushButton_10.setText(QCoreApplication.translate("MainWindow", u"FM", None))
        self.mode_pushButton_11.setText(QCoreApplication.translate("MainWindow", u"C4FM", None))
        self.mode_pushButton_12.setText(QCoreApplication.translate("MainWindow", u"DATA-FM", None))
        self.RF_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  RF", None))
        self.RF_label_1.setText(QCoreApplication.translate("MainWindow", u"RF Power", None))
        self.RF_label_2.setText(QCoreApplication.translate("MainWindow", u"AF Gain", None))
        self.RF_label_3.setText(QCoreApplication.translate("MainWindow", u"RF Gain", None))
        self.RF_label_4.setText(QCoreApplication.translate("MainWindow", u"Squelch", None))
        self.Meter_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Meters", None))
        self.S_meter_progressBar.setFormat("")
        self.S_meter_label_1.setText("")
        self.S_meter_label_2.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.PO_meter_progressBar.setFormat("")
        self.PO_meter_label_2.setText(QCoreApplication.translate("MainWindow", u"PO", None))
        self.PO_meter_label_1.setText("")
        self.Clar_groupBox.setTitle(QCoreApplication.translate("MainWindow", u" CLAR", None))
        self.Clar_clear_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Clar_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"OFF", None))
        self.Clar_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Rx", None))
        self.Clar_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Tx", None))
        self.Clar_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Rx/Tx", None))

        self.Squelch_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Auto Squelch", None))
        self.Squelch_label_1.setText(QCoreApplication.translate("MainWindow", u"CTCSS", None))
        self.Squelch_label_2.setText(QCoreApplication.translate("MainWindow", u"DCS", None))
        self.Squelch_label_3.setText(QCoreApplication.translate("MainWindow", u"OFFSET", None))
        self.Squelch_offset_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"SIMPLEX", None))
        self.Squelch_offset_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"PLUS SHIFT", None))
        self.Squelch_offset_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"MINUS SHIFT", None))

        self.Squelch_label_4.setText(QCoreApplication.translate("MainWindow", u"MODE", None))
        self.Squelch_mode_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"OFF", None))
        self.Squelch_mode_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CTCSS ENC/DEC", None))
        self.Squelch_mode_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CTCSS ENC", None))
        self.Squelch_mode_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"DCS ENC/DEC", None))
        self.Squelch_mode_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"DCS ENC", None))

        self.A_B_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.A_B_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"A=B", None))
        self.A_B_pushButton_1.setText(QCoreApplication.translate("MainWindow", u"A/B", None))
        self.Memory_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Memory Channel", None))
        ___qtablewidgetitem = self.Memory_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Freq", None));
        ___qtablewidgetitem1 = self.Memory_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mode", None));
        ___qtablewidgetitem2 = self.Memory_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tag", None));
        ___qtablewidgetitem3 = self.Memory_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Skip", None));
        ___qtablewidgetitem4 = self.Memory_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CTCSS", None));
        ___qtablewidgetitem5 = self.Memory_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"DCS", None));
        ___qtablewidgetitem6 = self.Memory_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Split", None));
        ___qtablewidgetitem7 = self.Memory_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tx Freq", None));
        self.Memory_AM_pushButton.setText(QCoreApplication.translate("MainWindow", u"A\u2192M", None))
        self.Memory_VM_pushButton.setText(QCoreApplication.translate("MainWindow", u"V/M", None))
        self.Memory_scan_up_pushButton.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.Memory_scan_up_pushButton.setProperty(u"scan", QCoreApplication.translate("MainWindow", u"UP", None))
        self.Memory_scan_down_pushButton.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.Memory_scan_down_pushButton.setProperty(u"scan", QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.Memory_scan_stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Memory_scan_stop_pushButton.setProperty(u"scan", QCoreApplication.translate("MainWindow", u"OFF", None))
        self.Radio_tabWidget.setTabText(self.Radio_tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"RF", None))
        self.Notch_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Notch Filter", None))
        self.Notch_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.Notch_label_1.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.Notch_label_2.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
        self.Contour_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Contour Filter", None))
        self.Contour_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.Contour_label_1.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.Contour_label_2.setText(QCoreApplication.translate("MainWindow", u"BW", None))
        self.Contour_label_3.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.Contour_label_4.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
        self.IF_filter_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  IF Filter", None))
        self.IF_filter_BW_wide_pushButton.setText(QCoreApplication.translate("MainWindow", u"Wide", None))
        self.IF_filter_label_3.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.IF_filter_label_1.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.IF_filter_label_2.setText(QCoreApplication.translate("MainWindow", u"BW", None))
        self.IF_filter_label_4.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.IF_filter_BW_narrow_pushButton.setText(QCoreApplication.translate("MainWindow", u"Narrow", None))
        self.FrontEnd_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  RF Front End", None))
        self.FrontEnd_label_1.setText(QCoreApplication.translate("MainWindow", u"Atten.", None))
        self.FrontEnd_label_2.setText(QCoreApplication.translate("MainWindow", u"IPO", None))
        self.FrontEnd_ATT_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.FrontEnd_IPO_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"IPO", None))
        self.FrontEnd_IPO_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AMP 1", None))
        self.FrontEnd_IPO_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"AMP 2", None))

        self.Noise_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Noise Reduction", None))
        self.Noise_label_1.setText(QCoreApplication.translate("MainWindow", u"DNF", None))
        self.Noise_DNF_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.Noise_NB_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.Noise_NB_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.Noise_NB_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.Noise_NB_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.Noise_NB_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.Noise_NB_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.Noise_NB_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.Noise_NB_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.Noise_NB_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.Noise_NB_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.Noise_NB_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.Noise_NB_comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))

        self.Noise_label_3.setText(QCoreApplication.translate("MainWindow", u"NB", None))
        self.Noise_DNR_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.Noise_DNR_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.Noise_DNR_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.Noise_DNR_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.Noise_DNR_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.Noise_DNR_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.Noise_DNR_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.Noise_DNR_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.Noise_DNR_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.Noise_DNR_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.Noise_DNR_comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.Noise_DNR_comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.Noise_DNR_comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.Noise_DNR_comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.Noise_DNR_comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))

        self.Noise_DNR_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.Noise_label_2.setText(QCoreApplication.translate("MainWindow", u"DNR", None))
        self.IF_spectrum_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Frequency Spectrum", None))
        self.FFT_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"32 kHz", None))
        self.FFT_pushButton_1.setText(QCoreApplication.translate("MainWindow", u"8 kHz", None))
        self.FFT_label_2.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.FFT_window_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.FFT_window_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Hanning", None))
        self.FFT_window_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Hamming", None))
        self.FFT_window_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Bartlett", None))
        self.FFT_window_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Blackman", None))

        self.FFT_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"16 kHz", None))
        self.FFT_label_1.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.FFT_label_3.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.FFT_gain_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"+20 dB", None))
        self.FFT_gain_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"+10 dB", None))
        self.FFT_gain_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"0 dB", None))
        self.FFT_gain_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"-10 dB", None))
        self.FFT_gain_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"-20 dB", None))

        self.FFT_gain_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"0 dB", None))
        self.FFT_label_4.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.FFT_block_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"2048", None))
        self.FFT_block_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1024", None))
        self.FFT_block_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"512", None))

        self.FFT_block_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"1024", None))
        self.Radio_tabWidget.setTabText(self.Radio_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Interference Rejection", None))
        self.EQ_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  EQ Filter Response", None))
        self.EQ_1_label_1.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.EQ_1_label_2.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.EQ_1_label_3.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.EQ_2_label_3.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.EQ_2_label_1.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.EQ_2_label_2.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.EQ_3_label_2.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.EQ_3_label_1.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.EQ_3_label_3.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.EQ_1_label_4.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.EQ_2_label_4.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.EQ_3_label_4.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.EQ_comboBox.setItemText(0, "")
        self.EQ_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"High Boost 1", None))
        self.EQ_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"High Boost 2", None))
        self.EQ_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Mid Boost 1", None))
        self.EQ_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Mid Boost 2", None))
        self.EQ_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Studio Mic 1", None))

        self.EQ_label_1.setText(QCoreApplication.translate("MainWindow", u"Presets", None))
        self.EQ_pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.EQ_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Bank 1", None))
        self.EQ_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Bank 2", None))
        self.EQ_1_center_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_1_gain_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_1_BW_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_2_gain_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_2_center_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_2_BW_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_3_BW_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_3_gain_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_3_center_label.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.EQ_label_2.setText(QCoreApplication.translate("MainWindow", u"(w/ processor)", None))
        self.EQ_label_3.setText(QCoreApplication.translate("MainWindow", u"(w/o processor)", None))
        self.Speech_Proc_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Speech Processing", None))
        self.Speech_label_1.setText(QCoreApplication.translate("MainWindow", u"Microphone EQ", None))
        self.Speech_Proc_EQ_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.Speech_Proc_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.Speech_label_2.setText(QCoreApplication.translate("MainWindow", u"Speech Processor", None))
        self.Tx_Audio_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Tx Audio", None))
        self.Tx_Audio_BW_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"50~3000", None))
        self.Tx_Audio_BW_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"100~2900", None))
        self.Tx_Audio_BW_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"200~2800", None))
        self.Tx_Audio_BW_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"300~2700", None))
        self.Tx_Audio_BW_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"400~2600", None))

        self.Tx_Audio_label_1.setText(QCoreApplication.translate("MainWindow", u"Tx Bandwidth", None))
        self.Tx_Audio_label_2.setText(QCoreApplication.translate("MainWindow", u"Microphone Gain", None))
        self.Tx_Audio_label_3.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.Monitor_state_pushButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.Radio_tabWidget.setTabText(self.Radio_tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Speech Processing", None))
        self.Audio_filter_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Audio Filter Response", None))
        self.Audio_filter_pushButton_1.setText(QCoreApplication.translate("MainWindow", u"AM", None))
        self.Audio_filter_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CW", None))
        self.Audio_filter_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.Audio_filter_pushButton_4.setText(QCoreApplication.translate("MainWindow", u"RTTY", None))
        self.Audio_filter_pushButton_5.setText(QCoreApplication.translate("MainWindow", u"SSB", None))
        self.Audio_filter_label_12.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
        self.Audio_filter_label_13.setText(QCoreApplication.translate("MainWindow", u"Slope", None))
        self.Audio_filter_label_11.setText(QCoreApplication.translate("MainWindow", u"Low Cutoff", None))
        self.Audio_filter_comboBox_1.setItemText(0, QCoreApplication.translate("MainWindow", u"6dB/oct", None))
        self.Audio_filter_comboBox_1.setItemText(1, QCoreApplication.translate("MainWindow", u"18dB/oct", None))

        self.Audio_filter_label_22.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
        self.Audio_filter_label_23.setText(QCoreApplication.translate("MainWindow", u"Slope", None))
        self.Audio_filter_comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"6dB/oct", None))
        self.Audio_filter_comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"18dB/oct", None))

        self.Audio_filter_label_21.setText(QCoreApplication.translate("MainWindow", u"High Cutoff", None))
        self.Audio_filter_freq_label_1.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.Audio_filter_freq_label_2.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.Radio_tabWidget.setTabText(self.Radio_tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Audio Filter", None))
        self.menu_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"  Menu Functions", None))
        self.menu_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_105.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_52.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_153.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_140.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_57.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_55.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_56.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_67.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_95.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_126.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_147.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_40.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_134.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_49.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_44.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_63.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_64.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_99.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_76.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_109.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_174.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_61.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_84.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_142.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_127.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_162.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_112.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_50.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_133.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_70.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_173.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_42.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_66.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_96.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_90.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_122.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_89.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_146.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_114.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_128.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_80.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_150.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_71.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_83.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_107.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_61.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_144.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_148.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_101.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_137.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_56.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_135.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_129.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_69.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_140.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_93.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_75.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_77.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_130.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_67.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_69.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_82.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_117.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_68.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_109.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_154.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_48.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_79.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_135.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_112.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_138.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_120.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_110.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_130.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_113.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_126.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_175.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_62.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_141.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_65.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_169.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_116.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_180.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_43.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_158.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_170.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_143.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_148.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_133.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_141.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_73.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_183.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_38.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_147.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_94.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_137.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_59.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_78.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_73.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_88.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_47.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_124.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_118.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_127.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_85.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_53.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_36.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_104.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_34.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_185.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_37.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_121.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_105.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_155.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_163.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_83.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_85.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_93.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_64.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_113.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_182.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_58.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_114.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_117.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_145.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_149.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_71.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_115.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_66.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_62.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_39.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_91.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_123.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_167.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_75.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_35.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_144.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_125.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_100.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_128.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_139.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_94.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_87.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_166.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_45.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_111.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_59.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_111.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_124.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_87.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_142.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_41.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_131.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_179.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_97.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_51.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_97.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_143.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_131.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_161.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_79.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_176.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_108.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_82.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_102.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_99.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_149.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_58.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_153.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_150.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_29.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_181.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_80.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_90.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_91.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_88.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_101.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_81.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_132.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_123.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_177.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_89.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_65.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_103.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_49.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_120.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_160.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_106.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_81.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_178.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_119.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_156.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_106.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_54.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_108.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_100.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_57.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_98.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_74.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_103.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_77.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_84.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_104.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_151.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_63.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_92.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_165.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_146.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_152.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_107.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_136.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_78.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_46.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_74.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_76.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_157.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_119.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_68.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_118.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_159.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_122.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_172.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_102.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_116.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_139.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_152.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_136.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_134.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_115.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_72.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_86.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_151.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_98.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_70.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_129.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_164.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_121.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_132.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_171.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_138.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_184.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_168.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_72.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_110.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_60.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_145.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_55.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_96.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_125.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_95.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_92.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_86.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_label_186.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_187.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_188.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_189.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_190.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_191.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_192.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_193.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_194.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_195.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_196.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_197.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_198.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_199.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_200.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_201.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_202.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_203.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_204.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_205.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_206.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_207.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_208.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_209.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_210.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_211.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_212.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_213.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_214.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_215.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_216.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_217.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_218.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_219.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_220.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_221.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_222.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_223.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_224.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_225.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_226.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_227.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_228.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_229.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_230.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_231.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_232.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_233.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_234.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_235.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_236.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_237.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_238.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_239.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_240.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_241.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_242.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_243.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_244.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_245.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_246.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_247.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_248.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_249.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_250.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_251.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_252.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_253.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_254.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_255.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_256.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_257.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_258.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_259.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_260.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_261.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_262.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_263.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_264.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_265.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_266.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_267.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_268.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_269.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_270.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_271.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_272.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_273.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_274.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_275.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_276.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_277.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_278.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_279.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_280.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_281.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_282.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_283.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_284.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_285.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_286.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_287.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_288.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_289.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_290.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_291.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_292.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_293.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_294.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_295.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_296.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_297.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_298.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_299.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_300.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_301.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_302.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_303.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_304.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_305.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu_label_306.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Radio_tabWidget.setTabText(self.Radio_tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Radio Menu", None))
        self.Message_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Monospace'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRefresh.setTitle(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

