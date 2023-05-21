import chip
import datetime

# App
chip_data = chip.get()
chip_time = chip_data["time"]

current_time = datetime.datetime.now()
time_diff = current_time - chip_time

print(f"Version: {chip_data['version']}")
print(f"Private Id: {chip_data['privateIdentifier']}")
print(f"Public Id:  {chip_data['publicIdentifier']}")
print(f"Transactions: {chip_data['transactions']}")
print(f"Time: {chip_time}")
print(f"Time difference: {time_diff}")

if time_diff.total_seconds() > 3:
    print("WARNING: TIME DIFFERENCE OVER SAFE LIMIT")
