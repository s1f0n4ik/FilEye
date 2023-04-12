#!/urs/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget
import sys
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import matplotlib.pyplot as plt
import matplotlib.ticker as ticke
from matplotlib import ticker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sqlite3


class Ui_MainWindow_ew_mf(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 275)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(240, 235, 190)\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(182, 217, 157);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;        \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(147, 204, 105);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px    \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(182, 217, 157);\n"
"    padding: 6px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    margin: 0 -4px;\n"
"    \n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 491, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ok_but = QtWidgets.QPushButton(self.centralwidget)
        self.ok_but.setGeometry(QtCore.QRect(110, 170, 401, 28))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ok_but.setFont(font)
        self.ok_but.setObjectName("ok_but")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Пользователь не выбран! Выберите пользователя,"
                                                    " а потом возвращайтесь"))
        self.ok_but.setText(_translate("MainWindow", "Ok"))


class Ui_MainWindow_fc(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 716)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(240, 235, 190)\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(182, 217, 157);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;        \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(147, 204, 105);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px    \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(182, 217, 157);\n"
"    padding: 6px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    margin: 0 -4px;\n"
"    \n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(182, 217, 157);\n"
"    padding: 6px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    margin: 0 -4px;\n"
"    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(690, 70, 321, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.reg_but = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reg_but.setObjectName("reg_but")
        self.verticalLayout_3.addWidget(self.reg_but)
        self.choose_but = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.choose_but.setObjectName("choose_but")
        self.verticalLayout_3.addWidget(self.choose_but)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 671, 621))
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(131)
        self.main_but = QtWidgets.QPushButton(self.centralwidget)
        self.main_but.setGeometry(QtCore.QRect(10, 20, 171, 29))
        self.main_but.setObjectName("main_but")
        self.ch_label = QtWidgets.QLabel(self.centralwidget)
        self.ch_label.setGeometry(QtCore.QRect(700, 320, 301, 131))
        self.ch_label.setText("")
        self.ch_label.setObjectName("ch_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FilEye"))
        self.reg_but.setText(_translate("MainWindow", "New user"))
        self.choose_but.setText(_translate("MainWindow", "Select"))
        self.main_but.setText(_translate("MainWindow", "Main window"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1585, 975)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/poop-shit-poo-cream-ice-2_108504.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("poop-shit-poo-cream-ice-2_108504.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(240, 235, 190)\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(182, 217, 157);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;        \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(147, 204, 105);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px    \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(182, 217, 157);\n"
"    padding: 6px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    margin: 0 -4px;\n"
"    \n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(182, 217, 157);\n"
"    padding: 6px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    margin: 0 -4px;\n"
"    \n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 275, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_port_but = QtWidgets.QPushButton(self.layoutWidget)
        self.open_port_but.setObjectName("open_port_but")
        self.horizontalLayout.addWidget(self.open_port_but)
        self.close_port_but = QtWidgets.QPushButton(self.layoutWidget)
        self.close_port_but.setObjectName("close_port_but")
        self.horizontalLayout.addWidget(self.close_port_but)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 130, 361, 321))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 40, 301, 211))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.red_slider = QtWidgets.QSlider(self.layoutWidget1)
        self.red_slider.setMaximum(255)
        self.red_slider.setOrientation(QtCore.Qt.Vertical)
        self.red_slider.setObjectName("red_slider")
        self.horizontalLayout_2.addWidget(self.red_slider)
        self.green_slider = QtWidgets.QSlider(self.layoutWidget1)
        self.green_slider.setMaximum(255)
        self.green_slider.setOrientation(QtCore.Qt.Vertical)
        self.green_slider.setObjectName("green_slider")
        self.horizontalLayout_2.addWidget(self.green_slider)
        self.blue_slider = QtWidgets.QSlider(self.layoutWidget1)
        self.blue_slider.setMaximum(255)
        self.blue_slider.setOrientation(QtCore.Qt.Vertical)
        self.blue_slider.setObjectName("blue_slider")
        self.horizontalLayout_2.addWidget(self.blue_slider)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 290, 241, 19))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(100, 260, 211, 23))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spinBox_red = QtWidgets.QSpinBox(self.layoutWidget3)
        self.spinBox_red.setMaximum(255)
        self.spinBox_red.setObjectName("spinBox_red")
        self.horizontalLayout_5.addWidget(self.spinBox_red)
        self.spinBox_green = QtWidgets.QSpinBox(self.layoutWidget3)
        self.spinBox_green.setMaximum(255)
        self.spinBox_green.setObjectName("spinBox_green")
        self.horizontalLayout_5.addWidget(self.spinBox_green)
        self.spinBox_blue = QtWidgets.QSpinBox(self.layoutWidget3)
        self.spinBox_blue.setMaximum(255)
        self.spinBox_blue.setObjectName("spinBox_blue")
        self.horizontalLayout_5.addWidget(self.spinBox_blue)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 440, 341, 301))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 90, 301, 141))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.freq_dial = QtWidgets.QSlider(self.groupBox_2)
        self.freq_dial.setGeometry(QtCore.QRect(29, 70, 231, 22))
        self.freq_dial.setMouseTracking(False)
        self.freq_dial.setTabletTracking(True)
        self.freq_dial.setMinimum(10)
        self.freq_dial.setMaximum(65)
        self.freq_dial.setSingleStep(5)
        self.freq_dial.setProperty("value", 10)
        self.freq_dial.setOrientation(QtCore.Qt.Horizontal)
        self.freq_dial.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.freq_dial.setObjectName("freq_dial")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(240, 100, 55, 16))
        self.label_6.setObjectName("label_6")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(120, 110, 42, 22))
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(65)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(170, 110, 55, 21))
        self.label_8.setObjectName("label_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 20, 271, 31))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.on_b = QtWidgets.QPushButton(self.layoutWidget4)
        self.on_b.setObjectName("on_b")
        self.horizontalLayout_4.addWidget(self.on_b)
        self.off_b = QtWidgets.QPushButton(self.layoutWidget4)
        self.off_b.setObjectName("off_b")
        self.horizontalLayout_4.addWidget(self.off_b)
        self.fix_point_button = QtWidgets.QPushButton(self.layoutWidget4)
        self.fix_point_button.setObjectName("fix_point_button")
        self.horizontalLayout_4.addWidget(self.fix_point_button)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 230, 301, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.point_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.point_label.setObjectName("point_label")
        self.verticalLayout.addWidget(self.point_label)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(440, 10, 1041, 671))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.escape_but = QtWidgets.QPushButton(self.centralwidget)
        self.escape_but.setGeometry(QtCore.QRect(0, 0, 151, 29))
        self.escape_but.setObjectName("escape_but")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 50, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.update_but = QtWidgets.QPushButton(self.centralwidget)
        self.update_but.setGeometry(QtCore.QRect(160, 50, 93, 28))
        self.update_but.setObjectName("update_but")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(290, 90, 141, 29))
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FilEye"))
        self.open_port_but.setText(_translate("MainWindow", "Open"))
        self.close_port_but.setText(_translate("MainWindow", "Close"))
        self.groupBox.setTitle(_translate("MainWindow", "        Color control"))
        self.label.setText(_translate("MainWindow", "     Red"))
        self.label_2.setText(_translate("MainWindow", "  Green"))
        self.label_3.setText(_translate("MainWindow", "  Blue"))
        self.label_4.setText(_translate("MainWindow", "Port"))
        self.groupBox_4.setTitle(_translate("MainWindow", "    Frequency control"))
        self.label_5.setText(_translate("MainWindow", "10 Гц"))
        self.label_6.setText(_translate("MainWindow", "65 Гц"))
        self.label_8.setText(_translate("MainWindow", "Гц"))
        self.groupBox_3.setTitle(_translate("MainWindow", "On/Off frequency"))
        self.on_b.setText(_translate("MainWindow", "on"))
        self.off_b.setText(_translate("MainWindow", "off"))
        self.fix_point_button.setText(_translate("MainWindow", "Fix point"))
        self.point_label.setText(_translate("MainWindow", "Осталось точек: 7"))
        self.label_7.setText(_translate("MainWindow", "Graphic :"))
        self.escape_but.setText(_translate("MainWindow", "Main window"))
        self.update_but.setText(_translate("MainWindow", "Update"))
        self.save_button.setText(_translate("MainWindow", "Save"))


