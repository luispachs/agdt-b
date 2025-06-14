from src.Repository.Repository import Repository
from sqlalchemy.dialects.postgresql import Insert
from src.database.models.Business import Business
class BusinessRepository(Repository):
    def insert(self,businessName:str,businessAddress:str,businessPhone,ownerId:int):
        business = Insert(Business).values(businessName=businessName,businessAddress=businessAddress,businessPhone = businessPhone,owner_id=ownerId)
        result = self.conn.execute(business)
        return  result.inserted_primary_key