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
        # self.is_occupied doesn't refer to pool_hall_table?
        # or maybe it does because in open_tab callback it is converted to a Table class
        # so I can remove line 20?
        if self.is_occupied == "Not Occupied":
            self.is_occupied = "Occupied"
            # can i move chosen_table somewhere? How about in the init function? Why would that work or not?
            chosen_table = view.pool_hall_tables[self.table_number - 1]
            chosen_table['is_occupied'] = self.is_occupied
            chosen_table["start_time"] = datetime.now()
            print(chosen_table)
        else:
            print("no match")
    
    def close_table(self):
        chosen_table = view.pool_hall_tables[self.table_number - 1]
        if chosen_table["is_occupied"] == "Occupied":
            chosen_table['is_occupied'] = 'Not Occupied'
            chosen_table["end_time"] = datetime.now()
            self.min_played()
        else:
            print('no match')

    def min_played(self):
        # chosen table is used alot, try to refactor. see line 21
        chosen_table = view.pool_hall_tables[self.table_number - 1]
        chosen_table["total_minutes_played_today"] = chosen_table['end_time']- chosen_table['start_time']
        chosen_table['start_time'] = None
        chosen_table["end_time"] = None

    def format_datetime(self, input_value):
        chosen_table = view.pool_hall_tables[self.table_number - 1]
        print(chosen_table)
        print(input_value)
        if type(input_value) == datetime:
            my_str = input_value.strftime("%H:%M:%S")
            print(my_str)
            return(my_str)
        else:
            print('error')

    def toDict(self):
        return {
            "table_number": self.table_number,
            "is_occupied": "Not Occupied",
            "start_time": self.start_time,
            "end_time": self.end_time,
            "total_minutes_played_today": self.total_minutes_played_today
        }


class PoolHall:

    def __init__(self, tables):
        self.all_tables = tables

    def view_tables_in_hall(self):
        for i in range(0, len(self.all_tables)):
            tbl = self.all_tables[i]
            print(f'''
                Table_number: {tbl["table_number"]}
                Occupied: {tbl["is_occupied"]}
                Start time: {tbl["start_time"]}
                End time: {tbl["end_time"]}
                Minutes Played: {tbl["total_minutes_played_today"]}
            ''')

    def end_of_day_date_adder(self):
        today = date.today()
        return today.strftime("%B %d, %Y")
