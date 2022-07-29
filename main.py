import mysql.connector


class PracticeDB:
    def __init__(self):
        HOST = "localhost"
        USER = "root"
        PASSWORD = "password"
        DATABASE = "testdatabase"

        self.db = mysql.connector.connect(host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)
        self.mycursor = self.db.cursor()
        # self.add_to_person_table(["name", "age"], ["Rohit", "18"])
        # self.select_all_people()
        # self.select_specific_people(age=18, id=2)
        # self.order_by_column("name", False)
        # self.run_query("UPDATE person SET personID = 0 WHERE personID = 2")
        self.select_all_people()

    def run_query(self, query):
        self.mycursor.execute(query)

    def run_select_query(self, query):
        self.mycursor.execute(query)
        for row in self.mycursor:
            print(row)

    def order_by_column(self, column_name, asc=True):
        query = "SELECT * FROM person ORDER BY " + column_name
        if not asc:
            query += " DESC"
        self.mycursor.execute(query)
        for row in self.mycursor:
            print(row)

    def create_person_table(self):
        self.mycursor.execute(
            "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

    def describe_person_table(self):
        self.mycursor.execute("DESCRIBE Person")
        for row in self.mycursor:
            print(row)

    # list of column names as string and list of value names as string
    def add_to_person_table(self, columns, values):
        name = -1
        query = "INSERT INTO PERSON ("
        for column in columns:
            query += column + ", "
            if column == "name":
                name = columns.index("name")
        query = query[0:-2]
        query += ") VALUES ("
        count = 0
        for value in values:
            if count == name:
                value = "'" + value + "'"
            count += 1
            query += value + ", "
        query = query[0:-2]
        query += ")"
        self.mycursor.execute(query)
        self.db.commit()

    def select_all_people(self):
        self.mycursor.execute("SELECT * FROM Person")
        for person in self.mycursor:
            print(person)

    def select_specific_people(self, name="", age=-1, id=-1):
        query = "SELECT * FROM Person"
        if name != "" or age != -1 or id != -1:
            query += " WHERE"
            if name != "":
                query += " name = " + "'" + name + "'"
            if age != -1:
                if name != "":
                    query += " AND"
                query += " age = " + str(age)
            if id != -1:
                if name != "" or age != -1:
                    query += " AND"
                query += " personID = " + str(id)
            self.mycursor.execute(query)
            for person in self.mycursor:
                print(person)






connection = PracticeDB()
