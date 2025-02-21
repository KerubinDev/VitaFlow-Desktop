import unittest
from gui.login import LoginWidget
from gui.dashboard import DashboardWidget
from utils.authentication import hash_password, verify_password
from database.connection import create_connection

class TestApp(unittest.TestCase):

    def setUp(self):
        # Cria uma conexão com um banco de dados de teste
        self.connection = create_connection('test_database.db')
        # Instancia os widgets de login e dashboard
        self.login = LoginWidget()
        self.dashboard = DashboardWidget()

    def test_hash_password(self):
        password = "test_password"
        hashed = hash_password(password)
        self.assertNotEqual(password, hashed)
        self.assertTrue(verify_password(password, hashed))

    def test_login_valid_user(self):
        # Configuração dos valores de login para um usuário válido
        self.login.user_input.setText("valid_user")
        self.login.pass_input.setText("valid_password")
        # O método validate_user deve retornar True para um usuário válido
        result = self.login.validate_user()  # Método a ser implementado em LoginWidget
        self.assertTrue(result)

    def test_login_invalid_user(self):
        self.login.user_input.setText("invalid_user")
        self.login.pass_input.setText("invalid_password")
        result = self.login.validate_user()  # Método a ser implementado em LoginWidget
        self.assertFalse(result)

    def test_dashboard_progress(self):
        # Carrega os dados de um usuário para testar o dashboard
        self.dashboard.load_user_data("valid_user")  # Método a ser implementado em DashboardWidget
        progress = self.dashboard.get_progress()       # Método a ser implementado em DashboardWidget
        self.assertIsInstance(progress, dict)

    def tearDown(self):
        self.connection.close()

if __name__ == '__main__':
    unittest.main()