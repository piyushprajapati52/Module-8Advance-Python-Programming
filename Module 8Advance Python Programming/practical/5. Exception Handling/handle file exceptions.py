try:
    # Open the file in read mode
    file = open('example.txt', 'r')
    
    # Read the contents of the file
    content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except IOError:
    print("Error: An I/O error occurred while handling the file.")
finally:
    # Ensure the file is closed if it was opened
    try:
        file.close()
        print("File has been closed.")
    except NameError:
        # file was never opened
        print("File was not opened, so no need to close.")