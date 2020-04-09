import os
table_list = []

def table_maker():
    for i in range(0, 12):
        table_dict = {
            "table_number": None,
            "occupied": False,
            "start_time": None,
            "end_time": None,
            "num_minutes_played": None
        }
        table_dict['table_number'] = i
        table_list.append(table_dict)


def view_all_tables():
    # input for specific tables in main function
    # or default of all tables
    # sort by occupied/unoccupied
    print(table_list)
    for i in range(0, len(table_list)):
        print(i)
        print(f'''
            Table_number: {table_list[i]["table_number"]}
            Occupied: {table_list[i]["occupied"]}
            Start time: {table_list[i]["start_time"]}
            End time: {table_list[i]["end_time"]}
            Minutes Played: {table_list[i]["num_minutes_played"]}
        ''')


def mark_as_occupied(table_num):
    for i in table_list:
        if table_num in table_list[i]:
            table_list[i]["occupied"] = 'Occupied'





file_path = 'tables.json'

def is_file_empty(file_path):
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0


is_empty = is_file_empty(file_path)

if is_empty:
    print("file is empty")
    # table_maker()
