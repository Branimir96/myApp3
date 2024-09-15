import sqlite3

# Create or connect to a SQLite database
conn = sqlite3.connect('website.db')  # This will create a new SQLite database file 'example.db'
cursor = conn.cursor()

# Create a new table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    author TEXT NOT NULL,
    publication_date TEXT,
    article TEXT 
)
''')

# Insert data into the table
users = [
    (1, 'John Doe', 14-9-2024 , 'AAA'),
    (2, 'Jane Smith', 14-9-2024, 'BBB'),
    (3, 'Sam Wilson', 14-9-2024, 'CCC')
]

# Use 'executemany' to insert multiple rows at once
cursor.executemany('''
INSERT OR IGNORE INTO users (id, author, publication_date, article) 
VALUES (?, ?, ?, ?)
''', users)



# Commit the transaction
conn.commit()

# Retrieve and display data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
