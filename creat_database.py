import sqlite3

def create_database():
    connection = sqlite3.connect("anime_productivity.db")
    cursor = connection.cursor()

    # Criação das tabelas
    sql_commands = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            access_level TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            deadline DATETIME,
            status TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            start_time DATETIME,
            end_time DATETIME,
            session_type TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS pomodoro_config (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            work_time INTEGER DEFAULT 25,
            break_time INTEGER DEFAULT 5,
            block_distractions INTEGER DEFAULT 1,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS app_config (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            theme TEXT DEFAULT 'dark',
            notifications_enabled INTEGER DEFAULT 1,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );
        """
    ]

    for command in sql_commands:
        cursor.execute(command)

    # Inserção de dados padrão
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO users (username, password_hash, email, access_level) 
        VALUES ('admin', '$2b$12$KIXQjyoYt6MAe4iSIJCEIu0C/yLNiIudHsd9HiVy8QyTga3R4Q2Hy', 'admin@example.com', 'admin')
        """)
    
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE user_id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO tasks (user_id, title, description, deadline, status) 
        VALUES (1, 'Primeira Tarefa', 'Exemplo de tarefa padrão', '2025-12-31 23:59:59', 'pendente')
        """)
    
    cursor.execute("SELECT COUNT(*) FROM study_sessions WHERE user_id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO study_sessions (user_id, start_time, end_time, session_type) 
        VALUES (1, '2025-02-21 10:00:00', '2025-02-21 10:25:00', 'pomodoro')
        """)
    
    cursor.execute("SELECT COUNT(*) FROM pomodoro_config WHERE user_id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO pomodoro_config (user_id, work_time, break_time, block_distractions) 
        VALUES (1, 25, 5, 1)
        """)
    
    cursor.execute("SELECT COUNT(*) FROM app_config WHERE user_id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO app_config (user_id, theme, notifications_enabled) 
        VALUES (1, 'dark', 1)
        """)
    
    connection.commit()
    connection.close()
    print("Banco de dados 'anime_productivity.db' criado e populado com sucesso.")

if __name__ == "__main__":
    create_database()
