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