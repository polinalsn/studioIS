import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from server import Server
from mainView import mainView

# ---- ПОДКЛЮЧЕНИЕ СЕРВЕРА                                                                                          ----
server = Server()
server.connectDB()

# ---- ПОДКЛЮЧЕНИЕ ИНТЕРФЕЙСА                                                                                       ----
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(1280)
widget.setFixedHeight(720)
widget.setWindowTitle('Ателье')

# -- Словарь с окнами --
mainWindow = mainView()
widget.addWidget(mainWindow)
mainWindow.setWidget(widget)
mainWindow.setServer(server)
mainWindow.loadWindow()

# -- Инициализация экрана входа --
widget.show()


# ---- ОТКЛЮЧЕНИЕ СЕРВЕРА И ПРИЛОЖЕНИЯ                                                                              ----
def closeSys():
    app.exec()
    server.close()



sys.exit(closeSys())
