import sqlite3
connection = sqlite3.connect("test.db")
print(connection.total_changes)

# Create the basic framework of your database¶
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS people (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT)")
cursor.execute("INSERT INTO example (id, name, age) VALUES (1, 'alice', 20)")
cursor.execute("INSERT INTO people (nombre, apellido) VALUES ('John', 'Smith')")
cursor.execute("INSERT INTO example (id, name, age) VALUES (2, 'bob', 30)")
cursor.execute("INSERT INTO example (id, name, age) VALUES (3, 'eve', 40)")
connection.commit()

# Read the data¶

cursor.execute("SELECT * FROM example")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Modify existing data¶

cursor.execute("DELETE FROM example WHERE id = 1")
cursor.execute("UPDATE example SET age = 31 WHERE id = 2")


# Use a place holder¶
# Direct SQL requests
cursor.execute("UPDATE example SET age = 31 WHERE id = 2")
# SQL requests with place holders
age_var = 31
id_var = 2
cursor.execute("UPDATE example SET age = ? WHERE id = ?", (age_var, id_var))

connection.commit()

# End the connection to your database¶
connection.close()
