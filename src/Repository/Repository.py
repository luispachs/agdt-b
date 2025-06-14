from src.database.connection.DatabaseConnection import  DatabaseConnection
from sqlalchemy.orm import sessionmaker

class Repository:
    conn = None
    session = None
    def  __init__(self):
        db = DatabaseConnection()
        self.conn = db.get()
    def save(self):
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def getSession(self):
        self.session = sessionmaker(bind=self.conn.engine)
        return self.session()