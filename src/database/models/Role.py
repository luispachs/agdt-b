from src.database.models.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey

class Role(Base):
    __tablename__ = 'role'
    id:Mapped[int] = mapped_column('id',primary_key=True)
    name:Mapped[str] = mapped_column('name',nullable=False)

    permission_id = mapped_column('permission_id',ForeignKey('permissions.id'))

    permissionId:Mapped['Permission'] = relationship('Permission',back_populates= 'role')