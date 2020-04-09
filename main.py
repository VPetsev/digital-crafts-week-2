# You have just been hired by University of Houston as a developer. 
# Your first task is to create a pool table management app which will manage the pool tables in University Center Games Room.
# Here are the requested features:
# - As an admin you should be able to see all the tables(12)
# - As an admin each table in the list should show, whether the table is OCCUPIED or NOT OCCUPIED.
# - As an admin if the table is OCCUPIED then show the start time of the table, number of minutes played. 
    # (Hardmode - If the minutes are > 60 then show them in terms of hours)
# - As an admin you can only give out the tables that are NOT OCCUPIED. This means if 
    # pool table 8 is occupied and you try to give it 
    # out then the app will print a message saying "Pool Table 8 is currently occupied".
# - As an admin whenever I close the table it should write an entry in the text file / json file.
    #  The file should be named in the following format:
    #  (11-22-2017.txt or 11-22-2017.json) keeping track of all the tables. 
    #  The entry can consists of the following information:
# _________________________________________
    # Pool Table Number
    # Start Date Time
    # End Date Time
    # Total Time Played
    # Cost(if you are doing the hard mode)
# ___________________________________________

# HARD MODE - Associate dollar amount for time played on the pool table. $30 per hour.

# MORE HARD MODE - Write Unit Tests for your application

import json
from datetime import date
import random

# today = date.today()
# print(today)

now = datetime.datetime.now()
print(now)

# features algorithms:
# Create a json array of dictionaries for each table:
#   [{
#       Table Number: int
#       Occupied: Boolean
#       Start Time: Int?
#       Minutes played: int - default 0    
# }]
# Class InitializeTable:
#       def __init__(self):
#           self.table_number = table_number
#           occupied: False
#           start_time: ???
#           end_time: ???
#           number_of_minutes_played: start_time - end_time ## (logic for hours?)
#
#       def markAsOccupied(self):
#           pass
#   
# while loop:
#   
#   list_of_tables = []
#       load the different tables into the list
#
#   
#       
#       
#   for i in list_of_tables:
#       if list_of_tables[i].occupied = False:
#           pick a table to give out    
#           make that random table occupied = True  # maybe do it in class - never mind
# 
#   
# 
#   
#   end_of_day_save = write date and final save