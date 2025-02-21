"""
Módulo para gerenciar a conexão com o banco de dados SQLite.
Este módulo cria/conecta ao banco de dados, configurando as chaves estrangeiras.
"""

import sqlite3
import os

DATABASE_FILENAME = "anime_productivity.db"  # Nome do arquivo de banco de dados

class DatabaseConnection:
    def __init__(self, db_path=DATABASE_FILENAME):
        """
        Inicializa a conexão definindo o caminho completo do arquivo de banco.
        """
        self.db_path = os.path.join(os.getcwd(), db_path)
        self.connection = None

    def connect(self):
        """
        Estabelece a conexão com o banco de dados e ativa as chaves estrangeiras.
        """
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.execute("PRAGMA foreign_keys = 1")  # Habilita chaves estrangeiras
            print("Conexão estabelecida com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar com o banco de dados: {e}")

    def get_connection(self):
        """
        Retorna a conexão ativa com o banco de dados, conectando se necessário.
        """
        if self.connection is None:
            self.connect()
        return self.connection

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.connection:
            self.connection.close()
            print("Conexão fechada.")