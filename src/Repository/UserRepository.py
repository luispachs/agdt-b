from sqlalchemy.dialects.postgresql import insert

from src.Repository.Repository import Repository
from src.database.models.User import User

class UserRepository(Repository):
    def insert(self,name:str,lastname:str,phone:str,email:str,password:str,address:str,isChild:bool=True,parent:int=None):
        stmt = insert(User).values(name=name,lastname=lastname,phone=phone,email=email,password=password,address=address,isChild=isChild,parent_id=parent)
        result = self.conn.execute(stmt)
        data = result.inserted_primary_key
        return data




