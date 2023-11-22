import tkinter as tk
from tkinter import ttk
import mysql.connector

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_member"
)
cursor = db.cursor()

class UserCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User CRUD App. Developed by: Mohammad Nayan.")

        self.create_table()
        self.create_gui()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(create_table_query)
        db.commit()

    def create_gui(self):
        # Labels
        ttk.Label(self.root, text="Name:").grid(row=0, column=0)
        ttk.Label(self.root, text="Email:").grid(row=1, column=0)

        # Entry Fields
        self.name_entry = ttk.Entry(self.root)
        self.email_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)
        self.email_entry.grid(row=1, column=1)

        # Buttons
        ttk.Button(self.root, text="Create", command=self.create_user).grid(row=2, column=0)
        ttk.Button(self.root, text="Read", command=self.read_users).grid(row=2, column=1)
        ttk.Button(self.root, text="Update", command=self.update_user).grid(row=2, column=2)
        ttk.Button(self.root, text="Delete", command=self.delete_user).grid(row=2, column=3)

        # User List
        self.user_listbox = tk.Listbox(self.root)
        self.user_listbox.grid(row=3, column=0, columnspan=4)

    def create_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()

        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, email))
        db.commit()
        self.clear_entries()
        self.read_users()

    def read_users(self):
        self.user_listbox.delete(0, tk.END)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            self.user_listbox.insert(tk.END, f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    def update_user(self):
        selected_user = self.get_selected_user()
        if selected_user:
            name = self.name_entry.get()
            email = self.email_entry.get()
            update_query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
            cursor.execute(update_query, (name, email, selected_user[0]))
            db.commit()
            self.clear_entries()
            self.read_users()

    def delete_user(self):
        selected_user = self.get_selected_user()
        if selected_user:
            delete_query = "DELETE FROM users WHERE id = %s"
            cursor.execute(delete_query, (selected_user[0],))
            db.commit()
            self.clear_entries()
            self.read_users()

    def get_selected_user(self):
        try:
            selected_user = self.user_listbox.get(self.user_listbox.curselection())
            user_id = int(selected_user.split(',')[0].split(':')[1])
            return (user_id,)
        except Exception as e:
            return None

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserCRUDApp(root)
    root.mainloop()
