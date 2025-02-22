import os
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QMenuBar, QAction, QStackedWidget
from PyQt5.QtCore import Qt
from gui.login import LoginWidget
from gui.dashboard import Dashboard, DashboardWidget
from gui.settings import SettingsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime Productivity")
        self.setGeometry(100, 100, 1024, 768)
        self.load_stylesheet()

        # Cria um QStackedWidget para gerenciar as telas (login, dashboard, configurações)
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Instanciar os widgets de cada tela
        self.login_widget = LoginWidget()
        self.dashboard_widget = Dashboard()  # Tela completa com dashboard responsivo
        self.settings_widget = SettingsWidget()

        # Adiciona os widgets ao QStackedWidget
        self.stack.addWidget(self.login_widget)
        self.stack.addWidget(self.dashboard_widget)
        self.stack.addWidget(self.settings_widget)

        # Conecta o sinal de login bem-sucedido à transição para o dashboard
        self.login_widget.login_success.connect(self.show_dashboard)

    def load_stylesheet(self):
        # Carrega um stylesheet global para toda a aplicação (arquivo styles.qss na raiz do projeto)
        stylesheet_path = os.path.join(os.getcwd(), "styles.qss")
        if os.path.exists(stylesheet_path):
            with open(stylesheet_path, "r") as f:
                self.setStyleSheet(f.read())

    def show_dashboard(self):
        self.stack.setCurrentWidget(self.dashboard_widget)