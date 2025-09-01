# Define the filename and the text to write
filename = 'output.txt'
text_to_write = 'This is some text written to the file.'

# Open the file in write mode
file = open(filename, 'w')

# Write the text to the file
file.write(text_to_write)

# Close the file
file.close()

print(f'Successfully written to {filename}')
