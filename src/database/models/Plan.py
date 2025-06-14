
from src.database.models.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey

class Plan(Base):
    __tablename__ = 'planes'
    id:Mapped[int] = mapped_column('id',primary_key=True)
    name:Mapped[str] = mapped_column('name',nullable=False)

    value:Mapped[float] = mapped_column('value',nullable=False,default=0.0)

    frequency:Mapped[str] = mapped_column('frequency',nullable=False,default='MONTHLY')
    planBusiness:Mapped[List['BusinessPlan']] = relationship('BusinessPlan',back_populates='plan')


    def __init__(self,id:int=None,name:str=None,value:float=0.0,frequency:str='FREE'):
        self.name=name
        self.value=value
        self.frequency=frequency
        super().__init__(id)