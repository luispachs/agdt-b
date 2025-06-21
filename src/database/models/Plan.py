
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
    monthy:Mapped[float] = mapped_column('monthly',nullable=False,default=0.0)
    yearly:Mapped[float] = mapped_column('yearly',nullable=False,default=0.0)
    headSquareNumber:Mapped[int] =mapped_column('head_square_number',nullable=False,default=1)
    planBusiness:Mapped[List['BusinessPlan']] = relationship('BusinessPlan',back_populates='plan')


    def __init__(self,id:int=None,name:str=None,value:float=0.0,monthly:float=0.0,yearly:float=0.0):
        self.name=name
        self.value=value
        self.monthly=monthly
        self.yearly=yearly
        super().__init__(id)