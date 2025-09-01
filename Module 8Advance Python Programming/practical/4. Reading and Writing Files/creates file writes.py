# Define the filename and the string to write
filename = 'output_file.txt'
string_to_write = 'This is the string that will be written to the file.'

# Open the file in write mode
with open(filename, 'w') as file:
    # Write the string to the file
    file.write(string_to_write)

print(f'Successfully written to {filename}')
