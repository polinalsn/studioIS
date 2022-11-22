from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi


class mainView(QtWidgets.QMainWindow):

    def __int__(self):
        super(mainView, self).__init__()

    def loadWindow(self):
        loadUi("studio.ui", self)
        self.tabWidget.setTabText(0, 'Поиск по таблицам')
        self.tabWidget.setTabText(1, 'Работа с данными')
        self.statusbar.showMessage("Ателье, Лесневская Полина Сергеевна")
        self.loadTabTables()

    def loadTabTables(self):
        pass

    def setServer(self, server):
        self.server = server

    def setWidget(self, widget):
        self.widget = widget
