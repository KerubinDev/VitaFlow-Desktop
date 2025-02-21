from PyQt5 import QtWidgets, QtGui
from utils.authentication import authenticate_user

class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - Anime Productivity App")
        self.setGeometry(100, 100, 300, 200)
        self.init_ui()

    def init_ui(self):
        self.layout = QtWidgets.QVBoxLayout()

        self.username_label = QtWidgets.QLabel("Username:")
        self.layout.addWidget(self.username_label)

        self.username_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.username_input)

        self.password_label = QtWidgets.QLabel("Password:")
        self.layout.addWidget(self.password_label)

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)
        self.layout.addWidget(self.login_button)

        self.error_message = QtWidgets.QLabel("")
        self.error_message.setStyleSheet("color: red;")
        self.layout.addWidget(self.error_message)

        self.setLayout(self.layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if authenticate_user(username, password):
            self.error_message.setText("Login successful!")
            # Proceed to the main application window
        else:
            self.error_message.setText("Invalid username or password.")