from src.database.models.Base import Base
from src.database.models.Role import Role
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey

class Permission(Base):
    __tablename__ = 'permissions'
    id:Mapped[int] = mapped_column('id',primary_key=True)
    canCreateUser:Mapped[bool] = mapped_column('can_create_user',default=False,nullable=False)
    canEditUser:Mapped[bool] = mapped_column('can_edit_user',default=False,nullable=False)
    canDeleteUser:Mapped[bool] = mapped_column('can_delete_user',default=False,nullable=False)
    canCreateService:Mapped[bool] = mapped_column('can_create_service',default=False,nullable=False)
    canEditService:Mapped[bool] = mapped_column('can_edit_service',default=False,nullable=False)
    canDeleteService:Mapped[bool] = mapped_column('can_delete_service',default=False,nullable=False)
    canCreateModification:Mapped[bool] = mapped_column('can_create_modification',default=False,nullable=False)
    canEditModification:Mapped[bool] = mapped_column('can_edit_modification',default=False,nullable=False)
    canDeleteModification:Mapped[bool] = mapped_column('can_delete_modification',default=False,nullable=False)
    canGenerateReport:Mapped[bool] = mapped_column('can_generate_modification',default=False,nullable=False)
    canLookService:Mapped[bool] = mapped_column('can_look_service',default=False,nullable=False)

    business_id = mapped_column('business_id',ForeignKey('business.id'))

    businessId:Mapped['Business'] = relationship('Business',back_populates='permissions')
    role:Mapped['Role'] = relationship(lambda :Role,back_populates='permissionId')