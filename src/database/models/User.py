from sqlalchemy import ForeignKey

from src.database.models.Account import Account
from src.database.models.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List, Optional


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column('id',primary_key=True,autoincrement='auto')
    name:Mapped[str] = mapped_column('name',nullable=False)
    lastname:Mapped[str]= mapped_column('lastname',nullable=False)
    phone: Mapped[str]=mapped_column('phone',nullable=False,unique=True)
    email:Mapped[str]=mapped_column('email',nullable=False,unique=True)
    password: Mapped[str]=mapped_column('password',nullable=False)
    address: Mapped[str]=mapped_column('address',nullable=False)
    isChild: Mapped[bool] = mapped_column('ischild',nullable=False,default=False)
    parent_id:Mapped[Optional[int]] = mapped_column('parent',ForeignKey('users.id'))
    parent: Mapped[Optional['User']] = relationship('User',remote_side=lambda:User.id,back_populates='children')
    children: Mapped[Optional[List['User']]] = relationship('User',back_populates= 'parent')

    account:Mapped['Account'] = relationship('Account')
    business:Mapped['Business'] = relationship('Business')

    def __init__(self, id:int=None,name:str=None,lastname:str=None,phone:str=None,email:str=None,password:str=None,address:str=None,isChild:bool=None,parent:int=None):
        self.name=name
        self.lastname=lastname
        self.phone=phone
        self.email=email
        self.password=password
        self.address=address
        self.isChild=isChild
        self.parent_id = parent
        super().__init__(id)
