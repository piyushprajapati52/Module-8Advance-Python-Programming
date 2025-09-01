
# Define the filename
filename = 'example.txt'

# Open the file in write mode and write some text
with open(filename, 'w') as file:
    file.write('This is a sample text.')

# Open the file in read mode
with open(filename, 'r') as file:
    # Read the first 10 characters
    content = file.read(10)
    
    # Check the current position of the file cursor
    position = file.tell()
    
    # Print the content read and the current cursor position
    print(f'Content read: "{content}"')
    print(f'Current position of the file cursor: {position}')
