from flask import request
from sqlalchemy import select
from src.Utils.TokenExtract import TokenExtract
from src.Security.Hash.Jwt import JWT
def schedules():
    isValid = JWT.validate(TokenExtract(request.authorization))



def create():
    pass

def update():
    pass

def delete():
    pass