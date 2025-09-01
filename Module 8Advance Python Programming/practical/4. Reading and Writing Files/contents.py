# Define the filename
filename = 'output.txt'

# Open the file in read mode
with open(filename, 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Print the contents to the console
print(contents)
