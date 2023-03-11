import random
import string
import os

# Define a list of common boy's names
boy_names = ['Noah', 'Liam', 'Ethan', 'Oliver', 'Aiden', 'Caleb', 'Mason', 'Elijah', 'Logan', 'Lucas', 'Jackson', 'Jack', 'Michael', 'William', 'Benjamin', 'James', 'Daniel', 'Henry', 'Alexander', 'Jacob']

# Create a directory to store the text files
os.makedirs('boy_names', exist_ok=True)

# Generate 100 text files with random boy names
for i in range(1, 101):
    # Generate a random boy name from the list
    name = random.choice(boy_names)

    # Create a file name with the name and a random string of characters
    file_name = f'boy_names/{name}_{"".join(random.choices(string.ascii_lowercase, k=5))}.txt'

    # Create the text file and write the boy's name to it
    with open(file_name, 'w') as f:
        f.write(name)
