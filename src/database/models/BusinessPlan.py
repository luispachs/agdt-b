from src.database.models.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from src.database.models.Plan import Plan

class BusinessPlan(Base):
    __tablename__ = 'business_plan'
    id:Mapped[int] = mapped_column('id',primary_key=True)

    plan_id:Mapped[int] = mapped_column('plan_id',ForeignKey('planes.id'))
    business_id:Mapped[int] = mapped_column('business_id',ForeignKey('business.id'))

    plan:Mapped['Plan'] = relationship(lambda: Plan,back_populates='planBusiness')
    business:Mapped['Business'] =relationship('Business',back_populates='businessPlan')
