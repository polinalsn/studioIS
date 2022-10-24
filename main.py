import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from server import Server
from Views.loginView.loginView import loginView


# ---- ПОДКЛЮЧЕНИЕ СЕРВЕРА                                                                                          ----
server = Server()
server.connectDB()


# ---- ПОДКЛЮЧЕНИЕ ИНТЕРФЕЙСА                                                                                       ----
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(1280)
widget.setFixedHeight(720)
widget.setWindowTitle('Автоматизированная библиотечная информационная система')

# -- Словарь с окнами --
loginWindow = loginView()
WIDGET_DICT = {
    'login screen': loginWindow
}

# -- Инициализация экрана входа --
widget.addWidget(WIDGET_DICT['login screen'])
try:
    temp = server.selectVersion()
    loginWindow.setVersion(str(server.selectVersion()))
except Exception as e:
    loginWindow.setVersion('unversioned')

widget.show()

# ---- ОТКЛЮЧЕНИЕ СЕРВЕРА И ПРИЛОЖЕНИЯ                                                                              ----
def closeSys():
    app.exec()
    server.close()


sys.exit(closeSys())
