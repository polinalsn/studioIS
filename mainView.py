from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi


class mainView(QtWidgets.QMainWindow):

    def __int__(self):
        super(mainView, self).__init__()

    def setServer(self, server):
        self.server = server

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
        self.tabWidget.setTabText(2, 'Расчетные функции')
        self.tabWidget.setTabText(3, 'Произвольный запрос')
        self.statusbar.showMessage("Ателье, Лесневская Полина Сергеевна")
        self.loadTabTables()
        self.loadTabIUD()
        self.loadTabExtra()
        self.loadTabAdmin()

    def loadTabAdmin(self):
        # -- Кнопки --
        self.selectBtn.clicked.connect(self.freeExec)
        self.tabelBox3.currentTextChanged.connect(self.manage)

    def manage(self):
        match self.tabelBox3.currentText():
            case 'Клиенты':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Требования клиентов', 'Заказы'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_client'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_client', 'surname', 'name', 'middle_name', 'phone_number'])
            case 'Детали':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Пошивы моделей'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_part'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_part', 'description', 'part_name', 'creation_date'])
            case 'Заказы':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Клиенты', 'Мерки', 'Требования к моделям', 'Пошивы моделей', 'Модели', 'Стандарты',
                                         'Портные'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_client', 'id_measurements', 'id_demand', 'ms_number', 'id_model', 'id_standart',
                                     'id_tailor'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_order', 'id_tailor', 'id_model', 'id_demand', 'ms_number', 'id_measurements',
                                        'id_client', 'order_date', 'order_amount', 'completion_date', 'id_standart',
                                        'description'])
            case 'Материалы':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Типы материалов', 'Пошивы моделей', 'Склады'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_material_type', 'id_material', 'id_warehouse'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_material', 'id_warehouse', 'material_name', 'composition', 'id_material_type'])
            case 'Мерки':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Пошивы моделей', 'Заказы'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_measurements'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_measurements', 'chest', 'waist', 'hip', 'hands', 'legs'])
            case 'Модели':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Требования к моделям', 'Заказы'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_demand', 'id_model'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_model', 'id_demand', 'length', 'width'])
            case 'Оборудование':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Пошивы моделей'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_device'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_device', 'device_name', 'using_start_date'])
            case 'Портные':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Заказы'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_tailor'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_tailor', 'surname', 'name', 'middle_name'])
            case 'Пошивы моделей':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Оборудование', 'Типы материалов', 'Материалы', 'Мерки', 'Заказы', 'Детали',
                                         'Этапы пошива', 'Статусы', 'Склады'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_device', 'id_material_type', 'id_material', 'id_measurements', 'ms_number',
                                     'id_part', 'stage_num', 'id_status', 'id_warehouse'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['ms_number', 'id_measurements', 'id_part', 'sewing_date', 'id_status',
                                        'id_material', 'id_material_type', 'id_warehouse', 'stage_num', 'id_device'])
            case 'Склады':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Материалы', 'Пошивы моделей'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_warehouse'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_warehouse', 'square', 'warehouse_name'])
            case 'Стандарты':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Заказы'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_standart'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_standart', 'standart_name', 'standart_docs', 'description'])
            case 'Статусы':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Пошивы моделей'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_status'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_status', 'status_name', 'status_date', 'description'])
            case 'Типы материалов':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Материалы', 'Пошивы моделей'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_material_type'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_material_type', 'material_name', 'description'])
            case 'Требования к моделям':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Модели', 'Заказы'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_demand'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_demand', 'demand_name', 'description'])
            case 'Требования клиентов':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Клиенты'])
                self.boxFK.clear()
                self.boxFK.addItems(['id_client'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['id_demand', 'id_client', 'description'])
            case 'Этапы пошива':
                self.tabelBox4.clear()
                self.tabelBox4.addItems(['Пошивы моделей'])
                self.boxFK.clear()
                self.boxFK.addItems(['stage_num'])
                self.boxOrder.clear()
                self.boxOrder.addItems(['stage_num', 'stage_status', 'stage_description'])

    def getTabel3(self):
        match self.tabelBox3.currentText():
            case 'Клиенты':
                return 'Client'
            case 'Детали':
                return 'Part'
            case 'Заказы':
                return 'Order'
            case 'Материалы':
                return 'Material'
            case 'Мерки':
                return 'Measurements'
            case 'Модели':
                return 'Model'
            case 'Оборудование':
                return 'Devices'
            case 'Портные':
                return 'Tailor'
            case 'Пошивы моделей':
                return 'Model_sewing'
            case 'Склады':
                return 'Warehouse'
            case 'Стандарты':
                return 'Standarts'
            case 'Статусы':
                return 'Status'
            case 'Типы материалов':
                return 'Material_type'
            case 'Требования к моделям':
                return 'Model_demand'
            case 'Требования клиентов':
                return 'Client_demand'
            case 'Этапы пошива':
                return 'Sewing_stage'

    def getTabel4(self):
        match self.tabelBox4.currentText():
            case 'Клиенты':
                return 'Client'
            case 'Детали':
                return 'Part'
            case 'Заказы':
                return 'Order'
            case 'Материалы':
                return 'Material'
            case 'Мерки':
                return 'Measurements'
            case 'Модели':
                return 'Model'
            case 'Оборудование':
                return 'Devices'
            case 'Портные':
                return 'Tailor'
            case 'Пошивы моделей':
                return 'Model_sewing'
            case 'Склады':
                return 'Warehouse'
            case 'Стандарты':
                return 'Standarts'
            case 'Статусы':
                return 'Status'
            case 'Типы материалов':
                return 'Material_type'
            case 'Требования к моделям':
                return 'Model_demand'
            case 'Требования клиентов':
                return 'Client_demand'
            case 'Этапы пошива':
                return 'Sewing_stage'

    def freeExec(self):
        self.tabelFree.clear()
        data = []
        match self.selectBox.currentText():
            case 'SELECT':
                data = self.server.selectFree(self.lineFree.text(), self.getTabel3())
            case 'SELECT INNER JOIN':
                data = self.server.selectIJ(self.lineFree.text(), self.getTabel3(), self.getTabel4(), self.boxFK.currentText())
            case 'SELECT GROUP BY':
                data = self.server.selectGB(self.lineFree.text(), self.getTabel3(), self.boxOrder.currentText())
        try:
            self.tabelFree.setColumnCount(len(data[0]))
            self.tabelFree.setRowCount(len(data))
            for row in range(len(data)):
                for column in range(len(data[0])):
                    self.tabelFree.setItem(row, column, QtWidgets.QTableWidgetItem(str(data[row][column])))
            self.statusbar.showMessage('Успешно выполнен SELECT')
        except Exception as e:
            print(e)
            self.statusbar.showMessage('Ошибка при попытке выполнить SELECT')

    def loadTabExtra(self):
        # -- Кнопки --
        self.exBtn1.clicked.connect(self.avgChestHeight)
        self.exBtn2.clicked.connect(self.orderSum)
        self.exBtn3.clicked.connect(self.calcBackWidth)
        self.exBtn4.clicked.connect(self.calcChestHeight)
        self.exBtn5.clicked.connect(self.calcChestWeightWomen)
        self.exBtn6.clicked.connect(self.getS)
        self.exBtn7.clicked.connect(self.giveUseDays)
        self.exBtn8.clicked.connect(self.newStage)

    def avgChestHeight(self):
        self.statusbar.showMessage('Средняя высота груди = ' + str(self.server.avgChestHeight()))

    def orderSum(self):
        self.statusbar.showMessage('Количество активных заказов - ' + str(self.server.orderSum()))

    def calcBackWidth(self):
        if self.exLine1.text() != '':
           self.statusbar.showMessage(self.server.calcBackWidth(self.exLine1.text()))

    def calcChestHeight(self):
        if self.exLine2.text() != '':
            self.statusbar.showMessage(self.server.calcChestHeight(self.exLine2.text()))

    def calcChestWeightWomen(self):
        if self.exLine3.text() != '':
            self.statusbar.showMessage(self.server.calcChestWeightWomen(self.exLine3.text()))

    def getS(self):
        if self.exLine4.text()  != '' and self.exLine5.text():
            self.statusbar.showMessage(self.server.getS(self.exLine4.text(), self.exLine5.text()))

    def giveUseDays(self):
        if self.exLine6.text() != '':
            self.statusbar.showMessage(self.server.giveUseDays(self.exLine6.text()))

    def newStage(self):
        if self.exLine7.text() != '' and self.exLine8.text() != '':
            self.statusbar.showMessage(self.server.newStage(self.exLine7.text(), self.exLine8.text()))

    def loadTabIUD(self):
        # -- Кнопки --
        self.execBtn.clicked.connect(self.execQueue)
        # -- Боксы
        self.tabelBox2.currentTextChanged.connect(self.changeLabels)
        self.comBox.currentTextChanged.connect(self.changeLabelsDelete)
        fields = ['ID Клиента', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона']
        bools = [True, True, True, True, True, False, False, False, False, False, False, False]
        self.setVision(bools, fields)

    def changeLabels(self):
        if self.comBox.currentText() == 'Добавить' or self.comBox.currentText() == 'Обновить':
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
                    fields = ['Номер пошива', 'ID Мерок', 'ID Детали', 'Дата пошива', 'ID Статуса', 'ID Материала',
                              'ID Типа материала', 'ID Склада', 'ID Этапа', 'ID Оборудования']
                    bools = [True, True, True, True, True, True, True, True, True, True, False, False]
                    self.setVision(bools, fields)
                case 'Склады':
                    fields = ['ID Склада', 'Площадь', 'Название склада']
                    bools = [True, True, True, False, False, False, False, False, False, False, False, False]
                    self.setVision(bools, fields)
                case 'Стандарты':
                    fields = ['ID Стандарта', 'Название', 'Документ', 'Описание']
                    bools = [True, True, True, True, False, False, False, False, False, False, False, False]
                    self.setVision(bools, fields)
                case 'Статусы':
                    fields = ['ID Статуса', 'Название', 'Дата', 'Описание']
                    bools = [True, True, True, True, False, False, False, False, False, False, False, False]
                    self.setVision(bools, fields)
                case 'Типы материалов':
                    fields = ['ID Типа материала', 'Название', 'Описание']
                    bools = [True, True, True, False, False, False, False, False, False, False, False, False]
                    self.setVision(bools, fields)
                case 'Требования к моделям':
                    fields = ['ID Требования', 'Название', 'Описание']
                    bools = [True, True, True, False, False, False, False, False, False, False, False, False]
                    self.setVision(bools, fields)
                case 'Требования клиентов':
                    fields = ['ID Требования', 'ID Клиента', 'Описание']
                    bools = [True, True, True, False, False, False, False, False, False, False, False, False]
                    self.setVision(bools, fields)
                case 'Этапы пошива':
                    fields = ['Номер этапа', 'Название', 'Описание']
                    bools = [True, True, True, False, False, False, False, False, False, False, False, False]
                    self.setVision(bools, fields)
        else:
            self.changeLabelsDelete()

    def changeLabelsDelete(self):
        if self.comBox.currentText() == "Удалить":
            fields = ['ID ']
            bools = [True, False, False, False, False, False, False, False, False, False, False, False]
            self.setVision(bools, fields)
        elif self.comBox.currentText() == 'Добавить' or self.comBox.currentText() == 'Обновить':
            self.changeLabels()

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
        elif len(fields) == 1:
            self.label1.setText(fields[0] + self.tabelBox2.currentText())
        elif len(fields) == 10:
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

        self.input1.setText('')
        self.input2.setText('')
        self.input3.setText('')
        self.input4.setText('')
        self.input5.setText('')
        self.input6.setText('')
        self.input7.setText('')
        self.input8.setText('')
        self.input9.setText('')
        self.input10.setText('')
        self.input11.setText('')
        self.input12.setText('')

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

    def execQueue(self):
        match self.comBox.currentText():
            case 'Добавить':
                match self.tabelBox2.currentText():
                    case 'Клиенты':
                        if (self.server.insert("Client", '(id_client, surname, name, middle_name, phone_number)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}', '{self.input5.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Клиенты")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Клиенты")
                    case 'Детали':
                        if (self.server.insert("Part", '(id_part, description, part_name, creation_date)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Детали")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Детали")
                    case 'Заказы':
                        if (self.server.insert("Order", '(id_order, id_tailor, id_model, id_demand, ms_number, '
                                                        'id_measurements, id_client, order_date, order_amount, '
                                                        'completion_date, id_standart, description)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}', '{self.input5.text()}', '{self.input6.text()}',"
                                               f"'{self.input7.text()}', '{self.input8.text()}', '{self.input9.text()}',"
                                               f"'{self.input10.text()}', '{self.input11.text()}', '{self.input12.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Заказы")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Заказы")
                    case 'Материалы':
                        if (self.server.insert("Material", '(id_material, id_warehouse, material_name, composition,'
                                                           'id_material_type)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}', '{self.input5.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Материалы")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Материалы")
                    case 'Мерки':
                        if (self.server.insert("Measurements", '(id_measurements, chest, waist, hip, hands, legs)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}', '{self.input5.text()}', '{self.input6.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Мерки")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Мерки")
                    case 'Модели':
                        if (self.server.insert("Model", '(id_model, id_demand, length, width)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Модели")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Модели")
                    case 'Оборудование':
                        if (self.server.insert("Devices", '(id_device, device_name, using_start_date)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Оборудование")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Оборудование")
                    case 'Портные':
                        if (self.server.insert("Tailor", '(id_tailor, surname, name, middle_name)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Портные")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Портные")
                    case 'Пошивы моделей':
                        if (self.server.insert("Model_sewing", '(ms_number, id_measurements, id_part, sewing_date, '
                                                               'id_status, id_material, id_material_type, id_warehouse, '
                                                               'stage_num, id_device)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}', '{self.input5.text()}', '{self.input6.text()}',"
                                               f"'{self.input7.text()}', '{self.input8.text()}', '{self.input9.text()}',"
                                               f"'{self.input10.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Пошивы моделей")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Пошивы моделей")
                    case 'Склады':
                        if (self.server.insert("Warehouse", '(id_warehouse, square, warehouse_name)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Склады")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Склады")
                    case 'Стандарты':
                        if (self.server.insert("Standarts", '(id_standart, standart_name, standart_docs, description)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Стандарты")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Стандарты")
                    case 'Статусы':
                        if (self.server.insert("Status", '(id_status, status_name, status_date, description)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}',"
                                               f"'{self.input4.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Статусы")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Статусы")
                    case 'Типы материалов':
                        if (self.server.insert("Material_type", '(id_material_type, material_name, description)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Типы материалов")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Типы материалов")
                    case 'Требования к моделям':
                        if (self.server.insert("Model_demand", '(id_demand, demand_name, description)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Требования к моделям")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Требования к моделям")
                    case 'Требования клиентов':
                        if (self.server.insert("Client_demand", '(id_demand, id_client, description)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Требования клиентов")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Требования клиентов")
                    case 'Этапы пошива':
                        if (self.server.insert("Sewing_stage", '(stage_num, stage_status, stage_description)',
                                               f"('{self.input1.text()}', '{self.input2.text()}', '{self.input3.text()}')")):
                            self.statusbar.showMessage("Данные добавлены в таблицу Этапы пошива")
                        else:
                            self.statusbar.showMessage("Данные не добавлены в таблицу Этапы пошива")
            case 'Обновить':
                match self.tabelBox2.currentText():
                    case 'Клиенты':
                        if self.server.update("Client",
                                              f"surname='{self.input2.text()}', name='{self.input3.text()}', "
                                              f"middle_name='{self.input4.text()}', phone_number='{self.input5.text()}'"
                                              f" WHERE id_client='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Клиенты обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Клиенты не обновлены")
                    case 'Детали':
                        if self.server.update("Part",
                                              f"description='{self.input2.text()}', part_name='{self.input3.text()}', "
                                              f"creation_date='{self.input4.text()}' WHERE "
                                              f"id_part='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Детали обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Детали не обновлены")
                    case 'Заказы':
                        if self.server.update("Order",
                                              f"id_tailor='{self.input2.text()}', id_model='{self.input3.text()}', "
                                              f"id_demand='{self.input4.text()}', ms_number='{self.input5.text()}', "
                                              f"id_measurements='{self.input6.text()}', id_client='{self.input7.text()}', "
                                              f"order_date='{self.input8.text()}', order_amount='{self.input9.text()}', "
                                              f"completion_date='{self.input10.text()}', id_standart='{self.input11.text()}', "
                                              f"description='{self.input12.text()}' WHERE id_order='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Заказы обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Заказы не обновлены")
                    case 'Материалы':
                        if self.server.update("Material",
                                              f"id_warehouse='{self.input2.text()}', material_name='{self.input3.text()}', "
                                              f"composition='{self.input4.text()}', id_material_type='{self.input5.text()}' "
                                              f"WHERE id_material='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Материалы обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Материалы не обновлены")
                    case 'Мерки':
                        if self.server.update("Measurements",
                                              f"chest='{self.input2.text()}', waist='{self.input3.text()}', "
                                              f"hip='{self.input4.text()}', hands='{self.input5.text()}', "
                                              f"legs='{self.input6.text()}' WHERE id_measurements='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Мерки обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Мерки не обновлены")
                    case 'Модели':
                        if (
                        self.server.update("Model",
                                           f"id_demand='{self.input2.text()}', length='{self.input3.text()}', "
                                           f"width='{self.input3.text()}' WHERE id_model='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные в таблице Модели обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Модели не обновлены")
                    case 'Оборудование':
                        if self.server.update("Devices",
                                              f"device_name='{self.input2.text()}', using_start_date='{self.input3.text()}' "
                                              f"WHERE id_device='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Оборудование обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Оборудование не обноввлены")
                    case 'Портные':
                        if (
                        self.server.update("Tailor",
                                           f"surname='{self.input2.text()}', name='{self.input3.text()}', "
                                           f"middle_name='{self.input4.text()}' WHERE id_tailor='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные в таблице Портные обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Портные не обновлены")
                    case 'Пошивы моделей':
                        if self.server.update("Model_sewing",
                                              f"id_measurements='{self.input2.text()}', id_part='{self.input3.text()}', "
                                              f"sewing_date='{self.input4.text()}', id_status='{self.input5.text()}', "
                                              f"id_material='{self.input6.text()}', id_material_type='{self.input7.text()}', "
                                              f"id_warehouse='{self.input8.text()}', stage_num='{self.input9.text()}', "
                                              f"id_device='{self.input10.text()}' WHERE ms_number='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Пошивы моделей обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Пошивы моделей не обновлены")
                    case 'Склады':
                        if (self.server.update("Warehouse",
                                               f"square='{self.input2.text()}', warehouse_name='{self.input3.text()}' "
                                               f"WHERE id_warehouse='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные в таблице Склады обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Склады не обновлены")
                    case 'Стандарты':
                        if (self.server.update("Standarts",
                                               f"standart_name='{self.input2.text()}', standart_docs='{self.input3.text()}', "
                                               f"description='{self.input4.text()}' WHERE id_standart='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные в таблице Стандарты обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Стандарты не обновлены")
                    case 'Статусы':
                        if (self.server.update("Status",
                                               f"status_name='{self.input2.text()}', status_date='{self.input3.text()}', "
                                               f"description='{self.input4.text()}' WHERE id_status='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные в таблице Статусы обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Статусы не обновлены")
                    case 'Типы материалов':
                        if self.server.update("Material_type",
                                              f"material_name='{self.input2.text()}', description='{self.input3.text()}' "
                                              f"WHERE id_material_type='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Типы материалов обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Типы материалов не обновлены")
                    case 'Требования к моделям':
                        if self.server.update("Model_demand",
                                              f"demand_name='{self.input2.text()}', description='{self.input3.text()}' "
                                              f"WHERE id_demand='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные в таблице Требования к моделям обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Требования к моделям не обновлены")
                    case 'Требования клиентов':
                        if (self.server.update("Client_demand",
                                               f"id_client='{self.input2.text()}', description='{self.input3.text()}' "
                                               f"WHERE id_demand='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные в таблице Требования клиентов обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Требования клиентов не обноввлены")
                    case 'Этапы пошива':
                        if (self.server.update("Sewing_stage",
                                               f"stage_status='{self.input2.text()}', stage_description='{self.input3.text()}' "
                                               f"WHERE stage_num='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные в таблице Этапы пошива обновлены")
                        else:
                            self.statusbar.showMessage("Данные в таблице Этапы пошива не обновлены")
            case 'Удалить':
                match self.tabelBox2.currentText():
                    case 'Клиенты':
                        if self.server.delete("Client", f"id_client='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Клиенты удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Клиенты не удалены")
                    case 'Детали':
                        if self.server.delete("Part", f"id_part='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Детали удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Детали не удалены")
                    case 'Заказы':
                        if self.server.delete("Order", f"id_order='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Заказы удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Заказы не удалены")
                    case 'Материалы':
                        if self.server.delete("Material", f"id_material='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Материалы удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Материалы не удалены")
                    case 'Мерки':
                        if self.server.delete("Measurements", f"id_measurements='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Мерки удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Мерки не удалены")
                    case 'Модели':
                        if (self.server.delete("Model", f"id_model='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные из таблицы Модели удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Модели не удалены")
                    case 'Оборудование':
                        if self.server.delete("Devices", f"id_device='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Оборудование удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Оборудование не удалены")
                    case 'Портные':
                        if (self.server.delete("Tailor", f"id_tailor='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные из таблицы Портные удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Портные не удалены")
                    case 'Пошивы моделей':
                        if self.server.delete("Model_sewing", f"ms_number='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Пошивы моделей удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Пошивы моделей не удалены")
                    case 'Склады':
                        if (self.server.delete("Warehouse", f"id_warehouse='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные из таблицы Склады удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Склады не удалены")
                    case 'Стандарты':
                        if (self.server.delete("Standarts", f"id_standart='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные из таблицы Стандарты удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Стандарты не удалены")
                    case 'Статусы':
                        if (self.server.delete("Status", f"id_status='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные из таблицы Статусы удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Статусы не удалены")
                    case 'Типы материалов':
                        if self.server.delete("Material_type", f"id_material_type='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Типы материалов удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Типы материалов не удалены")
                    case 'Требования к моделям':
                        if self.server.delete("Model_demand", f"id_demand='{self.input1.text()}'"):
                            self.statusbar.showMessage("Данные из таблицы Требования к моделям удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Требования к моделям не удалены")
                    case 'Требования клиентов':
                        if (self.server.delete("Client_demand", f"id_demand='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные из таблицы Требования клиентов удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Требования клиентов не удалены")
                    case 'Этапы пошива':
                        if (self.server.delete("Sewing_stage", f"stage_num='{self.input1.text()}'")):
                            self.statusbar.showMessage("Данные из таблицы Этапы пошива удалены")
                        else:
                            self.statusbar.showMessage("Данные из таблицы Этапы пошива не удалены")

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
                self.setStatusTabel()
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
            self.tabels.setHorizontalHeaderLabels(['ID Клиента', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
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
            self.tabels.setHorizontalHeaderLabels(
                ['ID Заказа', 'ID Портного', 'ID Модели', 'ID Требования', 'Номер пошива', 'ID Мерок', 'ID Клиента',
                 'Дата заказа', 'Стоимость', 'Дата выполнения', 'ID Стандарта', 'Описание'])
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
            self.tabels.setHorizontalHeaderLabels(
                ['ID Материала', 'ID Склада', 'Название материала', 'Состав', 'ID Типа материала'])
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
                self.tabels.setItem(tabelrow, 3, QtWidgets.QTableWidgetItem(row[3]))
                tabelrow += 1
        else:
            self.statusbar.showMessage("Не удалось подключить таблицу 'Портные'!")

    def setModelSewingTabel(self):
        self.tabels.clear()
        if (self.setData(self.server.selectModelSewings(self.line1.text(), self.line2.text()))):
            self.tabels.setColumnCount(10)
            self.tabels.setHorizontalHeaderLabels(
                ['Номер пошива', 'ID Мерок', 'ID Детали', 'Дата пошива', 'ID Статуса', 'ID Материала',
                 'ID Типа материала', 'ID Склада', 'Номер этапа', 'ID Оборудования'])
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

    def setStatusTabel(self):
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
            self.tabels.setHorizontalHeaderLabels(['ID Типа материала', 'Название', 'Описание'])
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
            self.tabels.setHorizontalHeaderLabels(['ID Требования', 'ID Клиента', 'Описание'])
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
            self.tabels.setHorizontalHeaderLabels(['Номер этапа', 'Название', 'Описание'])
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
