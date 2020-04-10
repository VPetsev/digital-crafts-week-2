import logic

pool_hall_tables = []
for i in range(1, 13):
    table = logic.Table(i)
    pool_hall_tables.append(table)

my_poolhall = logic.PoolHall(pool_hall_tables)

# def menu_print():
#     print("""
# Menu options (1/2/3/q): 
# 1. Mark a table as occupied
# 2. Mark a table as unoccupied
# 3. See all active tables
# 4. Total revenue
# 5. Revenue per table")
# q. Press q to quit""")
#     user_choice = input()
#     user_choice
