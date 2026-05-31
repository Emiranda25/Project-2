import time
import sys
def time_tracker(time_input, previous_time):
    hours_input, minutes_input, seconds_input = map(int, time_input.split(':'))
    hours_previous, minutes_previous, seconds_previous = map(int, previous_time.split(':'))
    total_seconds = (hours_input + hours_previous) * 3600 + (minutes_input + minutes_previous) * 60 + (seconds_input + seconds_previous)
    final_hours = total_seconds // 3600
    final_minutes = (total_seconds % 3600) // 60
    final_seconds = total_seconds % 60
    final_time = f"{final_hours:02d}:{final_minutes:02d}:{final_seconds:02d}"
    return final_time

def stop_watch():
    time_start = time.time()
    try:
        while True:
            recorded_time = time.time() - time_start
            hours = int(recorded_time // 3600)
            minutes = int((recorded_time % 3600) // 60)
            seconds = int(recorded_time % 60)

            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            print(f"recorded time: {time_string}")

            sys.stdout.flush() #to update the terminal and empty the cpu to prevent overflow
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\n\nStopwatch stopped!")
        final_time = time.time() - time_start
        
        # Final time calculation
        hours = int(final_time // 3600)
        minutes = int((final_time % 3600) // 60)
        seconds = int(final_time % 60)
        
        print(f"Final Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
        print("====================================")
        


# current_log = "01:00:00"
# new_entry = "02:43:25"

# total = time_tracker(new_entry,current_log)
# print({total})

if __name__ == "__main__":
    stop_watch()