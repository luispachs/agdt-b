from src.database.models.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
class Service(Base):
    __tablename__ = 'services'

    id:Mapped[int] = mapped_column('id',primary_key=True)
    name:Mapped[str] = mapped_column('name',nullable=False)
    serviceValue:Mapped[float] =mapped_column('service_value',nullable=False,default=0.0)
    description: Mapped[str] = mapped_column('description',nullable=True)

    business_id = mapped_column(ForeignKey('business.id'))

    businessId: Mapped['Business'] = relationship('Business',back_populates='services')