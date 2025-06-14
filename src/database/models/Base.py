from sqlalchemy.orm import DeclarativeBase
from src.database.connection.DatabaseConnection import DatabaseConnection
class Base(DeclarativeBase):
    id=None
    def __init__(self,id=None):
        super().__init__()
        self.id=id
        db = DatabaseConnection()
        self.metadata.create_all(db.engine)