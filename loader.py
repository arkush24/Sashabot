import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


from utils.db_api.sqlighter import SQLighter

#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#соеденяем с бд
#db = SQLighter('data/database.db')

#подгрузка вебсайта
#driver = webdriver.Chrome(ChromeDriverManager().install())
