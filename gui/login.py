from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import pyqtSignal
from utils.authentication import authenticate_user

class LoginWidget(QWidget):
    # Sinal disparado quando o login é bem-sucedido
    login_success = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Título da tela de login
        title_label = QLabel("Login - Anime Productivity")
        layout.addWidget(title_label)

        # Campo para o nome do usuário
        user_layout = QHBoxLayout()
        user_label = QLabel("Usuário:")
        self.user_input = QLineEdit()
        user_layout.addWidget(user_label)
        user_layout.addWidget(self.user_input)
        layout.addLayout(user_layout)

        # Campo para a senha
        pass_layout = QHBoxLayout()
        pass_label = QLabel("Senha:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        pass_layout.addWidget(pass_label)
        pass_layout.addWidget(self.pass_input)
        layout.addLayout(pass_layout)

        # Botão para efetuar login
        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        # Exemplo simplificado de validação de login.
        # Em produção, deve-se validar os dados com o banco de dados e usar hash na senha.
        if self.user_input.text() and self.pass_input.text():
            self.login_success.emit()