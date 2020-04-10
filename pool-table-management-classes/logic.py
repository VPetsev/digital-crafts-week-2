import os
import json
import view
from datetime import date, datetime

# file_path = 'tables.json'

# is_empty = is_file_empty(file_path)

# if is_empty:
#     print("file is empty")
#     table_maker()
# else:
#     with open('tables.json', 'r') as file:
#         saved_tables = json.load(file)

#     for i in range(0, len(saved_tables)):
# table_list.append(saved_tables[i])


class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = "Not Occupied"
        self.start_time = ""
        self.end_time = ""
        self.total_minutes_played_today = 0

# which number to mark as occupied?

    def mark_table_as_occupied(self, table):
        if view.pool_hall_tables[table].is_occupied == "Not Occupied":
            view.pool_hall_tables[table].is_occupied = "Occupied"
        else:
            print("no match")
            
    def time_adder(self, table):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if view.pool_hall_tables[table].start_time == "":
            view.pool_hall_tables[table].start_time = current_time
            print('if fired')
        elif (view.pool_hall_tables[table].start_time != "" and 
              view.pool_hall_tables[table].end_time == ""):
            view.pool_hall_tables[table].end_time = current_time
            time_started = int(view.pool_hall_tables[table].start_time)
            time_ended = int(view.pool_hall_tables[table].end_time) 
            time_played = time_ended - time_started
            view.pool_hall_tables[table].total_minutes_played_today += time_played
            # reset table here or in main?
            print('elif fired')
        else:
            print("unknown error")
        

    def mark_table_as_unoccupied(self, table):
        if (view.pool_hall_tables[table].is_occupied == "Occupied"):
            view.pool_hall_tables[table].is_occupied = "Not Occupied"
        else:
            print("else fired")

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
                Minutes Played: {tbl.number_of_minutes_played}
            ''')

    def reset_table(self, table_to_reset):
        datetime_time_played = datetime.strptime(min_played)
        table_reset["num_minutes_played"] += datetime_time_played

    def end_of_day_date_adder(self):
        today = date.today()
        return today.strftime("%B %d, %Y")

# def end_of_day_date_adder():
#     today = date.today()
#     return today.strftime("%B %d, %Y")

# file_path = 'tables.json'

# def is_file_empty(file_path):
#     return os.path.exists(file_path) and os.stat(file_path).st_size == 0



