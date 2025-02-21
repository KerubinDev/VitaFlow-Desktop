from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QVBoxLayout

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
        layout = QVBoxLayout()
        
        # Título das configurações
        title = QLabel("Configurações")
        layout.addWidget(title)

        # Exemplo: Opção para seleção de tema
        theme_label = QLabel("Selecione o tema:")
        layout.addWidget(theme_label)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["dark", "light"])
        layout.addWidget(self.theme_combo)

        self.setLayout(layout)