from plyer import notification

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Anime Productivity App',
        timeout=10  # Notificação será exibida por 10 segundos
    )

def notify_pomodoro_start():
    show_notification("Pomodoro Iniciado", "Vamos lá! Foco, dattebayo!")

def notify_pomodoro_end():
    show_notification("Pomodoro Finalizado", "Hora da pausa! Relaxe um pouco!")