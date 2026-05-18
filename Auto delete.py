import os
import time
from datetime import datetime, timedelta

HISTORY_FILE_PATH = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\History')
DAYS_THRESHOLD = 2

def clear_old_history(file_path, days):
    if not os.path.exists(file_path):
        print(f"File not found at: {file_path}")
        print("Please verify the file path for your specific browser and OS.")
        return

    last_modified_timestamp = os.path.getmtime(file_path)
    last_modified_date = datetime.fromtimestamp(last_modified_timestamp)
    
    current_time = datetime.now()
    time_inactive = current_time - last_modified_date

    print(f"Browser last active: {last_modified_date.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Time inactive: {time_inactive.days} days, {time_inactive.seconds // 3600} hours")

    if time_inactive > timedelta(days=days):
        print(f"\nBrowser has been inactive for more than {days} days. Deleting history...")
        try:
            os.remove(file_path)
            print("Success: Browser history has been deleted.")
        except PermissionError:
            print("\nError: Permission denied. The browser is likely open right now.")
            print("Please close all browser windows and background processes before running this script.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
    else:
        print(f"\nBrowser has been active within the last {days} days. No action taken.")

if __name__ == "__main__":
    clear_old_history(HISTORY_FILE_PATH, DAYS_THRESHOLD)