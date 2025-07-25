from src.Repository.Repository import Repository
from sqlalchemy.dialects.postgresql import Insert
from sqlalchemy import Select
from src.database.models.Business import Business
class BusinessRepository(Repository):
    def insert(self,businessName:str,businessAddress:str,businessPhone,ownerId:int):
        business = Insert(Business).values(businessName=businessName,businessAddress=businessAddress,businessPhone = businessPhone,owner_id=ownerId)
        result = self.conn.execute(business)
        return  result.inserted_primary_key
    
    def getByUserId(self,userId:int):
        session = self.getSession()
        stmt =  Select(Business).where(Business.ownerId == userId)
        business = session.execute(stmt)
        if business is None:
            return None
        return business