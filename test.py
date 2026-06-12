import personal_work_time_tracker

print("would you like to use today? Stop watch or manual input?")
info = input("what will you use today?")
x = info.upper()

if x == "STOPWATCH":
   personal_work_time_tracker.stop_watch()
if x == "INPUT":
   prev = input("Current time logged? in HH:MM:SS format " )
   cur = input("Time your trying to log? in HH:MM:SS format " )
   total = personal_work_time_tracker.time_tracker(prev,cur)
   print(total)
else:
   print("wrong input please try again")
