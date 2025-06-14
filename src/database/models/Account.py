from src.database.models.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
class Account(Base):
    __tablename__ = 'account'
    id:Mapped[int] = mapped_column('id',primary_key=True)
    permission_id:Mapped[int] = mapped_column('permission_id',ForeignKey('permissions.id'))
    permissionId:Mapped['Permission'] = relationship('Permission')
    user_id:Mapped[int] = mapped_column('user_id',ForeignKey('users.id'))
    userId:Mapped['User'] = relationship('User' ,back_populates='account')