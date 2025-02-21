from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QMenuBar, QAction
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime Productivity App")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.title_label = QLabel("Bem-vindo ao Anime Productivity App!")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.start_button = QPushButton("Iniciar Pomodoro")
        self.start_button.clicked.connect(self.start_pomodoro)
        self.layout.addWidget(self.start_button)

        self.create_menu()

    def create_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Arquivo")

        exit_action = QAction("Sair", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        settings_action = QAction("Configurações", self)
        settings_action.triggered.connect(self.open_settings)
        file_menu.addAction(settings_action)

    def start_pomodoro(self):
        # Implementar lógica para iniciar o temporizador Pomodoro
        pass

    def open_settings(self):
        # Implementar lógica para abrir a tela de configurações
        pass