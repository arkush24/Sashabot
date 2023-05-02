from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()


BOT_TOKEN = "6187368993:AAEmj3HVJPuPwSKVaSalyuTDfo7Ou5tbSgo"  # Забираем значение типа str
#ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
#IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

#HOST = 'https://ficbook.net/' #Хост
#URL = 'https://ficbook.net/popular/' #основная ссылка

url_main =['all', 'gen', 'het'] #вспомогательные
url_temp =['temp_all', 'temp_gen', 'temp_het'] #tempопвые
