from src.database.models.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from src.database.models.User import User
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey

class Tax(Base):
    __tablename__ = 'tax'
    id:Mapped[int] = mapped_column('id',primary_key=True)
    name:Mapped[str] = mapped_column('name',nullable=False)
    value:Mapped[float] = mapped_column('value',nullable=False,default=0.0)
    taxType:Mapped[float] = mapped_column('type',nullable=False,default='FIXED',comment='Possible values are \"FIXED\" OR \"PERCENTUAL\"')

    business_id = mapped_column('business_id',ForeignKey('business.id'))

    businessId:Mapped['Business'] = relationship('Business',back_populates='taxes')