class Ui_MainWindow_reg(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 657)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(240, 235, 190)\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(182, 217, 157);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;        \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(147, 204, 105);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px    \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(182, 217, 157);\n"
"    padding: 6px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    margin: 0 -4px;\n"
"    \n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(182, 217, 157);\n"
"    padding: 6px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    margin: 0 -4px;\n"
"    \n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.registration_but = QtWidgets.QPushButton(self.centralwidget)
        self.registration_but.setGeometry(QtCore.QRect(240, 460, 611, 28))
        self.registration_but.setObjectName("registration_but")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 180, 101, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(340, 166, 501, 281))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.surname_edit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.surname_edit.setObjectName("surname_edit")
        self.verticalLayout.addWidget(self.surname_edit)
        self.name_edit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.name_edit.setObjectName("name_edit")
        self.verticalLayout.addWidget(self.name_edit)
        self.patronymic_edit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.patronymic_edit.setObjectName("patronymic_edit")
        self.verticalLayout.addWidget(self.patronymic_edit)
        self.group_edit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.group_edit.setObjectName("group_edit")
        self.verticalLayout.addWidget(self.group_edit)
        self.gender_edit = QtWidgets.QComboBox(self.layoutWidget_2)
        self.gender_edit.setObjectName("gender_edit")
        self.gender_edit.addItem("")
        self.gender_edit.addItem("")
        self.gender_edit.addItem("")
        self.verticalLayout.addWidget(self.gender_edit)
        self.cancel_but = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_but.setGeometry(QtCore.QRect(240, 510, 611, 28))
        self.cancel_but.setObjectName("cancel_but")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FilEye"))
        self.registration_but.setText(_translate("MainWindow", "Save"))
        self.label_3.setText(_translate("MainWindow", "    Фамилия"))
        self.label_2.setText(_translate("MainWindow", "      Имя"))
        self.label.setText(_translate("MainWindow", "    Отчество"))
        self.label_5.setText(_translate("MainWindow", "  Номер группы"))
        self.label_6.setText(_translate("MainWindow", "         Пол"))
        self.gender_edit.setItemText(0, _translate("MainWindow", "Выбрать..."))
        self.gender_edit.setItemText(1, _translate("MainWindow", "Мужской"))
        self.gender_edit.setItemText(2, _translate("MainWindow", "Женский"))
        self.cancel_but.setText(_translate("MainWindow", "Cancel"))


