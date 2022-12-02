from config import host, user, password, dbname
import psycopg2


class Server:
    """
    Класс Server устанавливает подключение к базе данных и позволяет получать результаты SQL-запросов
    """
    def connectDB(self):
        """
        ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ

        Возвращает: Экземпляр класса при успешном подключении и None при неуспешном
        """
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                dbname=dbname
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('[INFO] Соединение установлено')
        except Exception as e:
            print('[INFO] Ошибка во время подключения к базе данных', e)
        return self.connection

    def close(self):
        """Закрытие соединения"""
        if self.connection:
            self.connection.close()
            print('[ИНФО] Соединение с базой данных остановлено')

    def selectClients(self, surname, name):
        db = 'public."Client"'
        line1 = surname.lower()
        line2 = name.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(surname) LIKE '%{line1}%' and LOWER(name) LIKE '%{line2}%' ORDER BY id_client;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectParts(self, description, part_name):
        db = 'public."Part"'
        line1 = description.lower()
        line2 = part_name.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(description) LIKE '%{line1}%' and LOWER(part_name) LIKE '%{line2}%' ORDER BY id_part;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectOrders(self, order_amound, description):
        db = 'public."Order"'
        if order_amound != '':
            line1 = f"and order_amount = {order_amound}"
        else:
            line1 = ''
        line2 = description.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(description) LIKE '%{line2}%' {line1} ORDER BY id_order;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectMaterials(self, material_name, composition):
        db = 'public."Material"'
        line1 = material_name.lower()
        line2 = composition.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(material_name) LIKE '%{line1}%' and LOWER(composition) LIKE '%{line2}%' ORDER BY id_material;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectMeasurements(self, chest, waist):
        db = 'public."Measurements"'
        if chest != '':
            line1 = f"WHERE chest = {chest}"
        else:
            line1 = ''
        if waist != '' and line1 == '':
            line2 = f"WHERE waist = {waist}"
        elif waist != '' and line1 != '':
            line2 = f"and waist = {waist}"
        else:
            line2 = ''
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} {line1} {line2} ORDER BY id_measurements;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectModels(self, length, width):
        db = 'public."Model"'
        if length != '':
            line1 = f"WHERE length = {length}"
        else:
            line1 = ''
        if width != '' and line1 == '':
            line2 = f"WHERE width = {width}"
        elif width != '' and line1 != '':
            line2 = f"and width = {width}"
        else:
            line2 = ''
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} {line1} {line2} ORDER BY id_model;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectDevices(self, device_name, using_start_date):
        db = 'public."Devices"'
        line1 = device_name.lower()
        if using_start_date != '':
            line2 = f"and using_start_date = '{using_start_date}'"
        else:
            line2 = ''
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(device_name) LIKE '%{line1}%' {line2} ORDER BY id_device;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectTailors(self, surname, name):
        db = 'public."Tailor"'
        line1 = surname.lower()
        line2 = name.lower()
        try:
            self.cursor.execute(
                f"SELECT id_tailor, surname, name, middle_name FROM {db} WHERE LOWER(surname) LIKE '%{line1}%' and LOWER(name) LIKE '%{line2}%' ORDER BY id_tailor;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectModelSewings(self, sewing_date, id_status):
        db = 'public."Model_sewing"'
        if sewing_date != '':
            line1 = f"WHERE sewing_date = '{sewing_date}'"
        else:
            line1 = ''
        if id_status != '' and line1 == '':
            line2 = f"WHERE id_status = {id_status}"
        elif id_status != '' and line1 != '':
            line2 = f"and id_status = {id_status}"
        else:
            line2 = ''
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} {line1} {line2} ORDER BY ms_number;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectWarehouses(self, warehouse_name, square):
        db = 'public."Warehouse"'
        line1 = warehouse_name.lower()
        if square != '':
            line2 = f"and square = {square}"
        else:
            line2 = ''
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(warehouse_name) LIKE '%{line1}%' {line2} ORDER BY id_warehouse;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectStandarts(self, standart_name, standart_docs):
        db = 'public."Standarts"'
        line1 = standart_name.lower()
        line2 = standart_docs.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(standart_name) LIKE '%{line1}%' and LOWER(standart_docs) LIKE '%{line2}%' ORDER BY id_standart;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectStatuses(self, status_name, description):
        db = 'public."Status"'
        line1 = status_name.lower()
        line2 = description.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(status_name) LIKE '%{line1}%' and LOWER(description) LIKE '%{line2}%' ORDER BY id_status;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectMaterialTypes(self, material_name, description):
        db = 'public."Material_type"'
        line1 = material_name.lower()
        line2 = description.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(material_name) LIKE '%{line1}%' and LOWER(description) LIKE '%{line2}%' ORDER BY id_material_type;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectModelDemands(self, demand_name, description):
        db = 'public."Model_demand"'
        line1 = demand_name.lower()
        line2 = description.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(demand_name) LIKE '%{line1}%' and LOWER(description) LIKE '%{line2}%' ORDER BY id_demand;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectClientDemands(self, id_client, description):
        db = 'public."Client_demand"'
        line1 = description.lower()
        if id_client != '':
            line2 = f"and id_client = {id_client}"
        else:
            line2 = ''
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(description) LIKE '%{line1}%' {line2} ORDER BY id_demand;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectSewingStages(self, stage_status, stage_description):
        db = 'public."Sewing_stage"'
        line1 = stage_status.lower()
        line2 = stage_description.lower()
        try:
            self.cursor.execute(
                f"SELECT * FROM {db} WHERE LOWER(stage_status) LIKE '%{line1}%' and LOWER(stage_description) LIKE '%{line2}%' ORDER BY stage_num;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def insert(self, dbName, valuesName, valuesList):
        try:
            self.cursor.execute(
                f'INSERT INTO public."{dbName}" {valuesName} VALUES {valuesList};'
            )
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, dbName, setValues):
        try:
            self.cursor.execute(
                f'UPDATE public."{dbName}" SET {setValues};'
            )
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, dbName, condition):
        try:
            self.cursor.execute(
                f'DELETE FROM public."{dbName}" WHERE {condition};'
            )
            return True
        except Exception as e:
            print(e)
            return False

    def avgChestHeight(self):
        try:
            self.cursor.execute(
                'SELECT public.avg_chest_height();'
            )
            return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)
            return ''

    def orderSum(self):
        try:
            self.cursor.execute(
                'SELECT public.order_sum();'
            )
            return self.cursor.fetchall()[0][0]
        except Exception as e:
            print(e)
            return ''

    def calcBackWidth(self, chest):
        try:
            self.cursor.execute(
                f'SELECT public.calc_back_width({chest});'
            )
            return 'Ширина спины = ' + str(self.cursor.fetchall()[0][0])
        except Exception as e:
            print(e)
            return 'Ошибка в веденных данных'

    def calcChestHeight(self, chest):
        try:
            self.cursor.execute(
                f'SELECT public.calc_chest_height({chest});'
            )
            return 'Высота груди = ' + str(self.cursor.fetchall()[0][0])
        except Exception as e:
            print(e)
            return 'Ошибка в веденных данных'

    def calcChestWeightWomen(self, chest):
        try:
            self.cursor.execute(
                f'SELECT public.calc_chest_weight_women({chest});'
            )
            return 'Ширина груди = ' + str(self.cursor.fetchall()[0][0])
        except Exception as e:
            print(e)
            return 'Ошибка в веденных данных'

    def getS(self, len, wid):
        try:
            self.cursor.execute(
                f'SELECT public."getS"({len}, {wid});'
            )
            return 'Площадь = ' + str(self.cursor.fetchall()[0][0])
        except Exception as e:
            print(e)
            return 'Ошибка в веденных данных'

    def giveUseDays(self, id):
        try:
            self.cursor.execute(
                f'SELECT public."give_use_days"({id});'
            )
            return 'Количество дней - ' + str(self.cursor.fetchall()[0][0])
        except Exception as e:
            print(e)
            return 'Ошибка в веденных данных'

    def newStage(self, msNumber, stageNum):
        try:
            self.cursor.execute(
                f'CALL public."new_stage"({msNumber}, {stageNum});'
            )
            return 'Заменено успешно'
        except Exception as e:
            print(e)
            return 'Ошибка в веденных данных'

    def selectFree(self, values, dbName):
        try:
            self.cursor.execute(
                f'SELECT {values} FROM public."{dbName}";'
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectIJ(self, values, dbName, dbNameJoin, key):
        try:
            self.cursor.execute(
                f'SELECT {values} FROM public."{dbName}" INNER JOIN public."{dbNameJoin}" ON "{dbNameJoin}".{key} = "{dbName}".{key};'
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectGB(self, values, dbName, key):
        try:
            self.cursor.execute(
                f'SELECT {values} FROM public."{dbName}" GROUP BY {key}'
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []