import os
import json
from datetime import date, datetime

table_list = []
total_time_played = 0

def table_maker():
    for i in range(0, 12):
        table_dict = {
            "table_number": None,
            "occupied": 'Not Occupied',
            "start_time": None,
            "end_time": None,
            "num_minutes_played": None
        }
        table_dict['table_number'] = i + 1
        table_list.append(table_dict)

def view_tables(table_to_check):
    for i in range(0, len(table_list)):
        tbl = table_list[i]
        print(f'''
            Table_number: {tbl["table_number"]}
            Occupied: {tbl["occupied"]}
            Start time: {tbl["start_time"]}
            End time: {tbl["end_time"]}
            Minutes Played: {tbl["num_minutes_played"]}
        ''')

def time_adder():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def mark_as_occupied(table_num):
    for i in range(0, len(table_list)):
        tbl = table_list[i]
        if (tbl["table_number"] == table_num) and (tbl["occupied"] != "Occupied"):
            tbl["occupied"] = 'Occupied'
            tbl["start_time"] = time_adder()
            print(f'Table: {table_num} is now {tbl["occupied"]}')
        elif (tbl["table_number"] == table_num) and (tbl["occupied"] == 'Occupied'):
            print(f'Table {table_num} is already occupied')

def mark_as_unoccupied(table_num):
    tbl = table_list[i]
    if (tbl["table_number"] == table_num) and (tbl["occupied"] == "Occupied"):
        tbl["occupied"] != 'Not Occupied' # ???
        tbl["end_time"] = time_adder()            
        start_time_delta = datetime.strptime(tbl["start_time"], "%H:%M:%S")
        end_time_delta = datetime.strptime(tbl["end_time"], "%H:%M:%S")
        minutes_played = str(end_time_delta - start_time_delta)  # timedelta type
        tbl["num_minutes_played"] = minutes_played
        table_reset(table_num, minutes_played)
        print(f"Table occupied for {minutes_played}")
        print(f"Total time table {table_num} used today: {total_time_played}")
        

def table_reset(table_to_reset, min_played):
    table_reset = table_list[table_to_reset]
    datetime_time_played = datetime.strptime(min_played)
    table_reset["num_minutes_played"] += datetime_time_played

def end_of_day_date_adder():
    today = date.today()
    return today.strftime("%B %d, %Y")
    
file_path = 'tables.json'

def is_file_empty(file_path):
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

is_empty = is_file_empty(file_path)

if is_empty:
    print("file is empty")
    table_maker()
else:
    with open('tables.json', 'r') as file:
        saved_tables = json.load(file)

    for i in range(0, len(saved_tables)):
        table_list.append(saved_tables[i])


