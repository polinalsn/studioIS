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
        self.labelTabel.setFont(
            QtGui.QFont('SansSerif', 24)
        )
        self.label1.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.label2.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.label3.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.label4.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.label5.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.label6.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.answState.setFont(
            QtGui.QFont('SansSeruf', 14)
        )

        # -- Настройка кнопок --
        self.upd.setFont(
            QtGui.QFont('SansSerif', 24)
        )
        self.upd.clicked.connect(self.setupTabel)
        self.btnExec.setFont(
            QtGui.QFont('SansSerif', 32)
        )
        self.btnExec.clicked.connect(self.tryFunc)

        #-- Настройка комбобоксов --
        self.boxTabel.currentTextChanged.connect(self.checkTabel)
        self.boxFunc.currentTextChanged.connect(self.checkFunc)

        # -- Настройка доп херни --
        self.date1.setFont(
            QtGui.QFont('SansSerif', 18)
        )
        self.date2.setFont(
            QtGui.QFont('SansSerif', 18)
        )
        self.checkBox.setFont(
            QtGui.QFont('SansSerif', 18)
        )

        #-- Настройка стартового окна --
        self.label1.setVisible(True)
        self.label2.setVisible(True)
        self.label3.setVisible(True)
        self.label4.setVisible(True)
        self.label5.setVisible(True)
        self.label6.setVisible(True)

        self.input1.setVisible(True)
        self.input2.setVisible(True)
        self.input3.setVisible(False)
        self.input4.setVisible(True)
        self.input5.setVisible(False)
        self.input6.setVisible(True)

        self.checkBox.setVisible(True)
        self.date1.setVisible(False)
        self.date2.setVisible(True)
        self.date3.setVisible(False)

        self.label1.setText('ID Книги')
        self.label2.setText('Название книги')
        self.label3.setText('Наличие')
        self.label4.setText('Жанр')
        self.label5.setText('Дата публикации')
        self.label6.setText('ID Автора')
        self.checkBox.setText('')

    def checkFunc(self):
        match self.boxFunc.currentText():
            case 'Добавить':
                self.checkTabel()
            case 'Обновить':
                self.checkTabel()
            case 'Удалить':
                self.label1.setVisible(True)
                self.label2.setVisible(False)
                self.label3.setVisible(False)
                self.label4.setVisible(False)
                self.label5.setVisible(False)
                self.label6.setVisible(False)

                self.input1.setVisible(True)
                self.input2.setVisible(False)
                self.input3.setVisible(False)
                self.input4.setVisible(False)
                self.input5.setVisible(False)
                self.input6.setVisible(False)



