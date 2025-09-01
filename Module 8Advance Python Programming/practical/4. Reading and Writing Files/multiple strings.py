# Define the filename and the list of strings to write
filename = 'multiple_strings.txt'
strings_to_write = [
    'First line of text.',
    'Second line of text.',
    'Third line of text.',
    'Fourth line of text.'
]

# Open the file in write mode
with open(filename, 'w') as file:
    # Write each string to the file, followed by a newline
    for string in strings_to_write:
        file.write(string + '\n')

print(f'Successfully written multiple strings to {filename}')
