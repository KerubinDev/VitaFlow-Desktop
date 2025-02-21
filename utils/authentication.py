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