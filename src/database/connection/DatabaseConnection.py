from sqlalchemy import create_engine
import os
class DatabaseConnection:
    engine=None
    conn =None
    def __init__(self):
        self.engine = create_engine(f'postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}')

    def get(self):
        self.conn = self.engine.connect()
        return self.conn
