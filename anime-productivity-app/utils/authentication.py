from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    """Gera um hash seguro para a senha fornecida."""
    return generate_password_hash(password)

def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verifica se a senha fornecida corresponde ao hash armazenado."""
    return check_password_hash(stored_password, provided_password)