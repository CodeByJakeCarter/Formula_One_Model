from sqlalchemy.orm import sessionmaker
from f1model.db.engine import engine

session_factory = sessionmaker(bind=engine)