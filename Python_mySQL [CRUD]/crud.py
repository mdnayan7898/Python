
import mysql.connector
import tkinter as tk

# Database connection setup
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_member"
)
cursor = db_connection.cursor()

# Tkinter window
root = tk.Tk()
root.title("User Management App. Developer: Mohammad Nayan")

# Create
def create_user():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db_connection.commit()
        name_entry.delete(0, "end")
        email_entry.delete(0, "end")
        read_users()

# Read
def read_users():
    user_listbox.delete(0, "end")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        user_listbox.insert("end", f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

# Delete
def delete_user():
    selected_user = user_listbox.get(user_listbox.curselection())
    user_id = selected_user.split(":")[1].split(",")[0]
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db_connection.commit()
    read_users()

# Tkinter widgets
name_label = tk.Label(root,  text="Name:")
name_label.pack()
name_entry = tk.Entry(root, width=100)
name_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root, width=100)
email_entry.pack()

create_button = tk.Button(root, text="Create User", command=create_user)
create_button.pack()

user_listbox = tk.Listbox(root, width=100, selectmode=tk.SINGLE)
user_listbox.pack()
read_users()

delete_button = tk.Button(root, text="Delete User", command=delete_user)
delete_button.pack()

# Run the Tkinter main loop
root.mainloop()

# Close the cursor and database connection when the application is closed
cursor.close()
db_connection.close()
