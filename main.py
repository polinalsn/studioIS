import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from user import User
from Views.signView.signView import signView
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

# ---- ПОЛЬЗОВАТЕЛЬСКАЯ РОЛЬ                                                                                        ----
miUser = User()

# -- Словарь с окнами --
loginWindow = loginView()
signWindow = signView()
WIDGET_DICT = {
    'login screen': loginWindow,  # 0
    'sign screen': signWindow  # 1
}
widget.addWidget(WIDGET_DICT['login screen'])
loginWindow.setWidget(widget)
loginWindow.setUser(miUser)
loginWindow.setServer(server)
widget.addWidget(WIDGET_DICT['sign screen'])
signWindow.setWidget(widget)
signWindow.setUser(miUser)
signWindow.setServer(server)

# -- Инициализация экрана входа --
try:
    temp = server.selectVersion()
    loginWindow.setVersion(str(server.selectVersion()))
    signWindow.setVersion(str(server.selectVersion()))
except Exception as e:
    loginWindow.setVersion('unversioned')

widget.show()


# ---- ОТКЛЮЧЕНИЕ СЕРВЕРА И ПРИЛОЖЕНИЯ                                                                              ----
def closeSys():
    app.exec()
    server.close()



sys.exit(closeSys())
