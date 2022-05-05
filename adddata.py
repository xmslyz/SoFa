import sqlite3
from datetime import datetime

class Database:
    INSERT_COMMAND = 'insert into ksiega (data, hora, tipo, recibio, cuota, celebro) values (?,?,?,?,?,?)'
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def addRecord(self, year, month, day, autoCommit = False):
        self.cursor.execute(self.INSERT_COMMAND, (f'{day}-{month}-{year}','','','','',''))
        if autoCommit:
            self.connection.commit()

    def getData(self):
        result = self.connection.execute('select * from ksiega')
        return [row for row in result]

    def commit(self):
        self.connection.commit()

class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def isSunday(self, day):
        return datetime(self.year, self.month, day).weekday() == 6

    def numberOfDays(self):
        if self.month == 2:
            return 29 if self.year % 4 == 0 else 28
        elif self.month % 2 + (self.month // 7) == 0:
            return 30
        else:
            return 31

    def addRecords(self, database):
       for day in range(1, self.numberOfDays() + 1):
           for recordIdx in range(9 if self.isSunday(day) else 7):
               database.addRecord(self.year, self.month, day)
       database.commit()

# przyklad uzycia:
database = Database('person.db')
Month(2022,5).addRecords(database)
Month(2022,6).addRecords(database)
#odczyt danych
r = database.getData()
print(r)
