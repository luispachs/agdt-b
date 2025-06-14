
from src.database.models.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey

class Modification(Base):
    __tablename__ =  'modification'
    id:Mapped[int] = mapped_column('id',primary_key=True)
    name:Mapped[str] = mapped_column('name',nullable=False,unique=True)
    price:Mapped[float] = mapped_column('price',nullable=False,default=0.0)
    business_id =mapped_column('business_id',ForeignKey('business.id'))
    businessId:Mapped['Business'] =relationship('Business',back_populates='modifications')