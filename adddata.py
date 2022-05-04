from datetime import datetime
import sqlite3


class Dodaj:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def isSunday(self, year, month, day):
        return datetime (year, month, day).weekday() == 6


    def monthDays(self, month, year):
        if month == 2:
            return 29 if year % 4 == 0 else 28
        elif month % 2 + (month // 7) == 0:
            return 30
        else:
            return 31


    def addRecords (self, month, year):
        for day in range (self.monthDays(month, year)):
            for recordIdx in range (7 if self.isSunday(year, month, day + 1) else 9):
                self.addRecord(recordIdx, day + 1, month, year)


    def addRecord(self, idx, day, month, year):
        print("adding ", idx, "for", datetime(year, month, day))



con = sqlite3.connect("person.db")
cur = con.cursor()
data = 0        # addRecord
sql = ( " INSERT INTO ksiega (data, hora, tipo, recibio, cuota, celebro) VALUES (?,?,?,?,?,?) " )
value = (data, "", "", "", "", "")
cur.execute(sql, value)
con.commit()
cur.close()
