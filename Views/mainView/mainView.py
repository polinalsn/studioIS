from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi


class mainView(QtWidgets.QMainWindow):
    def __int__(self):
        super(mainView, self).__init__()

    def setWidget(self, widget):
        self.widget = widget

    def setUser(self, user):
        self.user = user

    def loadProfile(self):
        # -- Настройка надписей --
        self.nameLabel.setFont(
            QtGui.QFont('SansSerif', 18, QFont.Bold)
        )
        self.roleLabel.setFont(
            QtGui.QFont('SansSerif', 18, QFont.Bold)
        )
        self.nameText.setFont(
           QtGui.QFont('SansSerif', 18)
        )
        self.roleText.setFont(
            QtGui.QFont('SansSerif', 18)
        )
        self.nameText.setText(self.user.name)
        match self.user.role:
            case 'user\n':
                self.roleText.setText('Пользователь')
            case 'admin\n':
                self.roleText.setText('Администратор')
            case 'user':
                self.roleText.setText('Пользователь')
            case 'admin':
                self.roleText.setText('Администратор')

        # -- Настройка кнопок --
        self.updBook.setFont(
            QtGui.QFont('SansSerif', 24)
        )
        self.updBook.clicked.connect(self.setupBookTabel)

    def setupUI(self):
        loadUi("Views\mainView\mainView.ui", self)
        self.tabWidget.setTabText(0, 'Профиль')
        self.tabWidget.setTabText(1, 'Таблицы')

    def setupBookTabel(self):
        self.tabelBook.setColumnCount(6)
        self.tabelBook.setHorizontalHeaderLabels(['ID книги', 'Название книги', 'Статус', 'Жанр', 'Год издания', 'ID автора'])
        self.setBookData(self.server.selectBooks())
        tabelrow = 0
        self.tabelBook.setRowCount(self.bookSize)
        for row in self.bookData:
            print(row)
            self.tabelBook.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabelBook.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tabelBook.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabelBook.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tabelBook.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(row[4].strftime('%m/%d/%Y')))
            self.tabelBook.setItem(tabelrow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            tabelrow += 1

    def setBookData(self, Data):
        self.bookData = Data
        self.bookSize = len(Data)

    def setServer(self, server):
        self.server = server
