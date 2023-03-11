import os

# Define the folder name pattern
folder_pattern = '{}A'

# Define the number of folders to create
num_folders = 100

# Create the parent directory to store all the folders
parent_directory = 'all'
os.makedirs(parent_directory, exist_ok=True)

# Generate the folder names and create the folders
for i in range(1, num_folders+1):
    # Generate the folder name
    folder_name = folder_pattern.format(i)
    
    # Create the folder
    folder_path = os.path.join(parent_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
