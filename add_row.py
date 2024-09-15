import sqlite3

# Connect to the existing database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Insert a new row with data into the users table
cursor.execute('''
INSERT INTO users (name, age, email, phone_number, address)
VALUES (?, ?, ?, ?, ?)
''', ('Branimir Rajcic', 28, 'brajcic@example.com', '555-123-4567', '789 cipriano Street'))

# Commit the transaction
conn.commit()

# Retrieve and display the table contents to verify the new row has been added
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Data after adding the new row:")
for row in rows:
    print(row)

# Close the connection
conn.close()
