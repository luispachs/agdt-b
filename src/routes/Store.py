from flask import request
from src.Security.Hash.Jwt import JWT
from src.Utils.TokenExtract import TokenExtract
from src.Utils.GetUser import GetUser
from src.Repository.BusinessRepository import BusinessRepository
def getAll():
    token = TokenExtract(request.authorization)
    claim = JWT.validate(token)
 
    user =  GetUser(claim)
    print(user.id)
    if user is None:
        return {'message':'Unauthorize'},401
    if user.isChild:
        user = user.parent
    businessRepository = BusinessRepository()
    business = businessRepository.getByUserId(user.id)
    return {'business':business},200
    