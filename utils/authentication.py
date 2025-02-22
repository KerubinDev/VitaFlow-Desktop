import bcrypt

def hash_password(password: str) -> str:
    """
    Gera um hash para a senha utilizando bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """
    Verifica se a senha fornecida corresponde ao hash armazenado.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def authenticate_user(username: str, password: str) -> bool:
    """
    Autentica o usuário com base nas credenciais fornecidas.
    Este exemplo utiliza dados fixos para validação.
    Em produção, a verificação deve ser realizada consultando o banco de dados.
    """
    # Exemplo de credenciais válidas para teste:
    valid_credentials = {
        "valid_user": "valid_password"
    }
    
    if username in valid_credentials:
        return password == valid_credentials[username]
    return False