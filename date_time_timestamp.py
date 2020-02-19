import time
import datetime


date = "2020-02-10 00:00:00"
print(f"{date} date string to timestamp")
ts = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").timetuple())
print(f"result of timestamp : {ts}")

print()
print(f"{ts} timestamp to date string")
print(f"result of date {datetime.datetime.fromtimestamp(ts)}")

print("------------------------------")

date = "2020-02-10 00:00:00.123"
print(f"{date} date string with milliseconds to timestamp")
ts_with_milli_sec = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").timestamp() * 1000
print(f"result of timestamp : {ts_with_milli_sec}")

print()
print(f"{ts_with_milli_sec} timestamp to date string with milliseconds")
print(f"result of date {datetime.datetime.fromtimestamp(ts_with_milli_sec / 1000)}")
