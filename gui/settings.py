from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QVBoxLayout, QPushButton, QHBoxLayout

class Settings:
    def __init__(self):
        self.theme = "dark"  # Padrão: tema escuro
        self.notifications_enabled = True  # Notificações ativadas por padrão

    def toggle_theme(self):
        if self.theme == "dark":
            self.theme = "light"
        else:
            self.theme = "dark"

    def set_notifications(self, enabled):
        self.notifications_enabled = enabled

    def get_settings(self):
        return {
            "theme": self.theme,
            "notifications_enabled": self.notifications_enabled
        }

class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setObjectName("settingsWidget")
        layout = QVBoxLayout()

        title = QLabel("Configurações")
        title.setObjectName("settingsTitle")
        layout.addWidget(title)

        # Seleção de tema com layout horizontal
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Selecione o tema:")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["dark", "light"])
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        layout.addLayout(theme_layout)

        self.save_button = QPushButton("Salvar Configurações")
        layout.addWidget(self.save_button)

        self.setLayout(layout)