class Ui_MainWindow_sw(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 677)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(240, 235, 190)\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(182, 217, 157);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;        \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(147, 204, 105);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px    \n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 270, 521, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Cabin_but = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Cabin_but.setObjectName("Cabin_but")
        self.verticalLayout.addWidget(self.Cabin_but)
        self.start_but = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_but.setObjectName("start_but")
        self.verticalLayout.addWidget(self.start_but)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FilEye"))
        self.Cabin_but.setText(_translate("MainWindow", "File cabinet"))
        self.start_but.setText(_translate("MainWindow", "Start"))


class Ui_MainWindow_ew(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 275)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(240, 235, 190)\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(182, 217, 157);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;        \n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(147, 204, 105);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px    \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(182, 217, 157);\n"
"    padding: 6px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    margin: 0 -4px;\n"
"    \n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 491, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ok_but = QtWidgets.QPushButton(self.centralwidget)
        self.ok_but.setGeometry(QtCore.QRect(110, 170, 401, 28))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ok_but.setFont(font)
        self.ok_but.setObjectName("ok_but")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Такой пользователь уже имеется!"))
        self.ok_but.setText(_translate("MainWindow", "Ok"))


class MainFuncWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.start()
        self.set()
        self.count = 0
        self.flag = False

    def start(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.serial = QSerialPort()
        self.serial.setBaudRate(19200)  # Задаём скорость (Как на Arduino)

    def update_ports(self):
            ports = QSerialPortInfo().availablePorts()
            ports_list = []
            for port in ports:
                    ports_list.append(port.portName())
            self.ui.comboBox.addItems(ports_list)

    def on_open(self):

        self.serial.setPortName(self.ui.comboBox.currentText())
        self.serial.open(QIODevice.ReadWrite)

    def on_close(self):
        self.serial.close()

    def write_serial(self, data: list):
        txs = ""
        for value in data:
            txs += str(value)
            txs += ","
        txs = txs[:-1]
        txs += ";\n"
        self.serial.write(txs.encode())

    def err_win(self):
            err_window = ErrorWindow_mf()
            widget.addWidget(err_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def check_sel_user(self):
        try:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                cursor.execute("SELECT * WHERE flag = 1")
                if cursor.fetchall() == None:
                        self.err_win()

        except sqlite3.Error as err:
                print("Error: ", err)
        finally:
                cursor.close()
                db.close()

    def click_off(self):
        self.write_serial([2, 0, 0, 0])

    def click_on(self):
        self.write_serial([2, 1, 0, 0])
        self.flag = True

    def frequency_control_slider(self):
        self.write_serial([1, self.ui.freq_dial.value(), 0, 0])
        self.ui.spinBox.setValue(self.ui.freq_dial.value())

    def frequency_control_spinbox(self):
        self.write_serial([1, self.ui.spinBox.value(), 0, 0])
        self.ui.freq_dial.setValue(self.ui.spinBox.value())

    def rgb_control(self):
        self.write_serial([0, self.ui.red_slider.value(), self.ui.green_slider.value(), self.ui.blue_slider.value()])
        self.ui.spinBox_red.setValue(self.ui.red_slider.value())
        self.ui.spinBox_green.setValue(self.ui.green_slider.value())
        self.ui.spinBox_blue.setValue(self.ui.blue_slider.value())

    def rgb_control_spinbox_red(self):
        self.write_serial([0, self.ui.spinBox_red.value(), self.ui.spinBox_green.value(), self.ui.spinBox_blue.value()])
        self.ui.red_slider.setValue(self.ui.spinBox_red.value())

    def rgb_control_spinbox_green(self):
        self.write_serial([0, self.ui.spinBox_red.value(), self.ui.spinBox_green.value(), self.ui.spinBox_blue.value()])
        self.ui.green_slider.setValue(self.ui.spinBox_green.value())

    def rgb_control_spinbox_blue(self):
        self.write_serial([0, self.ui.spinBox_red.value(), self.ui.spinBox_green.value(), self.ui.spinBox_blue.value()])
        self.ui.blue_slider.setValue(self.ui.spinBox_blue.value())

    def back_start_win(self):
        start_w = StartWindow()
        widget.addWidget(start_w)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        self.MainWindow.close()

    def set_count(self):
        self.count += 1
        self.making_points()
        if 6 - self.count <= 0:
            self.ui.point_label.setText("Всё!")
        elif 6 - self.count == 1:
            self.ui.point_label.setText("Последняя точка!")
        else:
            self.ui.point_label.setText("Осталось точек:" + str(6 - self.count))

    def making_points(self):
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            if self.count <= 7:
                values = f"{self.ui.spinBox_red.value()} {self.ui.spinBox_green.value()}" \
                         f" {self.ui.spinBox_blue.value()} {self.ui.spinBox.value()}"

                if self.count == 1:
                    cursor.execute("UPDATE users SET color_and_freq1 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 2:
                    cursor.execute("UPDATE users SET color_and_freq2 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 3:
                    cursor.execute("UPDATE users SET color_and_freq3 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 4:
                    cursor.execute("UPDATE users SET color_and_freq4 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 5:
                    cursor.execute("UPDATE users SET color_and_freq5 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 6:
                    cursor.execute("UPDATE users SET color_and_freq6 = ? WHERE flag = ?", [values, 1])
                    db.commit()

        except sqlite3.Error as err:
            print("Error: ", err)
        finally:
            cursor.close()
            db.close()

    def making_graph(self):
        if self.ui.horizontalLayout_6.isEmpty():
                self.check_sel_user()
                if self.flag == False:
                        self.ui.point_label.setText("Включите частоту!")
                else:

                        try:
                            db = sqlite3.connect("database.db")
                            cursor = db.cursor()
                            x1 = cursor.execute("SELECT color_and_freq1 FROM users WHERE flag = ?", [1]).fetchone()
                            x2 = cursor.execute("SELECT color_and_freq2 FROM users WHERE flag = ?", [1]).fetchone()
                            x3 = cursor.execute("SELECT color_and_freq3 FROM users WHERE flag = ?", [1]).fetchone()
                            x4 = cursor.execute("SELECT color_and_freq4 FROM users WHERE flag = ?", [1]).fetchone()
                            x5 = cursor.execute("SELECT color_and_freq5 FROM users WHERE flag = ?", [1]).fetchone()
                            x6 = cursor.execute("SELECT color_and_freq6 FROM users WHERE flag = ?", [1]).fetchone()
                            data_values = [int(x1[0].split()[3]), int(x2[0].split()[3]), int(x3[0].split()[3]), int(x4[0].split()[3]),
                                           int(x5[0].split()[3]), int(x6[0].split()[3])]
                            xs = range(len(data_values))

                            y1 = cursor.execute("SELECT color_and_freq1 FROM users WHERE flag = ?", [1]).fetchone()
                            y2 = cursor.execute("SELECT color_and_freq2 FROM users WHERE flag = ?", [1]).fetchone()
                            y3 = cursor.execute("SELECT color_and_freq3 FROM users WHERE flag = ?", [1]).fetchone()
                            y4 = cursor.execute("SELECT color_and_freq4 FROM users WHERE flag = ?", [1]).fetchone()
                            y5 = cursor.execute("SELECT color_and_freq5 FROM users WHERE flag = ?", [1]).fetchone()
                            y6 = cursor.execute("SELECT color_and_freq6 FROM users WHERE flag = ?", [1]).fetchone()
                            data_names = [y1[0].split()[:3], y2[0].split()[:3], y3[0].split()[:3], y4[0].split()[:3], y5[0].split()[:3],
                                          y6[0].split()[:3]]
                            fig = plt.figure()
                            ax = plt.axes()
                            ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
                            ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
                            ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
                            ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

                            #  Добавляем линии основной сетки:
                            ax.grid(which='major',
                                    color='k')

                            #  Включаем видимость вспомогательных делений:
                            ax.minorticks_on()
                            #  Теперь можем отдельно задавать внешний вид
                            #  вспомогательной сетки:
                            ax.grid(which='minor',
                                    color='gray',
                                    linestyle=':')
                            ax.set_xlabel("Цвет в RGB-системе (бит)")
                            ax.set_ylabel("Частота (Гц)")
                            ax.yaxis.grid(True, zorder=1)
                            color_theme = [(round(int(data_names[0][0]) / 255, 2), round(int(data_names[0][1]) / 255, 2), round(int(data_names[0][2]) / 255, 2)),
                                           (round(int(data_names[1][0]) / 255, 2), round(int(data_names[1][1]) / 255, 2),
                                            round(int(data_names[1][2]) / 255, 2)), (round(int(data_names[2][0]) / 255, 2),
                                                                                  round(int(data_names[2][1]) / 255, 2),
                                                                                  round(int(data_names[2][2]) / 255, 2)),
                                           (round(int(data_names[3][0]) / 255, 2), round(int(data_names[3][1]) / 255, 2), round(int(data_names[3][2]) / 255, 2)), (round(int(data_names[4][0]) / 255, 2), round(int(data_names[4][1]) / 255, 2),
                                                                                                    round(int(data_names[4][2]) / 255, 2)),
                                           (round(int(data_names[5][0]) / 255, 2), round(int(data_names[5][1]) / 255, 2), round(int(data_names[5][2]) / 255, 2))]
                            plt.bar([x + 0.05 for x in xs], data_values, color = color_theme)
                            plt.xticks(xs, data_names)
                            canvas = FigureCanvas(fig)
                            canvas.draw()
                            self.ui.horizontalLayout_6.addWidget(canvas)
                        except sqlite3.Error as err:
                            print("Error: ", err)
                        finally:
                            cursor.close()
                            db.close()
        else:
                self.ui.point_label.setText("График уже сделан. Попробуйте выбрать нового пользователя "
                                            "или переснять для выбранного")

    def set(self):
        self.ui.open_port_but.clicked.connect(self.on_open)
        self.ui.close_port_but.clicked.connect(self.on_close)
        self.ui.freq_dial.valueChanged.connect(self.frequency_control_slider)
        self.ui.spinBox.valueChanged.connect(self.frequency_control_spinbox)
        self.ui.red_slider.valueChanged.connect(self.rgb_control)
        self.ui.green_slider.valueChanged.connect(self.rgb_control)
        self.ui.blue_slider.valueChanged.connect(self.rgb_control)
        self.ui.spinBox_red.valueChanged.connect(self.rgb_control_spinbox_red)
        self.ui.spinBox_green.valueChanged.connect(self.rgb_control_spinbox_green)
        self.ui.spinBox_blue.valueChanged.connect(self.rgb_control_spinbox_blue)
        self.ui.on_b.clicked.connect(self.click_on)
        self.ui.off_b.clicked.connect(self.click_off)
        self.ui.fix_point_button.clicked.connect(self.set_count)
        self.ui.save_button.clicked.connect(self.making_graph)
        self.ui.escape_but.clicked.connect(self.back_start_win)
        self.ui.update_but.clicked.connect(self.update_ports)


class StartWindow(QWidget, Ui_MainWindow_sw):
    def __init__(self):
        super().__init__()
        self.start_sw()
        self.set_sw()

    def start_sw(self):
        self.MainWindow_sw = QtWidgets.QMainWindow()
        self.ui_sw = Ui_MainWindow_sw()
        self.ui_sw.setupUi(self.MainWindow_sw)
        self.MainWindow_sw.show()

    def open_main_func_win(self):
        main_func_win = MainFuncWindow()
        # noinspection PyTypeChecker
        widget.addWidget(main_func_win)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.MainWindow_sw.close()

    def open_file_cabinet(self):
        file_cab = FileCabinetWindow()
        widget.addWidget(file_cab)
        widget.setCurrentIndex(widget.currentIndex() + 2)
        self.MainWindow_sw.close()

    def set_sw(self):
        self.ui_sw.start_but.clicked.connect(self.open_main_func_win)
        self.ui_sw.Cabin_but.clicked.connect(self.open_file_cabinet)


class FileCabinetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_fc()
        self.set_fc()
        self.table_set()
        self.db_show()

    def start_fc(self):
        self.MainWindow_fc = QtWidgets.QMainWindow()
        self.ui_fc = Ui_MainWindow_fc()
        self.ui_fc.setupUi(self.MainWindow_fc)
        self.MainWindow_fc.show()
        self.create_db()

    def table_set(self):
        self.ui_fc.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Имя", "Отчество", "Группа", "Пол"])

    def create_db(self):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS users(
                surname VARCHAR(30),
                first_name VARCHAR(30),
                patronymic VARCHAR(30),
                platoon VARCHAR(4),
                gender VARCHAR(7),
                id INTEGER PRIMARY KEY,
                color_and_freq1 VARCHAR(20),
                color_and_freq2 VARCHAR(20),
                color_and_freq3 VARCHAR(20),
                color_and_freq4 VARCHAR(20),
                color_and_freq5 VARCHAR(20),
                color_and_freq6 VARCHAR(20),
                flag INTEGER,
                count INTEGER   
            )  
            """
            cursor.executescript(query)

    def db_show(self):
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        query = "SELECT * FROM users"
        cur.execute("""SELECT COUNT(*) FROM users""")
        res = cur.fetchone()[0]
        self.ui_fc.tableWidget.setRowCount(res)
        tablerow = 0
        for row in cur.execute(query):
            self.ui_fc.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui_fc.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui_fc.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui_fc.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui_fc.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui_fc.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

    def choose_user(self):
        cur_row = self.ui_fc.tableWidget.currentRow()
        if cur_row == None:
                self.ui_fc.ch_label.setText("Пользователь не выбран!")
        else:
                try:
                    db = sqlite3.connect("database.db")
                    cursor = db.cursor()
                    cursor.execute("SELECT flag FROM users WHERE flag = ?", [1])
                    if cursor.fetchall() is None:
                        cursor.execute("UPDATE users SET flag = ? WHERE id = ?", [1, cur_row + 1])
                        db.commit()
                        self.ui_fc.ch_label.setText("Пользователь выбран")
                    else:
                        cursor.execute("UPDATE users SET flag = ? WHERE flag = ?", [0, 1])
                        cursor.execute("UPDATE users SET flag = ? WHERE id = ?", [1, cur_row + 1])
                        db.commit()
                        self.ui_fc.ch_label.setText("Пользователь выбран")

                except sqlite3.Error as err:
                    print("Error: ", err)
                finally:
                    cursor.close()
                    db.close()

    def open_reg(self):
        reg_w = RegistrationWindow()
        widget.addWidget(reg_w)
        widget.setCurrentIndex(widget.currentIndex() + 3)
        self.MainWindow_fc.close()

    def back_start_win(self):
        start_w = StartWindow()
        widget.addWidget(start_w)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        self.MainWindow_fc.close()

    def set_fc(self):
        self.ui_fc.reg_but.clicked.connect(self.open_reg)
        self.ui_fc.main_but.clicked.connect(self.back_start_win)
        self.ui_fc.choose_but.clicked.connect(self.choose_user)


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_reg()
        self.set_reg()

    def start_reg(self):

        self.MainWindow_reg = QtWidgets.QMainWindow()
        self.ui_reg = Ui_MainWindow_reg()
        self.ui_reg.setupUi(self.MainWindow_reg)
        self.MainWindow_reg.show()

    def set_reg(self):
        self.ui_reg.registration_but.clicked.connect(self.registration)
        self.ui_reg.cancel_but.clicked.connect(self.return_to_file_cab)

    def return_to_file_cab(self):
        file_cab = FileCabinetWindow()
        widget.addWidget(file_cab)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        self.MainWindow_reg.close()

    def err_win(self):
        err_window = ErrorWindow()
        widget.addWidget(err_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def registration(self):
        user_surname = self.ui_reg.surname_edit.text()
        user_name = self.ui_reg.name_edit.text()
        user_patronymic = self.ui_reg.patronymic_edit.text()
        user_group = self.ui_reg.group_edit.text()
        user_gender = self.ui_reg.gender_edit.currentText()
        if user_surname == "" or user_name == "" or user_group == "" or user_gender == "Выбрать...":
            self.ui_reg.surname_edit.clear()
            self.ui_reg.name_edit.clear()
            self.ui_reg.patronymic_edit.clear()
            self.ui_reg.group_edit.clear()
        else:
            try:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                cursor.execute("SELECT surname FROM users WHERE surname = ?", [user_surname])
                # (surname,)
                if cursor.fetchone() is None:
                    cursor.execute("SELECT first_name FROM users WHERE first_name = ?", [user_name])
                    if cursor.fetchone() is None:
                        cursor.execute("INSERT INTO users(surname, first_name, patronymic, platoon, gender, count) "
                                       "VALUES(?, ?, ?, ?, ?, ?)",
                                       [user_surname, user_name, user_patronymic, user_group, user_gender, 0])

                        db.commit()
                        self.return_to_file_cab()
                    else:
                        self.err_win()
                else:
                    self.err_win()
            except sqlite3.Error as err:
                print("Error: ", err)
            finally:
                cursor.close()
                db.close()


class ErrorWindow(QWidget, Ui_MainWindow_ew):
    def __init__(self):
        super().__init__()
        self.start_err()
        self.set_err()

    def start_err(self):
        self.MainWindow_er = QtWidgets.QMainWindow()
        self.ui_err = Ui_MainWindow_ew()
        self.ui_err.setupUi(self.MainWindow_er)
        self.MainWindow_er.show()

    def ok(self):
        self.MainWindow_er.close()

    def set_err(self):
        self.ui_err.ok_but.clicked.connect(self.ok)


class ErrorWindow_mf(QWidget, Ui_MainWindow_ew_mf):
    def __init__(self):
        super().__init__()
        self.start_err()
        self.set_err()

    def start_err(self):
        self.MainWindow_er = QtWidgets.QMainWindow()
        self.ui_err_mf = Ui_MainWindow_ew_mf()
        self.ui_err_mf.setupUi(self.MainWindow_er)
        self.MainWindow_er.show()

    def ok(self):
        self.MainWindow_er.close()

    def set_err(self):
        self.ui_err_mf.ok_but.clicked.connect(self.ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = StartWindow()
    widget = QStackedWidget()
    widget.addWidget(ex)
    widget.setFixedWidth(400)
    widget.setFixedHeight(300)
    app.exec()
