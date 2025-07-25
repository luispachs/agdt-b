from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select
from src.Repository.Repository import Repository
from src.database.models.User import User
from  src.Logger.Log import Log

class UserRepository(Repository):
    def insert(self,name:str,lastname:str,phone:str,email:str,password:str,address:str,isChild:bool=True,parent:int=None):
        stmt = insert(User).values(name=name,lastname=lastname,phone=phone,email=email,password=password,address=address,isChild=isChild,parent_id=parent)
        result = self.conn.execute(stmt)
        data = result.inserted_primary_key
        return data

    def getByEmail(self,email:str):
        try:
            session = Repository().getSession()
            stmt = select(User).where(User.email == email)
            user = session.execute(stmt)
            if user is None:
                return None
            return user.scalars().first()
        except Exception as e:
            print(e)

    def getById(self,id:int):
        stmt = select(User).where(User.id == id)
        conn = self.getSession()
        user = conn.execute(stmt)
        if user is None:
            return None
        return user.first()
        




