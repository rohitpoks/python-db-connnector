from jproperties import Properties
import mysql.connector


class ConfigureDB:

    def __init__(self, filepath, host_key, user_key, password_key, db_name_key):
        configs = Properties()
        with open(filepath, 'rb') as config_file:
            configs.load(config_file)
        HOST = configs.get(host_key)
        USER = configs.get(user_key)
        PASSWORD = configs.get(password_key)
        DATABASE = configs.get(db_name_key)
        self.db = mysql.connector.connect(host=HOST.data, user=USER.data, passwd=PASSWORD.data, database=DATABASE.data)
        self.mycursor = self.db.cursor()


newDB = ConfigureDB("sample.properties", "db.url", "db.user", "db.password", "db.name")
newDB.mycursor.execute("SELECT * FROM Person")
for person in newDB.mycursor:
    print(person)
