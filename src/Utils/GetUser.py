from src.Repository.UserRepository import UserRepository
from src.database.models.User import User
from authlib.jose import JWTClaims

def GetUser(claim:dict)->User|None:
    userRepository = UserRepository()
    return userRepository.getById(claim['id'])