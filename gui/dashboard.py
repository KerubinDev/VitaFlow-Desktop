from PyQt5 import QtWidgets, QtGui, QtCore
from utils.notifications import show_notification
from datetime import datetime, timedelta

class Dashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard - Anime Productivity App")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()
        self.pomodoro_timer = None
        self.is_timer_running = False

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.calendar = QtWidgets.QCalendarWidget(self)
        layout.addWidget(self.calendar)

        self.task_list = QtWidgets.QListWidget(self)
        layout.addWidget(self.task_list)

        self.start_timer_button = QtWidgets.QPushButton("Iniciar Pomodoro", self)
        self.start_timer_button.clicked.connect(self.start_pomodoro)
        layout.addWidget(self.start_timer_button)

        self.timer_label = QtWidgets.QLabel("Tempo restante: 25:00", self)
        layout.addWidget(self.timer_label)

        self.setLayout(layout)

    def start_pomodoro(self):
        if not self.is_timer_running:
            self.is_timer_running = True
            self.remaining_time = 25 * 60  # 25 minutes in seconds
            self.update_timer()
            self.pomodoro_timer = QtCore.QTimer(self)
            self.pomodoro_timer.timeout.connect(self.update_timer)
            self.pomodoro_timer.start(1000)  # Update every second

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