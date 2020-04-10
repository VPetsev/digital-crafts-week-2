import os
import json
import view
from datetime import date, datetime, timedelta


class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = "Not Occupied"
        self.start_time = None
        self.end_time = None
        self.total_minutes_played_today = 0.0

    def open_table(self):
        if self.is_occupied == "Not Occupied":
            self.is_occupied = "Occupied"
            print(self.is_occupied)
            print(self.table_number)
            self.start_time = datetime.now()
        else:
            print("no match")
    
    def close_table(self):
        if self.is_occupied == "Occupied":
            self.is_occupied = "Not Occupied"
            self.end_time = datetime.now()
            self.total_minutes_played_today += self.min_played() 

    def min_played(self):
        total_time = (self.end_time - self.start_time)
        self.total_minutes_played_today = total_time

    def format_datetime(self, format):
        if type(format) == datetime:
            return format.strftime("%H:%M:%S")

    def toDict(self):
        return {
            "table_number": self.table_number,
            "is_occupied": "Not Occupied",
            "start_time": self.format_datetime(self.start_time),
            "end_time": self.format_datetime(self.end_time),
            "total_minutes_played_today": self.format_datetime(self.total_minutes_played_today)
        }

class PoolHall:

    def __init__(self, tables):
        self.all_tables = tables

    def view_tables_in_hall(self):
        for i in range(0, len(self.all_tables)):
            tbl = self.all_tables[i]
            print(f'''
                Table_number: {tbl.table_number}
                Occupied: {tbl.is_occupied}
                Start time: {tbl.start_time}
                End time: {tbl.end_time}
                Minutes Played: {tbl.total_minutes_played_today}
            ''')

    def end_of_day_date_adder(self):
        today = date.today()
        return today.strftime("%B %d, %Y")
