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
