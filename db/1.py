import mysql.connector

# 1) Connect without selecting a database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS 25_MWF_python")
cursor.close()
conn.close()

# 2) Reconnect and select the database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="25_MWF_python",
)
cursor = conn.cursor()
print("database created/selected successfully")


# 3) Create a table and perform CRUD operations
cursor.execute("""
               CREATE TABLE IF NOT EXISTS student(
                   id INT  AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(50),
                   age INT,
                   department VARCHAR(50)
               )
               """)
print("table created successfully")

# 4) Insert data into the table
cursor.execute("INSERT INTO student(name,age,department) Values('Krishna',21,'Computer')")
cursor.execute("INSERT INTO student(name,age,department) Values('Krish',20,'CEO')")
cursor.execute("INSERT INTO student(name,age,department) Values('Aashta',22,'Developer')")
cursor.execute("INSERT INTO student(name,age,department) Values('Urja',25,'Finance')")
cursor.execute("INSERT INTO student(name,age,department) Values('Yash',19,'Sales')")

conn.commit()
print("data inserted successfully")

# 5) Delete data from the table
cursor.execute("DELETE FROM student WHERE name='Krishna'")
conn.commit()
print("data deleted successfully")


# 6) Update data in the table
cursor.execute("UPDATE student SET age=23 WHERE name='Krish'")
conn.commit()
print("data updated successfully")


cursor.close()
conn.close()
