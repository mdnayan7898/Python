import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_member"
)

mycursor = mydb.cursor()
# Create Table
# mycursor.execute("CREATE TABLE members (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(255) NULL)")

# Insert single row
# sql = "INSERT INTO members (name, phone) VALUES (%s, %s)"
# val = ("Mohammad Nayan", "01690091590")
# mycursor.execute(sql, val)

# Insert Multiple Row
# sql = "INSERT INTO members (name, phone) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# Selecting data
mycursor.execute("SELECT * FROM members where id='1'")

myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

print(myresult.columns.name)

