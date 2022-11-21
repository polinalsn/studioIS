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
        if Data != []:
            self.data = Data
            self.size = len(Data)
            return True
        else:
            return False

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
            QtGui.QFont('SansSerif', 14)
        )
        self.labelReaders.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.labelAddBook.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.labelChangeState.setFont(
            QtGui.QFont('SansSerif', 16)
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
        self.btnAddBook.setFont(
            QtGui.QFont('SansSerif', 14)
        )
        self.btnAddBook.clicked.connect(self.tryAdd)
        self.btnChangeState.setFont(
            QtGui.QFont('SansSerif', 14)
        )
        self.btnChangeState.clicked.connect(self.tryChange)

        #-- Настройка комбобоксов --
        self.boxTabel.currentTextChanged.connect(self.checkTabel)
        self.boxFunc.currentTextChanged.connect(self.checkFunc)
        self.comboBox.currentTextChanged.connect(self.changeSearchFields)

        # -- Настройка доп херни --
        self.calendarWidget.setFont(
            QtGui.QFont('SansSerif', 16)
        )
        self.date1.setFont(
            QtGui.QFont('SansSerif', 10)
        )
        self.date2.setFont(
            QtGui.QFont('SansSerif', 10)
        )
        self.checkBox.setFont(
            QtGui.QFont('SansSerif', 10)
        )
        self.date3.setFont(
            QtGui.QFont('SansSerif', 10)
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
        # -- Настройка таблицы дня --
        self.row = self.server.selectReaders()
        self.tableReaders.setItem(0, 0, QtWidgets.QTableWidgetItem(self.row[0][0]))
        self.tableReaders.setItem(0, 1, QtWidgets.QTableWidgetItem(self.row[0][1]))
        self.tableReaders.setFont(
            QtGui.QFont('SansSerif', 9)
        )

    def tryAdd(self):
        if (self.lineBookName.text() != '' and self.lineFormularId.text() != ''):
            self.server.addBook(self.lineBookName.text(), self.lineFormularId.text())

    def tryChange(self):
        if (self.lineBookId.text() != ''):
            self.server.changeState(self.lineBookId.text())

    def checkFunc(self):
        match self.boxFunc.currentText():
            case 'Добавить':
                self.setClassicVisible()
            case 'Обновить':
                self.setClassicVisible()
            case 'Удалить':
                self.setDeleteVisible()

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
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        date1 = self.date2.date()
                        year, month, day = date1.getDate()
                        strin1 = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.insertFormulars(self.input1.text(), self.input2.text(), self.input3.text(), strin
                                                       , strin1, self.input6.text()):
                            self.answState.setText("Успешно!")
                        else:
                            self.answState.setText("Ошибка в вводимых данных!")
                    case 'Читательские билеты':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.insertTickets(self.input1.text(), self.input2.text(), self.input3.text(),
                                                     strin, self.input5.text()):
                            self.answState.setText("Успешно!")
                        else:
                            self.answState.setText("Ошибка в вводимых данных!")
                    case 'Работники':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.insertWorkers(self.input1.text(), self.input2.text(), self.input3.text(),
                                                     strin, self.input5.text()):
                            self.answState.setText("Успешно!")
                        else:
                            self.answState.setText("Ошибка в вводимых данных!")
                    case 'Должности':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.insertPost(self.input1.text(), self.input2.text(), self.date3.text(),
                                                  self.input4.text()):
                            self.answState.setText("Успешно!")
                        else:
                            self.answState.setText("Ошибка в вводимых данных!")
            case 'Обновить':
                match self.boxTabel.currentText():
                    case 'Книги':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.updateBooks(self.input1.text(), self.input2.text(),
                                                   self.checkBox.isChecked(), self.input4.text(), strin,
                                                   self.input6.text()):
                            self.answState.setText("Данные обновлены!")
                        else:
                            self.answState.setText("Ошибка в новых данных!")
                    case 'Авторы':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.updateAuthors(self.input1.text(), self.input2.text(), self.input3.text(),
                                                     strin):
                            self.answState.setText("Данные обновлены!")
                        else:
                            self.answState.setText("Ошибка в новых данных!")
                    case 'Формуляры':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        date1 = self.date2.date()
                        year, month, day = date1.getDate()
                        strin1 = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.updateFormulars(self.input1.text(), self.input2.text(), self.input3.text(), strin
                                , strin1, self.input6.text()):
                            self.answState.setText("Данные обновлены!")
                        else:
                            self.answState.setText("Ошибка в новых данных!")
                    case 'Читательские билеты':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.updateTickets(self.input1.text(), self.input2.text(), self.input3.text(),
                                                     strin, self.input5.text()):
                            self.answState.setText("Данные обновлены!")
                        else:
                            self.answState.setText("Ошибка в новых данных!")
                    case 'Работники':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.updateWorkers(self.input1.text(), self.input2.text(), self.input3.text(),
                                                     strin, self.input5.text()):
                            self.answState.setText("Данные обновлены!")
                        else:
                            self.answState.setText("Ошибка в новых данных!")
                    case 'Должности':
                        date = self.date1.date()
                        year, month, day = date.getDate()
                        strin = str(year) + '-' + str(month) + '-' + str(day)
                        if self.server.updatePost(self.input1.text(), self.input2.text(), self.date3.text(),
                                                  self.input4.text()):
                            self.answState.setText("Данные обновлены!")
                        else:
                            self.answState.setText("Ошибка в новых данных!")
            case 'Удалить':
                match self.boxTabel.currentText():
                    case 'Книги':
                        if self.server.deleteBook(self.input1.text()):
                            self.answState.setText("Книга успешно удалена!")
                        else:
                            self.answState.setText("Книгу нельзя удалить!")
                    case 'Авторы':
                        if self.server.deleteAuthor(self.input1.text()):
                            self.answState.setText("Автор успешно удален!")
                        else:
                            self.answState.setText("Автора нельзя удалить!")
                    case 'Формуляры':
                        if self.server.deleteFormular(self.input1.text()):
                            self.answState.setText("Формуляр успешно удален!")
                        else:
                            self.answState.setText("Формуляр нельзя удалить!")
                    case 'Читательские билеты':
                        if self.server.deleteTicket(self.input1.text()):
                            self.answState.setText("Читательский билет успешно удален!")
                        else:
                            self.answState.setText("Читательский билет нельзя удалить!")
                    case 'Работники':
                        if self.server.deleteWorker(self.input1.text()):
                            self.answState.setText("Работник успешно удален!")
                        else:
                            self.answState.setText("Работника нельзя удалить!")
                    case 'Должности':
                        if self.server.deletePost(self.input1.text()):
                            self.answState.setText("Должность успешна удалена!")
                        else:
                            self.answState.setText("Должность нельзя удалить!")

    def checkTabel(self):
        self.boxFunc.setCurrentText('Добавить')
        self.setClassicVisible()

    def setClassicVisible(self):
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
                self.input4.setVisible(False)
                self.input5.setVisible(False)
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
                self.input4.setVisible(False)
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

            case 'Должности':
                self.label1.setVisible(True)
                self.label2.setVisible(True)
                self.label3.setVisible(True)
                self.label4.setVisible(True)
                self.label5.setVisible(False)
                self.label6.setVisible(False)

                self.input1.setVisible(True)
                self.input2.setVisible(True)
                self.input3.setVisible(False)
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
                self.input4.setVisible(False)
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

    def setDeleteVisible(self):
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

        self.date1.setVisible(False)
        self.date2.setVisible(False)
        self.date3.setVisible(False)
        self.checkBox.setVisible(False)

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

    def changeSearchFields(self):
        match self.comboBox.currentText():
            case 'Книги':
                self.search1.setVisible(True)
                self.search2.setVisible(True)
                self.search3.setVisible(True)
                self.search4.setVisible(True)
                self.search5.setVisible(True)
            case 'Авторы':
                self.search1.setVisible(True)
                self.search2.setVisible(True)
                self.search3.setVisible(True)
                self.search4.setVisible(False)
                self.search5.setVisible(False)
            case 'Формуляры':
                self.search1.setVisible(True)
                self.search2.setVisible(True)
                self.search3.setVisible(True)
                self.search4.setVisible(True)
                self.search5.setVisible(True)
            case 'Работники библиотеки':
                self.search1.setVisible(True)
                self.search2.setVisible(True)
                self.search3.setVisible(True)
                self.search4.setVisible(True)
                self.search5.setVisible(False)
            case 'Должности':
                self.search1.setVisible(True)
                self.search2.setVisible(True)
                self.search3.setVisible(True)
                self.search4.setVisible(False)
                self.search5.setVisible(False)
            case 'Билеты':
                self.search1.setVisible(True)
                self.search2.setVisible(True)
                self.search3.setVisible(True)
                self.search4.setVisible(True)
                self.search5.setVisible(False)


    def setupBookTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(6)
        self.tabel.setHorizontalHeaderLabels(
            ['ID Книги', 'Название книги', 'Статус', 'Жанр', 'Год издания', 'ID Автора'])
        if (self.setData(self.server.selectBooks(self.search1.text(), self.search2.text(), self.search3.text(),
                                                 self.search4.text(), self.search5.text()))):
            self.searchRes.setText('Ок')
            tabelrow = 0
            self.tabel.setRowCount(self.size)
            for row in self.data:
                self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.tabel.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(row[4].strftime('%Y/%m/%d')))
                self.tabel.setItem(tabelrow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                tabelrow += 1
        else:
            self.searchRes.setText('Ошибка')
            self.tabel.clear()

    def setupAuthorTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(4)
        self.tabel.setHorizontalHeaderLabels(['ID Автора', 'Имя', 'Фамилия', 'Дата рождения'])
        if (self.setData(self.server.selectAuthors(self.search1.text(), self.search2.text(), self.search3.text()))):
            self.searchRes.setText('Ок')
            tabelrow = 0
            self.tabel.setRowCount(self.size)
            for row in self.data:
                self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%Y/%m/%d')))
                tabelrow += 1
        else:
            self.searchRes.setText('Ошибка')
            self.tabel.clear()

    def setupFormularTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(6)
        self.tabel.setHorizontalHeaderLabels(
            ['ID Формуляра', 'ID Билета', 'ID Рабочего', 'Дата выдачи', 'Дата возврата', 'Книги'])
        if (self.setData(self.server.selectFormulars(self.search1.text(), self.search2.text(), self.search3.text(),
                                                     self.search4.text(), self.search5.text()))):
            self.searchRes.setText("Ок")
            tabelrow = 0
            self.tabel.setRowCount(self.size)
            for row in self.data:
                self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%Y/%m/%d')))
                self.tabel.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(row[4].strftime('%Y/%m/%d')))
                self.tabel.setItem(tabelrow, 5, QtWidgets.QTableWidgetItem(row[5]))
                tabelrow += 1
        else:
            self.searchRes.setText('Ошибка')
            self.tabel.clear()

    def setupWorkerTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(5)
        self.tabel.setHorizontalHeaderLabels(['ID Рабочего', 'Имя', 'Фамилия', 'Дата рождения', 'Должность'])
        if (self.setData(self.server.selectLibraryWorkers(self.search1.text(), self.search2.text(), self.search3.text(),
                                                          self.search4.text()))):
            self.searchRes.setText('Ок')
            tabelrow = 0
            self.tabel.setRowCount(self.size)
            for row in self.data:
                self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%Y/%m/%d')))
                self.tabel.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(row[4]))
                tabelrow += 1
        else:
            self.searchRes.setText('Ошибка')
            self.tabel.clear()

    def setupPostTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(4)
        self.tabel.setHorizontalHeaderLabels(['Название должности', 'Зарплата', 'Дата найма', 'Уровень допуска'])
        if (self.setData(self.server.selectPosts(self.search1.text(), self.search2.text(), self.search3.text()))):
            self.searchRes.setText('Ок')
            tabelrow = 0
            self.tabel.setRowCount(self.size)
            for row in self.data:
                self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2].strftime('%Y/%m/%d')))
                self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                tabelrow += 1
        else:
            self.searchRes.setText('Ошибка')
            self.tabel.clear( )


    def setupTicketTabel(self):
        self.tabel.clear()
        self.tabel.setColumnCount(5)
        self.tabel.setHorizontalHeaderLabels(['ID Читательского билета', 'Имя', 'Фамилия', 'Дата рождениия', 'Рейтинг'])
        if (self.setData(self.server.selectTickets(self.search1.text(), self.search2.text(), self.search3.text(),
                                                   self.search4.text()))):
            self.searchRes.setText('Ок')
            tabelrow = 0
            self.tabel.setRowCount(self.size)
            for row in self.data:
                self.tabel.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabel.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabel.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabel.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%Y/%m/%d')))
                self.tabel.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                tabelrow += 1
        else:
            self.searchRes.setText('Ошибка')
            self.tabel.clear()
