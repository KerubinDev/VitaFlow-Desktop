from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QCalendarWidget
from utils.notifications import show_notification
from datetime import datetime, timedelta

class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Utiliza QGridLayout para melhor responsividade
        grid = QGridLayout()
        
        # Título centralizado
        title = QLabel("Dashboard - Anime Productivity")
        title.setObjectName("dashboardTitle")
        title.setAlignment(QtCore.Qt.AlignCenter)
        grid.addWidget(title, 0, 0, 1, 2)

        # Calendário
        self.calendar = QCalendarWidget()
        grid.addWidget(self.calendar, 1, 0)

        # Estatísticas
        self.stats_label = QLabel("Estatísticas de produtividade")
        grid.addWidget(self.stats_label, 1, 1)

        self.setLayout(grid)

class Dashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard - Anime Productivity App")
        self.setGeometry(100, 100, 1024, 768)
        self.init_ui()
        self.pomodoro_timer = None
        self.is_timer_running = False

    def init_ui(self):
        # Layout responsivo com QGridLayout
        grid = QtWidgets.QGridLayout()

        # Calendário posicionado à esquerda
        self.calendar = QtWidgets.QCalendarWidget(self)
        grid.addWidget(self.calendar, 0, 0, 2, 1)

        # Lista de tarefas à direita (parte superior)
        self.task_list = QtWidgets.QListWidget(self)
        grid.addWidget(self.task_list, 0, 1)

        # Controles Pomodoro na parte inferior direita
        pomodoro_layout = QtWidgets.QVBoxLayout()
        self.start_timer_button = QtWidgets.QPushButton("Iniciar Pomodoro", self)
        self.start_timer_button.clicked.connect(self.start_pomodoro)
        pomodoro_layout.addWidget(self.start_timer_button)
        self.timer_label = QtWidgets.QLabel("Tempo restante: 25:00", self)
        pomodoro_layout.addWidget(self.timer_label)
        grid.addLayout(pomodoro_layout, 1, 1)

        self.setLayout(grid)

    def start_pomodoro(self):
        if not self.is_timer_running:
            self.is_timer_running = True
            self.remaining_time = 25 * 60  # 25 minutos
            self.update_timer()
            self.pomodoro_timer = QtCore.QTimer(self)
            self.pomodoro_timer.timeout.connect(self.update_timer)
            self.pomodoro_timer.start(1000)  # Atualiza a cada segundo

    def update_timer(self):
        if self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.timer_label.setText(f"Tempo restante: {minutes:02}:{seconds:02}")
            self.remaining_time -= 1
        else:
            self.pomodoro_timer.stop()
            self.is_timer_running = False
            self.timer_label.setText("Tempo esgotado!")
            show_notification("Pomodoro", "Tempo esgotado! Hora de uma pausa!")

    def add_task(self, task):
        self.task_list.addItem(task)

    def update_calendar(self):
        # Implementar a lógica para atualizar o calendário com tarefas
        pass

    def generate_report(self):
        # Implementar a lógica para gerar relatórios em PDF
        pass