#TODO: РЕАЛИЗОВАТЬ insert
    def tryFunc(self):
        match self.boxFunc.currentText():
            case 'Добавить':
                match self.boxTabel.currentText():
                    case 'Книги':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.insertBooks(self.input1.text(), self.input2.text(),
                                                   self.checkBox.isChecked(), self.input4.text(), strin,
                                                   self.input6.text()):
                            self.answState.setText("Успешно!")
                        else:
                            self.answState.setText("Ошибка в вводимых данных!")
                    case 'Авторы':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.insertAuthors(self.input1.text(), self.input2.text(), self.input3.text(),
                                                   strin):
                            self.answState.setText("Успешно!")
                        else:
                            self.answState.setText("Ошибка в вводимых данных!")
                    case 'Формуляры':
                        pass
                    case 'Читательские билеты':
                        pass
                    case 'Работники':
                        pass
                    case 'Должности':
                        pass
            case 'Обновить':
                pass
            case 'Удалить':
                pass


    def checkTabel(self):
        match self.boxTabel.currentText():
            case 'Книги':
                self.label1.setVisible(True)
                self.label2.setVisible(True)
                self.label3.setVisible(True)
                self.label4.setVisible(True)
                self.label5.setVisible(True)
                self.label6.setVisible(True)

                self.input1.setVisible(True)
                self.input2.setVisible(True)
                self.input3.setVisible(False)
                self.input4.setVisible(True)
                self.input5.setVisible(False)
                self.input6.setVisible(True)

                self.checkBox.setVisible(True)
                self.date1.setVisible(False)
                self.date2.setVisible(True)
                self.date3.setVisible(False)

                self.label1.setText('ID Книги')
                self.label2.setText('Название книги')
                self.label3.setText('Наличие')
                self.label4.setText('Жанр')
                self.label5.setText('Дата публикации')
                self.label6.setText('ID Автора')

                self.boxFunc.setCurrentText('Добавить')
            case 'Авторы':
                self.label1.setVisible(True)
                self.label2.setVisible(True)
                self.label3.setVisible(True)
                self.label4.setVisible(True)
                self.label5.setVisible(False)
                self.label6.setVisible(False)

                self.input1.setVisible(True)
                self.input2.setVisible(True)
                self.input3.setVisible(True)
                self.input4.setVisible(False)
                self.input5.setVisible(False)
                self.input6.setVisible(False)

                self.checkBox.setVisible(False)
                self.date1.setVisible(True)
                self.date2.setVisible(False)
                self.date3.setVisible(False)

                self.label1.setText('ID Автора')
                self.label2.setText('Имя')
                self.label3.setText('Фамилия')
                self.label4.setText('Дата рождения')

                self.boxFunc.setCurrentText('Добавить')
            case 'Формуляры':
                self.label1.setVisible(True)
                self.label2.setVisible(True)
                self.label3.setVisible(True)
                self.label4.setVisible(True)
                self.label5.setVisible(True)
                self.label6.setVisible(True)

                self.input1.setVisible(True)
                self.input2.setVisible(True)
                self.input3.setVisible(True)
                self.input4.setVisible(True)
                self.input5.setVisible(True)
                self.input6.setVisible(True)

                self.checkBox.setVisible(False)
                self.date1.setVisible(True)
                self.date2.setVisible(True)
                self.date3.setVisible(False)

                self.label1.setText('Номер формуляра')
                self.label2.setText('ID Читательского билета')
                self.label3.setText('ID Рабочего')
                self.label4.setText('Дата выдачи')
                self.label5.setText('Дата возврата')
                self.label6.setText('Книги')

                self.boxFunc.setCurrentText('Добавить')
            case 'Работники':
                self.label1.setVisible(True)
                self.label2.setVisible(True)
                self.label3.setVisible(True)
                self.label4.setVisible(True)
                self.label5.setVisible(True)
                self.label6.setVisible(False)

                self.input1.setVisible(True)
                self.input2.setVisible(True)
                self.input3.setVisible(True)
                self.input4.setVisible(True)
                self.input5.setVisible(True)
                self.input6.setVisible(False)

                self.checkBox.setVisible(False)
                self.date1.setVisible(True)
                self.date2.setVisible(False)
                self.date3.setVisible(False)

                self.label1.setText('ID Работника')
                self.label2.setText('Имя')
                self.label3.setText('Фамилия')
                self.label4.setText('День рождения')
                self.label5.setText('Должность')

                self.boxFunc.setCurrentText('Добавить')
            case 'Должности':
                self.label1.setVisible(True)
                self.label2.setVisible(True)
                self.label3.setVisible(True)
                self.label4.setVisible(True)
                self.label5.setVisible(False)
                self.label6.setVisible(False)

                self.input1.setVisible(True)
                self.input2.setVisible(True)
                self.input3.setVisible(True)
                self.input4.setVisible(True)
                self.input5.setVisible(False)
                self.input6.setVisible(False)

                self.checkBox.setVisible(False)
                self.date1.setVisible(False)
                self.date2.setVisible(False)
                self.date3.setVisible(True)

                self.label1.setText('Должность')
                self.label2.setText('Зарплата')
                self.label3.setText('Дата принятия')
                self.label4.setText('Уровень допуска')

                self.boxFunc.setCurrentText('Добавить')
            case 'Читательские билеты':
                self.label1.setVisible(True)
                self.label2.setVisible(True)
                self.label3.setVisible(True)
                self.label4.setVisible(True)
                self.label5.setVisible(True)
                self.label6.setVisible(False)

                self.input1.setVisible(True)
                self.input2.setVisible(True)
                self.input3.setVisible(True)
                self.input4.setVisible(True)
                self.input5.setVisible(True)
                self.input6.setVisible(False)

                self.checkBox.setVisible(False)
                self.date1.setVisible(True)
                self.date2.setVisible(False)
                self.date3.setVisible(False)

                self.label1.setText('ID Читательских билетов')
                self.label2.setText('Имя')
                self.label3.setText('Фамилия')
                self.label4.setText('Дата рождения')
                self.label5.setText('Рейтинг')

                self.boxFunc.setCurrentText('Добавить')

    def setupUI(self):
        loadUi("Views\mainView\mainView.ui", self)
        self.tabWidget.setTabText(0, 'Профиль')
        self.tabWidget.setTabText(1, 'Таблицы')
        self.tabWidget.setTabText(2, 'Управление БД')

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
