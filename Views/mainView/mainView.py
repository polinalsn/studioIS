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

    def setData(self, Data):
        self.data = Data
        self.size = len(Data)

    def setServer(self, server):
        self.server = server

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
        self.upd.setFont(
            QtGui.QFont('SansSerif', 24)
        )
        self.upd.clicked.connect(self.setupTabel)

    def setupUI(self):
        loadUi("Views\mainView\mainView.ui", self)
        self.tabWidget.setTabText(0, 'Профиль')
        self.tabWidget.setTabText(1, 'Таблицы')

    def setupTabel(self):
        match self.comboBox.currentText():
            case 'Книги':
                self.setupBookTabel()
            case 'Авторы':
                self.setupAuthorTabel()
            case 'Формуляры':
                self.setupFormularTabel()
            case 'Работники библиотеки':
                self.setupWorkerTabel()
            case 'Должности':
                self.setupPostTabel()
            case 'Билеты':
                self.setupTicketTabel()

    def setupBookTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(6)
        self.tabel.setHorizontalHeaderLabels(
            ['ID Книги', 'Название книги', 'Статус', 'Жанр', 'Год издания', 'ID Автора'])
        self.setData(self.server.selectBooks())
        tabelrow = 0
        self.tabel.setRowCount(self.size)
        for row in self.data:
            self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tabel.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(row[4].strftime('%m/%d/%Y')))
            self.tabel.setItem(tabelrow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            tabelrow += 1

    def setupAuthorTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(4)
        self.tabel.setHorizontalHeaderLabels(['ID Автора', 'Имя', 'Фамилия', 'Дата рождения'])
        self.setData(self.server.selectAuthors())
        tabelrow = 0
        self.tabel.setRowCount(self.size)
        for row in self.data:
            self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%m/%d/%Y')))
            tabelrow += 1

    def setupFormularTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(6)
        self.tabel.setHorizontalHeaderLabels(
            ['ID Формуляра', 'ID Билета', 'ID Рабочего', 'Дата выдачи', 'Дата возврата', 'Книги'])
        self.setData(self.server.selectFormulars())
        tabelrow = 0
        self.tabel.setRowCount(self.size)
        for row in self.data:
            self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%m/%d/%Y')))
            self.tabel.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(row[4].strftime('%m/%d/%Y')))
            self.tabel.setItem(tabelrow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tabelrow += 1

    def setupWorkerTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(5)
        self.tabel.setHorizontalHeaderLabels(['ID Рабочего', 'Имя', 'Фамилия', 'Дата рождения', 'Должность'])
        self.setData(self.server.selectLibraryWorkers())
        tabelrow = 0
        self.tabel.setRowCount(self.size)
        for row in self.data:
            self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%m/%d/%Y')))
            self.tabel.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tabelrow += 1

    def setupPostTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(4)
        self.tabel.setHorizontalHeaderLabels(['Название должности', 'Зарплата', 'Дата найма', 'Уровень допуска'])
        self.setData(self.server.selectPosts())
        tabelrow = 0
        self.tabel.setRowCount(self.size)
        for row in self.data:
            self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2].strftime('%m/%d/%Y')))
            self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tabelrow += 1

    def setupTicketTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(5)
        self.tabel.setHorizontalHeaderLabels(['ID Читательского билета', 'Имя', 'Фамилия', 'Дата рождениия', 'Рейтинг'])
        self.setData(self.server.selectTickets())
        tabelrow = 0
        self.tabel.setRowCount(self.size)
        for row in self.data:
            self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%m/%d/%Y')))
            self.tabel.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            tabelrow += 1
