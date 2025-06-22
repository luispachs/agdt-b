from src.database.models.Base import Base
from src.database.models.Modification import Modification
from src.database.models.Permission import Permission
from src.database.models.BusinessPlan import BusinessPlan
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from datetime import datetime
class Business(Base):
    __tablename__ = 'business'
    id:Mapped[int] =mapped_column('id',primary_key=True)
    businessName:Mapped[str] =mapped_column('business_name',nullable=False,unique=True)
    businessAddress:Mapped[str] = mapped_column('business_address',nullable=False,unique=True)
    businessPhone:Mapped[str] = mapped_column('business_phone',unique=True,nullable=False)
    user_id:Mapped[int] = mapped_column('owner_id',ForeignKey('users.id'))
    paymentFrecuency:Mapped[str] = mapped_column('payment_frequency',nullable=True)
    startService:Mapped[datetime] = mapped_column('start_services',nullable=True)
    ownerId:Mapped['User'] = relationship('User',back_populates='business')

    modifications:Mapped[List['Modification']] = relationship(back_populates='businessId')

    permissions:Mapped[List['Permission']] = relationship(back_populates='businessId')
    businessPlan: Mapped[['BusinessPlan']] = relationship(lambda :BusinessPlan,back_populates='business')

    def __init__(self,id:int=None,businessName:str=None,businessAddress:str=None,businessPhone:str=None,ownerId:int=None):
        self.businessName=businessName
        self.businessAddress=businessAddress
        self.businessPhone=businessPhone
        super().__init__(id)
