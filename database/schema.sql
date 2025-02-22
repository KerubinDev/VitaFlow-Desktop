-- Script SQL para criação das tabelas do banco de dados.

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    access_level TEXT NOT NULL
);

-- Tabela de tarefas
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    deadline DATETIME,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Tabela de sessões de estudo
CREATE TABLE IF NOT EXISTS study_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    start_time DATETIME,
    end_time DATETIME,
    session_type TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Tabela de configuração do Pomodoro
CREATE TABLE IF NOT EXISTS pomodoro_config (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    work_time INTEGER DEFAULT 25,  -- tempo de trabalho em minutos
    break_time INTEGER DEFAULT 5,    -- tempo de pausa em minutos
    block_distractions INTEGER DEFAULT 1,  -- 1 para bloquear distrações
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Tabela de configuração do aplicativo
CREATE TABLE IF NOT EXISTS app_config (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    theme TEXT DEFAULT 'dark',
    notifications_enabled INTEGER DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- --------------------------------------------------------
-- Inserção de dados padrão (Seed Data)
-- --------------------------------------------------------

-- Insere um usuário admin (password "admin" com hash gerado via bcrypt)
INSERT INTO users (username, password_hash, email, access_level) VALUES 
('admin', '$2b$12$KIXQjyoYt6MAe4iSIJCEIu0C/yLNiIudHsd9HiVy8QyTga3R4Q2Hy', 'admin@example.com', 'admin');

-- Insere uma tarefa padrão para o admin
INSERT INTO tasks (user_id, title, description, deadline, status) VALUES 
(1, 'Primeira Tarefa', 'Exemplo de tarefa padrão', '2025-12-31 23:59:59', 'pendente');

-- Insere uma sessão de estudo padrão para o admin
INSERT INTO study_sessions (user_id, start_time, end_time, session_type) VALUES 
(1, '2025-02-21 10:00:00', '2025-02-21 10:25:00', 'pomodoro');

-- Insere a configuração do Pomodoro para o admin
INSERT INTO pomodoro_config (user_id, work_time, break_time, block_distractions) VALUES 
(1, 25, 5, 1);

-- Insere a configuração do aplicativo para o admin
INSERT INTO app_config (user_id, theme, notifications_enabled) VALUES 
(1, 'dark', 1);