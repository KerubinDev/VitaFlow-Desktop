from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///anime_productivity.db"  # URL para SQLite
# Para MySQL, a URL seria algo como: "mysql+pymysql://user:password@localhost/db_name"

def get_database_engine():
    engine = create_engine(DATABASE_URL)
    return engine

def get_session():
    engine = get_database_engine()
    Session = sessionmaker(bind=engine)
    return Session()