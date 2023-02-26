import os
import shutil
import datetime

# Define the directory where the Excel files are located
dir_path = "D:\Python_Coding_Class\Python_50Days\Testdir"

# Get a list of all the Excel files in the directory
files = os.listdir(dir_path)

# Filter out any non-Excel files
files = [f for f in files if f.endswith(".xlsx")]

# Sort the list of files by modification time (newest first)
files.sort(key=lambda x: os.path.getmtime(os.path.join(dir_path, x)), reverse=True)

# Get the path of the most recently modified file
latest_file = os.path.join(dir_path, files[0])

# Define the format for the week range
week_range_format = "%Y-%m-%d to %Y-%m-%d"

# Calculate the start and end dates for the current week
today = datetime.date.today()
start_of_week = today - datetime.timedelta(days=today.weekday())
end_of_week = start_of_week + datetime.timedelta(days=6)

# Format the week range using the start and end dates
week_range = start_of_week.strftime("%Y-%m-%d") + " to " + end_of_week.strftime("%Y-%m-%d")

# Create the new filename by replacing the file extension with the week range
new_filename = os.path.splitext(latest_file)[0] + " " + week_range + os.path.splitext(latest_file)[1]

# Copy the file to the new filename
shutil.copyfile(latest_file, os.path.join(dir_path, new_filename))
