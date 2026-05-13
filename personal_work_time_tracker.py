def time_tracker(time_input, previous_time):
    hours_input, minutes_input, seconds_input = map(int, time_input.split(':'))
    hours_previous, minutes_previous, seconds_previous = map(int, previous_time.split(':'))
    total_seconds = (hours_input + hours_previous) * 3600 + (minutes_input + minutes_previous) * 60 + (seconds_input + seconds_previous)
    final_hours = total_seconds // 3600
    final_minutes = (total_seconds % 3600) // 60
    final_seconds = total_seconds % 60
    final_time = f"{final_hours:02d}:{final_minutes:02d}:{final_seconds:02d}"
    return final_time

current_log = "01:00:00"
new_entry = "02:43:25"

total = time_tracker(new_entry,current_log)
print({total})