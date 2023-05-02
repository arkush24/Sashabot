import sqlite3

class SQLighter:

    def __init__(self, database_file):
        """Подключаемся к БД и сохраняем курсор"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_all_names(self, url):
        """Получаем все названия фанфиков в БД"""
        url = "top_"+url
        with self.connection:
            return self.cursor.execute("SELECT * FROM "+url).fetchall()

    def names_exists(self, name, url):
        """Проверяем есть ли имя в базе, если нет то +, иначе -"""
        url = "top_"+url
        with self.connection:
            result = self.cursor.execute("SELECT * FROM "+url+" WHERE name = ?", (name,)).fetchall()
            return bool(len(result))

    def add_name(self, name, url, url_db):
        """Добавляем имя фанфика"""
        url = "top_"+url
        with self.connection:
            return self.cursor.execute("INSERT INTO "+url+" ('name','url') VALUES (?,?)", (name,url_db,))

    def update_subscription(self, user_id, status):
        """ Обновляем статус подписки, пока хуй знает зачем"""
        return self.cursor.execute("UPDATE 'top_get' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))

    def delete(self, url):
        """Закрываем соединение с бд"""
        url = "top_"+url
        print("temp deleted")
        with self.connection:
            self.cursor.execute("DELETE FROM %s" % url)

    def close(self):
        """Закрываем соединение с бд"""
        self.connection.close()


















'''
    def get_all_users(self, status = True):
        """Получаем всех активных пользователей бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users' WHERE 'status' = ?", (status,)).fetchall()

    def users_exists(self, user_id):
        """проверяем есть ли юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = '%i'" % user_id).fetchall()
            print(len(result))
            return bool(len(result))

    def add_users(self, user_id, user_login, user_password, status = True):
        """Добавляем пользователя"""
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id', 'user_login', 'user_password', 'status') VALUES (?,?,?,?)", (user_id, user_login, user_password, status))

    def update_subscription(self, user_id, status):
        """ Обновляем статус подписки, пока хуй знает зачем"""
        return self.cursor.execute("UPDATE 'users' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))

    def close(self):
        """Закрываем соединение с бд"""
        self.connection.close()
'''
