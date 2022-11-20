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
        except Exception as e:
            print('[INFO] Ошибка во время подключения к базе данных', e)
        return self.connection

    def selectVersion(self):
        """
        Получить версию

        Возвращает: Вресию psql в tulpe
        """
        self.cursor.execute(
            "SELECT version();"
        )
        return self.cursor.fetchone()

    def close(self):
        """Закрытие соединения"""
        if self.connection:
            self.connection.close()
            print('[ИНФО] Соединение с базой данных остановлено')

    def selectBooks(self, nameBook, state, genre, publishYear, idAuthor):
        nameBook = nameBook.lower()
        state = state.lower()
        genre = genre.lower()
        if state != 'true' or state != 'false':
            stateStr = 'state IS NOT NULL'
        else:
            stateStr = f"state = '{state}'"
        if publishYear == '':
            yearStr = ''
        else:
            yearStr = f"and publish_year = date('{publishYear}')"
        if idAuthor == '':
            idStr = ''
        else:
            idStr = f"and id_author = {idAuthor}"
        try:
            self.cursor.execute(
                f"SELECT * FROM books WHERE LOWER(name_book) LIKE '%{nameBook}%' and {stateStr} and LOWER(genre) LIKE "
                f"'%{genre}%' {yearStr} {idStr} ORDER BY id_book;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectAuthors(self, firstName, lastName, birthday):
        firstName = firstName.lower()
        lastName = lastName.lower()
        if birthday == '':
            yearStr = ''
        else:
            yearStr = f"and birthday = date('{birthday}')"
        try:
            self.cursor.execute(
                f"SELECT * FROM authors WHERE LOWER(first_name) LIKE '%{firstName}%' and LOWER(last_name) LIKE '%{lastName}%'"
                f" {yearStr} ORDER BY id_author;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectFormulars(self, idTicket, idWorker, dateTake, dateBack, books):
        books = books.lower()
        if dateTake == '':
            yearStr = ''
        else:
            yearStr = f"and date_take = date('{dateTake}')"
        if dateBack == '':
            yearStr2 = ''
        else:
            yearStr2 = f"and date_back = date('{dateBack}')"
        if idTicket == '':
            idStr = ''
        else:
            idStr = f"and id_ticket = {idTicket}"
        if idWorker == '':
            idStr2 = ''
        else:
            idStr2 = f"and id_worker = {idWorker}"
        try:
            self.cursor.execute(
                f"SELECT * FROM formulars WHERE Lower(books) LIKE '%{books}%' {idStr} {idStr2} {yearStr} {yearStr2}  "
                f"ORDER BY formular_num;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectLibraryWorkers(self, firstName, lastName, birthday, namePost):
        firstName = firstName.lower()
        lastName = lastName.lower()
        namePost = namePost.lower()
        if birthday == '':
            yearStr = ''
        else:
            yearStr = f"and birthday = date('{birthday}')"
        try:
            self.cursor.execute(
                f"SELECT * FROM library_workers WHERE LOWER(first_name) LIKE '%{firstName}%' and LOWER(last_name) LIKE "
                f"'%{lastName}%' and LOWER(name_post) LIKE '%{namePost}%' {yearStr} ORDER BY id_worker;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectPosts(self, salary, term, clearenceLevel):
        if clearenceLevel == '':
            idStr = ''
        else:
            idStr = f"and clearence_level = {clearenceLevel}"
        if salary == '':
            idStr2 = ''
        else:
            idStr2 = f"and salary = {salary}"
        if term == '':
            yearStr = ''
        else:
            yearStr = f"and term = date('{term}')"
        try:
            self.cursor.execute(
                f"SELECT * FROM posts WHERE name_post LIKE '%%' {idStr} {idStr2} {yearStr} ORDER BY name_post;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def selectTickets(self, firstName, lastName, birthday, rating):
        firstName = firstName.lower()
        lastName = lastName.lower()
        if birthday == '':
            yearStr = ''
        else:
            yearStr = f"and birthday = date('{birthday}')"
        if rating == '':
            idStr = ''
        else:
            idStr = f"and rating = {rating}"
        try:
            self.cursor.execute(
                f"SELECT * FROM tickets WHERE first_name LIKE '%{firstName}%' and last_name LIKE '%{lastName}%' {yearStr} "
                f"{idStr} ORDER BY id_ticket;"
            )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []
    def insertBooks(self, idBook, nameBook, state, genre, publishYear, idAuthor):
        try:
            self.cursor.execute(
                F"INSERT INTO books(id_book, name_book, state, genre, publish_year, id_author) VALUES ({idBook}, "
                F"'{nameBook}', {state}, '{genre}', '{publishYear}', {idAuthor});"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def insertAuthors(self, idAuthor, firstName, lastName, birthday):
        try:
            self.cursor.execute(
                F"INSERT INTO authors(id_author, first_name, last_name, birthday) VALUES ({idAuthor}, '{firstName}', "
                F"'{lastName}', '{birthday}');"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def insertFormulars(self, formularNum, idTicket, idWorker, dateTake, dateBack, books):
        try:
            self.cursor.execute(
                F"INSERT INTO formulars(formular_num, id_ticket, id_worker, date_take, date_back, books) VALUES ("
                F"{formularNum}, {idTicket}, {idWorker}, '{dateTake}', '{dateBack}', '{books}');"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def insertTickets(self, idTicket, firstName, lastName, birthday, rating):
        try:
            self.cursor.execute(
                F"INSERT INTO tickets(id_ticket, first_name, last_name, birthday, rating) VALUES ({idTicket}, "
                F"'{firstName}', '{lastName}', '{birthday}', {rating});"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def insertWorkers(self, idWorker, firstName, lastName, birthday, namePost):
        try:
            self.cursor.execute(
                F"INSERT INTO library_workers(id_worker, first_name, last_name, birthday, name_post) VALUES ({idWorker},"
                F"'{firstName}', '{lastName}', '{birthday}', '{namePost}');"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def insertPost(self, namePost, salary, term, clearenceLevel):
        try:
            self.cursor.execute(
                F"INSERT INTO posts(name_post, salary, term, clearence_level) VALUES ('{namePost}', {salary}, '{term}',"
                F" {clearenceLevel});"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def updateAuthors(self, idAuthor, firstName, lastName, birthday):
        try:
            self.cursor.execute(
                F"UPDATE authors SET first_name='{firstName}', last_name='{lastName}', birthday='{birthday}'"
                F"WHERE id_author = {idAuthor};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def updateBooks(self, idBook, nameBook, state, genre, publishYear, idAuthor):
        try:
            self.cursor.execute(
                F"UPDATE books SET name_book='{nameBook}', state={state}, genre='{genre}', publish_year = '{publishYear}'"
                F", id_author={idAuthor} WHERE id_book = {idBook};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def updateFormulars(self, formularNum, idTicket, idWorker, dateTake, dateBack, books):
        try:
            self.cursor.execute(
                F"UPDATE formulars SET id_ticket={idTicket}, id_worker={idWorker}, date_take='{dateTake}', "
                F"date_back = '{dateBack}', books='{books}' WHERE formular_num = {formularNum};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def updateTickets(self, idTicket, firstName, lastName, birthday, rating):
        try:
            self.cursor.execute(
                F"UPDATE tickets SET first_name='{firstName}', last_name='{lastName}', birthday='{birthday}', "
                F"rating = {rating} WHERE id_ticket = {idTicket};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def updateWorkers(self, idWorker, firstName, lastName, birthday, namePost):
        try:
            self.cursor.execute(
                F"UPDATE library_workers SET first_name='{firstName}', last_name='{lastName}', birthday='{birthday}', "
                F"name_post = '{namePost}' WHERE id_worker = {idWorker};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def updatePost(self, namePost, salary, term, clearenceLevel):
        try:
            self.cursor.execute(
                F"UPDATE posts SET salary={salary}, term='{term}', clearence_level ='{clearenceLevel}'"
                F" WHERE name_post = '{namePost}';"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def deleteBook(self, idBook):
        try:
            self.cursor.execute(
                F"DELETE FROM books WHERE id_book={idBook};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def deleteAuthor(self, idAuthor):
        try:
            self.cursor.execute(
                F"DELETE FROM authors WHERE id_author={idAuthor};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def deleteFormular(self, formularNum):
        try:
            self.cursor.execute(
                F"DELETE FROM formulars WHERE formular_num={formularNum};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def deleteTicket(self, idTicket):
        try:
            self.cursor.execute(
                F"DELETE FROM tickets WHERE id_ticket={idTicket};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def deleteWorker(self, idWorker):
        try:
            self.cursor.execute(
                F"DELETE FROM library_workers WHERE id_worker={idWorker};"
            )
            return True
        except Exception as e:
            print(e)
            return False

    def deletePost(self, postName):
        try:
            self.cursor.execute(
                F"DELETE FROM posts WHERE name_post='{postName}';"
            )
            return True
        except Exception as e:
            print(e)
            return False