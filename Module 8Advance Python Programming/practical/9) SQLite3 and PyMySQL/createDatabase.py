# 1) Write a Python program to create a database and a table using SQLite3. 
# 2)Write a Python program to insert data into an SQLite3 database and fetch it.

import pymysql

host = 'localhost'
user = 'root'
password = '1234'

connection = pymysql.connect(host=host, user=user, password=password)
cursor = connection.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS pymsql1")
cursor.execute("USE pymsql1")

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT,
    admission_date DATE
)
''')

# Insert data
cursor.execute('''
INSERT INTO students (name, email, age, admission_date)
VALUES ('Piyush', 'piyush@gmail.com', 22, CURRENT_DATE)
''')

# Commit the changes
connection.commit()

# Fetch data
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close
cursor.close()

connection.close()
