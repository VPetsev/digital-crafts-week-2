from datetime import date, datetime

today = date.today()

def end_of_day_date_adder():
    today = date.today()
    return today.strftime("%B %d, %Y")

def time_adder():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

my_dict = {
    "table_number": 2,
    "occupied": "Occupied",
    "start_time": "18:33:01",
    "end_time": None,
    "num_minutes_played": None
}

my_dict["end_time"] = time_adder()
start_time_delta = datetime.strptime(my_dict["start_time"], "%H:%M:%S")
end_time_delta = datetime.strptime(my_dict["end_time"], "%H:%M:%S")


total_time = (end_time_delta - start_time_delta) # timedelta type
print(total_time)
my_dict["num_minutes_played"] = date.strftime(total_time)

print(my_dict["num_minutes_played"], "%H:%m:%s")
print(type(my_dict["num_minutes_played"]))
