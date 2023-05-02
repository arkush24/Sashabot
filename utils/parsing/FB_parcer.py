from bs4 import BeautifulSoup
from selenium import webdriver


import sys
sys.path.append('../..')
from data.config import URL, url_main, url_temp

from webdriver_manager.chrome import ChromeDriverManager

"""
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL+url_main[0])

items = driver.find_elements_by_class_name('visit-link')


for item in items:
    print(item.get_attribute('href'))
"""
def fill_table():
    """Заполнение таблицы сегодняшними топами"""

    driver = webdriver.Chrome(ChromeDriverManager().install())
    for i in range(3):
        db.delete(url_main[i])
        driver.get(URL+url_main[i])
        items = driver.find_elements_by_class_name('visit-link')
        if items:
            print('its ok')
        for item in items:
            db.add_name(item.text, url_main[i])
    driver.quit()

def fill_temp():
    """Заполнение temp баз данных"""

    del_temp()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for i in range(3):
        driver.get(URL+url_main[i])
        items = driver.find_elements_by_class_name('visit-link')
        if items:
            print('its ok')

        for item in items:
            if not db.names_exists(item.text, url_main[i]):
                db.add_name(item.text, url_temp[i],item.get_attribute('href'))



def del_temp():
    """Удаляем temp базы данных"""
    for i in range(3):
        db.delete(url_temp[i])

def saw_all_names():
    """Выводим все что есть в temp базах данных"""
    for i in range(3):
        print(db.get_all_names(url_temp[i]))

def saw_names(numb):
    """функция на выход: показать все имена"""
    return db.get_all_names(url_temp[numb])



def hendler_top():
    """ Админ функция на выход: заполнить таблицы"""
    #fill_temp()
    #fill_table()
    print("есть контакт")


if __name__ == '__main__':
    import sys
    sys.path.append('..')
    from db_api import sqlighter
    db = sqlighter.SQLighter('../../data/database.db')
    saw_names(0)

else:
    from loader import db
