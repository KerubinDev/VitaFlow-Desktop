from plyer import notification

def send_notification(title: str, message: str):
    """
    Envia uma notificação utilizando plyer.
    """
    notification.notify(
        title=title,
        message=message,
        app_name="Anime Productivity",
        timeout=10  # Duração da notificação em segundos
    )

# Adiciona um alias para compatibilidade
show_notification = send_notification

def notify_pomodoro_start():
    send_notification("Pomodoro Iniciado", "Vamos lá! Foco, dattebayo!")

def notify_pomodoro_end():
    send_notification("Pomodoro Finalizado", "Hora da pausa! Relaxe um pouco!")