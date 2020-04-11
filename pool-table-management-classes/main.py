from datetime import date
import view
import json
from logic import Table, PoolHall

running = True


while running:
    view.show_menu()
    choice = input("Input: ")
    if choice == '1':
        user_table_num = int(input("Choose a table to mark occupied: "))
        for index in range(0, len(view.pool_hall_tables)):
            table = view.pool_hall_tables[index]
            if table['table_number'] == user_table_num:
                Table(table['table_number']).open_table()
                break
            else:
                "Please choose a valid table"
    elif choice == '2':
        user_table_num = int(input("Choose a table to mark unoccupied: "))
        for index in range(0, len(view.pool_hall_tables)):
            table = view.pool_hall_tables[index]
            if table['table_number'] == user_table_num:
                Table(table['table_number']).close_table()
                break
        else:
            "Please choose a valid table"
    elif choice == '3':
        view.my_poolhall.view_tables_in_hall()
    if choice == 'q':
        break

view.save_to_json(view.pool_hall_tables)
