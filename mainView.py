from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi


class mainView(QtWidgets.QMainWindow):

    def __int__(self):
        super(mainView, self).__init__()

    def setServer(self, server):
        self.server = server

    def setWidget(self, widget):
        self.widget = widget

    def setData(self, data):
        if data != []:
            self.data = data
            self.size = len(data)
            return True
        else:
            return False

    def loadWindow(self):
        loadUi("studio.ui", self)
        self.tabWidget.setTabText(0, 'Поиск по таблицам')
        self.tabWidget.setTabText(1, 'Работа с данными')
        self.statusbar.showMessage("Ателье, Лесневская Полина Сергеевна")
        self.loadTabTables()
        self.loadIUDTabels()

    def loadIUDTabels(self):
        # -- Кнопки --

        # -- Боксы
        self.tabelBox2.currentTextChanged.connect(self.changeLabels)
        fields = ['ID Клиента', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона']
        bools = [True, True, True, True, True, False, False, False, False, False, False, False]
        self.setVision(bools, fields)

    def changeLabels(self):
        match self.tabelBox2.currentText():
            case 'Клиенты':
                fields = ['ID Клиента', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона']
                bools = [True, True, True, True, True, False, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Детали':
                fields = ['ID Детали', 'Описание', 'Название', 'Дата создания']
                bools = [True, True, True, True, False, False, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Заказы':
                fields = ['ID Заказа', 'ID Портного', 'ID Модели', 'ID Требования', 'Номер пошива', 'ID Мерок',
                          'ID Клиента', 'Дата заказа', 'Стоимость', 'Дата выполнения', 'ID Стандарта', 'Описание']
                bools = [True, True, True, True, True, True, True, True, True, True, True, True]
                self.setVision(bools, fields)
            case 'Материалы':
                fields = ['ID Материала', 'ID Склада', 'Название материала', 'Состав', 'ID Типа материала']
                bools = [True, True, True, True, True, False, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Мерки':
                fields = ['ID Мерок', 'Грудь', 'Талия', 'Бедра', 'Руки', 'Ноги']
                bools = [True, True, True, True, True, True, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Модели':
                fields = ['ID Модели', 'ID Требования', 'Длина', 'Ширина']
                bools = [True, True, True, True, False, False, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Оборудование':
                fields = ['ID Оборудования', 'Название', 'Дата ввода в эксплуатацию']
                bools = [True, True, True, False, False, False, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Портные':
                fields = ['ID Портного', 'Фамилия', 'Имя', 'Отчество']
                bools = [True, True, True, True, False, False, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Пошивы моделей':
                fields = ['Номер пошива', 'ID Мерок', 'ID Детали', 'Дата пошива', 'ID Статуса', 'ID Материала', 'ID Типа материала', 'ID Склада', 'ID Оборудования']
                bools = [True, True, True, True, True, True, True, True, True, False, False, False]
                self.setVision(bools, fields)
            case 'Склады':
                fields = ['ID Склада', 'Площадь', 'Название склада']
                bools = [True, True, True, False, False, False, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Стандарты':
                fields =  ['ID Стандарта', 'Название', 'Документ', 'Описание']
                bools = [True, True, True, False, False, False, False, False, False, False, False, False]
                self.setVision(bools, fields)
            case 'Статусы':
                pass
            case 'Типы материалов':
                pass
            case 'Требования к моделям':
                pass
            case 'Требования клиентов':
                pass
            case 'Этапы пошива':
                pass

    def setVision(self, bools, fields):
        if len(fields) == 5:
            self.label1.setText(fields[0])
            self.label2.setText(fields[1])
            self.label3.setText(fields[2])
            self.label4.setText(fields[3])
            self.label5.setText(fields[4])
        elif len(fields) == 4:
            self.label1.setText(fields[0])
            self.label2.setText(fields[1])
            self.label3.setText(fields[2])
            self.label4.setText(fields[3])
        elif len(fields) == 12:
            self.label1.setText(fields[0])
            self.label2.setText(fields[1])
            self.label3.setText(fields[2])
            self.label4.setText(fields[3])
            self.label5.setText(fields[4])
            self.label6.setText(fields[5])
            self.label7.setText(fields[6])
            self.label8.setText(fields[7])
            self.label9.setText(fields[8])
            self.label10.setText(fields[9])
            self.label11.setText(fields[10])
            self.label12.setText(fields[11])
        elif len(fields) == 6:
            self.label1.setText(fields[0])
            self.label2.setText(fields[1])
            self.label3.setText(fields[2])
            self.label4.setText(fields[3])
            self.label5.setText(fields[4])
            self.label6.setText(fields[5])
        elif len(fields) == 3:
            self.label1.setText(fields[0])
            self.label2.setText(fields[1])
            self.label3.setText(fields[2])
        elif len(fields) == 9:
            self.label1.setText(fields[0])
            self.label2.setText(fields[1])
            self.label3.setText(fields[2])
            self.label4.setText(fields[3])
            self.label5.setText(fields[4])
            self.label6.setText(fields[5])
            self.label7.setText(fields[6])
            self.label8.setText(fields[7])
            self.label9.setText(fields[8])

        self.label1.setVisible(bools[0])
        self.input1.setVisible(bools[0])

        self.label2.setVisible(bools[1])
        self.input2.setVisible(bools[1])

        self.label3.setVisible(bools[2])
        self.input3.setVisible(bools[2])

        self.label4.setVisible(bools[3])
        self.input4.setVisible(bools[3])

        self.label5.setVisible(bools[4])
        self.input5.setVisible(bools[4])

        self.label6.setVisible(bools[5])
        self.input6.setVisible(bools[5])

        self.label7.setVisible(bools[6])
        self.input7.setVisible(bools[6])

        self.label8.setVisible(bools[7])
        self.input8.setVisible(bools[7])

        self.label9.setVisible(bools[8])
        self.input9.setVisible(bools[8])

        self.label10.setVisible(bools[9])
        self.input10.setVisible(bools[9])

        self.label11.setVisible(bools[10])
        self.input11.setVisible(bools[10])

        self.label12.setVisible(bools[11])
        self.input12.setVisible(bools[11])

    def loadTabTables(self):
        # -- Кнопки --
        self.searchBtn.clicked.connect(self.selectTabel)

    def selectTabel(self):
        match self.tabelBox.currentText():
            case 'Клиенты':
                self.setClientTabel()
            case 'Детали':
                self.setPartTabel()
            case 'Заказы':
                self.setOrderTabel()
            case 'Материалы':
                self.setMaterialTabel()
            case 'Мерки':
                self.setMeasurementTabel()
            case 'Модели':
                self.setModelTabel()
            case 'Оборудование':
                self.setDeviceTabel()
            case 'Портные':
                self.setTailorTabel()
            case 'Пошивы моделей':
                self.setModelSewingTabel()
            case 'Склады':
                self.setWarehouseTabel()
            case 'Стандарты':
                self.setStandartsTabel()
            case 'Статусы':
                self.setStarusTabel()
            case 'Типы материалов':
                self.setMaterialTypeTabel()
            case 'Требования к моделям':
                self.setModelDemandTabel()
            case 'Требования клиентов':
                self.setClientDemandTabel()
            case 'Этапы пошива':
                self.setSewingStageTabel()

    def setClientTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectClients(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(5)
            self.tabels.setHorizontalHeaderLabels(['ID Клиента','Фамилия','Имя','Отчество', 'Номер телефона'])
            self.field1.setText("Фамилия")
            self.field2.setText("Имя")
            self.statusbar.showMessage("Связь с таблицей 'Клиенты' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.tabels.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(row[4]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Клиенты'!")

    def setPartTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectParts(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(4)
            self.tabels.setHorizontalHeaderLabels(['ID Детали', 'Описание', 'Название', 'Дата создания'])
            self.field1.setText("Описание")
            self.field2.setText("Название")
            self.statusbar.showMessage("Связь с таблицей 'Детали' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%Y-%m-%d')))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Детали'!")

    def setOrderTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectOrders(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(12)
            self.tabels.setHorizontalHeaderLabels(['ID Заказа', 'ID Портного', 'ID Модели', 'ID Требования', 'Номер пошива', 'ID Мерок', 'ID Клиента', 'Дата заказа', 'Стоимость', 'Дата выполнения', 'ID Стандарта', 'Описание'])
            self.field1.setText("Стоимость")
            self.field2.setText("Описание")
            self.statusbar.showMessage("Связь с таблицей 'Заказы' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tabels.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tabels.setItem(tabelrow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                self.tabels.setItem(tabelrow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                self.tabels.setItem(tabelrow, 7, QtWidgets.QTableWidgetItem(row[7].strftime('%Y-%m-%d')))
                self.tabels.setItem(tabelrow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                self.tabels.setItem(tabelrow, 9, QtWidgets.QTableWidgetItem(row[9].strftime('%Y-%m-%d')))
                self.tabels.setItem(tabelrow, 10, QtWidgets.QTableWidgetItem(str(row[10])))
                self.tabels.setItem(tabelrow, 11, QtWidgets.QTableWidgetItem(row[11]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Заказы'!")

    def setMaterialTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectMaterials(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(5)
            self.tabels.setHorizontalHeaderLabels(['ID Материала', 'ID Склада', 'Название материала', 'Состав', 'ID Типа материала'])
            self.field1.setText("Название")
            self.field2.setText("Состав")
            self.statusbar.showMessage("Связь с таблицей 'Материалы' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.tabels.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Материалы'!")

    def setMeasurementTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectMeasurements(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(6)
            self.tabels.setHorizontalHeaderLabels(['ID Мерок', 'Грудь', 'Талия', 'Бедра', 'Руки', 'Ноги'])
            self.field1.setText("Грудь")
            self.field2.setText("Талия")
            self.statusbar.showMessage("Связь с таблицей 'Мерки' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.tabels.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tabels.setItem(tabelrow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Мерки'!")

    def setModelTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectModels(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(4)
            self.tabels.setHorizontalHeaderLabels(['ID Модели', 'ID Требования', 'Длина', 'Ширина'])
            self.field1.setText("Длина")
            self.field2.setText("Ширина")
            self.statusbar.showMessage("Связь с таблицей 'Модели' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Модели'!")

    def setDeviceTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectDevices(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(3)
            self.tabels.setHorizontalHeaderLabels(['ID Оборудования', 'Название', 'Дата ввода в эксплуатацию'])
            self.field1.setText("Название")
            self.field2.setText("Дата")
            self.statusbar.showMessage("Связь с таблицей 'Оборудование' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2].strftime('%Y-%m-%d')))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Оборудование'!")

    def setTailorTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectTailors(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(4)
            self.tabels.setHorizontalHeaderLabels(['ID Портного', 'Фамилия', 'Имя', 'Отчество'])
            self.field1.setText("Фамилия")
            self.field2.setText("Имя")
            self.statusbar.showMessage("Связь с таблицей 'Портные' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[2]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Портные'!")

    def setModelSewingTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectModelSewings(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(10)
            self.tabels.setHorizontalHeaderLabels(['Номер пошива', 'ID Мерок', 'ID Детали', 'Дата пошива', 'ID Статуса', 'ID Материала', 'ID Типа материала', 'ID Склада', 'ID Оборудования'])
            self.field1.setText("Дата")
            self.field2.setText("Статус")
            self.statusbar.showMessage("Связь с таблицей 'Пошивы моделей' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3].strftime('%Y-%m-%d')))
                self.tabels.setItem(tabelrow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.tabels.setItem(tabelrow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                self.tabels.setItem(tabelrow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                self.tabels.setItem(tabelrow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                self.tabels.setItem(tabelrow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                self.tabels.setItem(tabelrow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Пошивы моделей'!")

    def setWarehouseTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectWarehouses(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(3)
            self.tabels.setHorizontalHeaderLabels(['ID Склада', 'Площадь', 'Название склада'])
            self.field1.setText("Название")
            self.field2.setText("Площадь")
            self.statusbar.showMessage("Связь с таблицей 'Склады' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Склады'!")

    def setStandartsTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectStandarts(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(4)
            self.tabels.setHorizontalHeaderLabels(['ID Стандарта', 'Название', 'Документ', 'Описание'])
            self.field1.setText("Название")
            self.field2.setText("Документ")
            self.statusbar.showMessage("Связь с таблицей 'Стандарты' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Стандарты'!")

    def setStarusTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectStatuses(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(4)
            self.tabels.setHorizontalHeaderLabels(
                ['ID Статуса', 'Название', 'Дата', 'Описание'])
            self.field1.setText("Название")
            self.field2.setText("Описание")
            self.statusbar.showMessage("Связь с таблицей 'Статусы' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2].strftime('%Y-%m-%d')))
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Статусы'!")

    def setMaterialTypeTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectMaterialTypes(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(3)
            self.tabels.setHorizontalHeaderLabels(
                ['ID Типа материала', 'Название', 'Описание'])
            self.field1.setText("Название")
            self.field2.setText("Описание")
            self.statusbar.showMessage("Связь с таблицей 'Типы материала' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Типы материала'!")

    def setModelDemandTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectModelDemands(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(3)
            self.tabels.setHorizontalHeaderLabels(
                ['ID Требования', 'Название', 'Описание'])
            self.field1.setText("Название")
            self.field2.setText("Описание")
            self.statusbar.showMessage("Связь с таблицей 'Требования к моделям' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Требования к моделям'!")

    def setClientDemandTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectClientDemands(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(3)
            self.tabels.setHorizontalHeaderLabels(
                ['ID Требования', 'ID Клиента', 'Описание'])
            self.field1.setText("ID Клиента")
            self.field2.setText("Описание")
            self.statusbar.showMessage("Связь с таблицей 'Требования клиентов' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Требования клиентов'!")

    def setSewingStageTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectSewingStages(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(3)
            self.tabels.setHorizontalHeaderLabels(
                ['Номер этапа', 'Название', 'Описание'])
            self.field1.setText("Название")
            self.field2.setText("Описание")
            self.statusbar.showMessage("Связь с таблицей 'Этапы пошива' успешно установлена!")
            tabelrow = 0
            self.tabels.setRowCount(self.size)
            for row in self.data:
                self.tabels.setItem(tabelrow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabels.setItem(tabelrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabels.setItem(tabelrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Этапы пошива'!")