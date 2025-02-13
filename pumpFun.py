# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pumpFun.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ui_token_address = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui_token_address.setFont(font)
        self.ui_token_address.setObjectName("ui_token_address")
        self.horizontalLayout_2.addWidget(self.ui_token_address)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ui_buy_token_amount = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui_buy_token_amount.setFont(font)
        self.ui_buy_token_amount.setObjectName("ui_buy_token_amount")
        self.verticalLayout.addWidget(self.ui_buy_token_amount)
        self.ui_buy_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ui_buy_btn.setFont(font)
        self.ui_buy_btn.setObjectName("ui_buy_btn")
        self.verticalLayout.addWidget(self.ui_buy_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ui_sell_token_amount = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui_sell_token_amount.setFont(font)
        self.ui_sell_token_amount.setObjectName("ui_sell_token_amount")
        self.verticalLayout_2.addWidget(self.ui_sell_token_amount)
        self.ui_sell_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ui_sell_btn.setFont(font)
        self.ui_sell_btn.setObjectName("ui_sell_btn")
        self.verticalLayout_2.addWidget(self.ui_sell_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_ = QtWidgets.QPlainTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_.setFont(font)
        self.txt_.setObjectName("txt_")
        self.gridLayout.addWidget(self.txt_, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_2.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 26))
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
        self.label.setText(_translate("MainWindow", "Token Adress:"))
        self.ui_buy_token_amount.setPlaceholderText(_translate("MainWindow", "Buy Amount"))
        self.ui_buy_btn.setText(_translate("MainWindow", "Buy"))
        self.ui_sell_token_amount.setPlaceholderText(_translate("MainWindow", "Sell Amount"))
        self.ui_sell_btn.setText(_translate("MainWindow", "sell"))
        self.groupBox.setTitle(_translate("MainWindow", "Log"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Newly Created Token"))
