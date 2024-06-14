import sys
import asyncio
import json
import websockets
import threading
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread

class Worker(QObject):
    token_creation_event = pyqtSignal(dict)

    def __init__(self, websocket_url, payload):
        super().__init__()
        self.websocket_url = websocket_url
        self.payload = payload

    async def handle_event(self, event):
        print("Token creation event received:")
        if 'mint' in event:
            self.token_creation_event.emit(event)

    async def subscribe_token_creation_event(self):
        async with websockets.connect(self.websocket_url) as websocket:
            await websocket.send(self.payload)
            while True:
                message = await websocket.recv()
                event = json.loads(message)
                await self.handle_event(event)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.subscribe_token_creation_event())
        loop.close()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.api_key = ""
        self.slippage = 0
        self.priorityFee = 0
        self.tokenAdress = ""
        self.websocket_url = ""
        self.tradeAmount = 0
        self.denominatedInSol = "false"
        self.pumpUrl = ""
        self.pool = "pump"
        self.worker_thread = None
        self.worker = None
        self.init_setting()
        self.read_config()

    def init_setting(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.show()
        self.setupUi(self.MainWindow)
        self.retranslateUi(self.MainWindow)
        self.payload = json.dumps({
            "method": "subscribeNewToken",
        })

    def start_worker(self):
        self.worker = Worker(self.websocket_url, self.payload)
        self.worker.token_creation_event.connect(self.handle_event)

        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.start()

    @QtCore.pyqtSlot(dict)
    def handle_event(self, event):
        print("Token creation event received:")
        if 'mint' in event:
            print(event)
            self.ui_token_creation_log.appendPlainText(f"#{event['mint']}")

    def read_config(self):
        try:
            with open('config.json') as f:
                data = json.load(f)
                self.api_key = data['api_key']
                self.priorityFee = data['priorityFee']
                self.pool = data["pool"]
                self.denominatedInSol = data["denominatedInSol"]
                self.websocket_url = data["websocket_url"]
                self.slippage = data["slippage"]
                self.pumpUrl = "https://pumpportal.fun/api/trade?api-key=" + self.api_key
                print('Read config success!')
                self.start_worker()
        except Exception as e:
            print(e)
            print("config file read failed...")

    def buy_token(self):
        self.tradeAmount = int(float(self.ui_buy_token_amount.text()))
        self.tokenAdress = self.ui_token_address.text()
        self.action = "buy"
        self.ui_token_trade_log.appendPlainText("buy")

    def sell_token(self):
        self.tradeAmount = int(float(self.ui_sell_token_amount.text()))
        self.tokenAdress = self.ui_token_address.text()
        self.action = "sell"

    def make_trade(self):
        response = requests.post(url=self.pumpUrl, data={
            "action": self.action,
            "mint": self.tokenAdress,
            "amount": self.tradeAmount,
            "denominatedInSol": self.denominatedInSol,
            "slippage": self.slippage,
            "priorityFee": self.priorityFee,
            "pool": self.pool
        })
        data = response.json()
        print(data)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
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
        self.verticalLayout = QtWidgets.QVBoxLayout()
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
        self.ui_token_trade_log = QtWidgets.QPlainTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui_token_trade_log.setFont(font)
        self.ui_token_trade_log.setObjectName("ui_token_trade_log")
        self.gridLayout.addWidget(self.ui_token_trade_log, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.ui_token_creation_log = QtWidgets.QPlainTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui_token_creation_log.setFont(font)
        self.ui_token_creation_log.setObjectName("ui_token_creation_log")
        self.gridLayout_2.addWidget(self.ui_token_creation_log, 0, 0, 1, 1)
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

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("PumpFunSnipperBot", "PumpFunSnipperBot"))
        self.label.setText(_translate("MainWindow", "Token Adress:"))
        self.ui_buy_token_amount.setPlaceholderText(_translate("MainWindow", "Buy Amount"))
        self.ui_buy_btn.setText(_translate("MainWindow", "Buy"))
        self.ui_sell_token_amount.setPlaceholderText(_translate("MainWindow", "Sell Amount"))
        self.ui_sell_btn.setText(_translate("MainWindow", "sell"))
        self.groupBox.setTitle(_translate("MainWindow", "Log"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Newly Created Token"))
        self.ui_buy_btn.clicked.connect(self.buy_token)
        self.ui_sell_btn.clicked.connect(self.sell_token)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Ui_MainWindow()
    sys.exit(app.exec_())





