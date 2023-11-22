import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QWidget

# Database connection setup
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_member"
)
cursor = db_connection.cursor()

class CRUDApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CRUD App")
        self.setGeometry(100, 100, 400, 400)

        # Create widgets
        self.name_label = QLabel("Name:")
        self.name_entry = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_entry = QLineEdit()
        self.create_button = QPushButton("Create")
        self.user_list = QListWidget()
        self.read_button = QPushButton("Read")
        self.update_button = QPushButton("Update")
        self.delete_button = QPushButton("Delete")

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_entry)
        layout.addWidget(self.create_button)
        layout.addWidget(self.user_list)
        layout.addWidget(self.read_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect button clicks to functions
        self.create_button.clicked.connect(self.create_user)
        self.read_button.clicked.connect(self.read_users)
        self.update_button.clicked.connect(self.update_user)
        self.delete_button.clicked.connect(self.delete_user)

    # Create
    def create_user(self):
        name = self.name_entry.text()
        email = self.email_entry.text()
        if name and email:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            db_connection.commit()
            self.name_entry.clear()
            self.email_entry.clear()

    # Read
    def read_users(self):
        self.user_list.clear()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            self.user_list.addItem(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    # Update
    def update_user(self):
        selected_item = self.user_list.currentItem()
        if selected_item:
            user_id = selected_item.text().split(":")[1].split(",")[0].strip()
            new_name = self.name_entry.text()
            new_email = self.email_entry.text()
            cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (new_name, new_email, user_id))
            db_connection.commit()
            self.read_users()

    # Delete
    def delete_user(self):
        selected_item = self.user_list.currentItem()
        if selected_item:
            user_id = selected_item.text().split(":")[1].split(",")[0].strip()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            db_connection.commit()
            self.read_users()

if __name__ == "__main__":
    app = QApplication([])
    window = CRUDApp()
    window.show()
    app.exec_()

# Close the cursor and database connection when the application is closed
cursor.close()
db_connection.close()
