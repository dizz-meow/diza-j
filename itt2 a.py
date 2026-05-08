from datetime import datetime, timedelta
date_str = "2023-10-15 10:30:00"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
t1 = datetime(2023, 10, 15, 12, 0, 0)
t2 = datetime(2023, 10, 15, 10, 30, 0)
diff_seconds = (t1 - t2).total_seconds()
now = datetime.now()
current_info = now.strftime("%Y-%m-%d %H:%M:%S, %A")
base_date = datetime(2023, 10, 1)
plus_5 = base_date + timedelta(days=5)
minus_5 = base_date - timedelta(days=5)
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 10, 31)
weekends = 0
temp_date = start_date
while temp_date <= end_date:
    if temp_date.weekday() >= 5: # 5 is Saturday, 6 is Sunday
        weekends += 1
    temp_date += timedelta(days=1)
print(f"Date Object: {date_obj}")
print(f"Difference (seconds): {diff_seconds}")
print(f"Current: {current_info}")
print(f"Added: {plus_5.date()}, Subtracted: {minus_5.date()}")
print(f"Weekends between {start_date.date()} and {end_date.date()}: {weekends}")
