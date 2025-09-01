# Define the filename
filename = "example.txt"

# Open the file in write mode
with open(filename, "w") as file:
    # Write some text to the file
    file.write("Hello, this is a sample text written to the file.\n")
    file.write("This is the second line of text.\n")
    file.write("Goodbye!")

# The file is automatically closed when exiting the 'with' block
print(f"Text has been written to {filename}.")
