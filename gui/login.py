from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import pyqtSignal
from utils.authentication import authenticate_user

class LoginWidget(QWidget):
    login_success = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("loginWidget")
        layout = QVBoxLayout()

        # Título com identidade anime
        title_label = QLabel("Bem-vindo ao Anime Productivity")
        title_label.setObjectName("loginTitle")
        title_label.setStyleSheet("font-size: 26px; font-weight: bold;")
        layout.addWidget(title_label)

        # Campo para usuário
        user_layout = QHBoxLayout()
        user_label = QLabel("Usuário:")
        self.user_input = QLineEdit()
        user_layout.addWidget(user_label)
        user_layout.addWidget(self.user_input)
        layout.addLayout(user_layout)

        # Campo para senha
        pass_layout = QHBoxLayout()
        pass_label = QLabel("Senha:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        pass_layout.addWidget(pass_label)
        pass_layout.addWidget(self.pass_input)
        layout.addLayout(pass_layout)

        # Botão de login com efeito hover definido no stylesheet
        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        # Validação simples para demonstração
        if self.user_input.text() and self.pass_input.text():
            self.login_success.emit()

    def validate_user(self):
        # Exemplo de validação (deve ser substituído por lógica real)
        if self.user_input.text() == "valid_user" and self.pass_input.text() == "valid_password":
            return True
        return False