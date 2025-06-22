from flask import request,jsonify,redirect
from src.Messages.Messages import Messages
from src.Repository.Repository import Repository
from src.Repository.UserRepository import UserRepository
from src.database.models.User import User
from src.database.models.Business import Business
from src.Security.Hash.Hash import Hash
from src.Security.Validators.StringValidator import StringValidator
from src.Exceptions.AgendateException import AgendateException
from src.Security.Validators.ValidatorException import ValidatorException
from src.Logger.Log import  Log
import sys
import os

def register():
    body = request.json
    session = Repository().getSession()
    try:
        session.begin()
        username = str(body['ownerName']).split(' ')
        if len(username)<2:
            return {'data':'username must be "name" "lastname"'},400
        if body['ownerPassword']!=body['ownerPasswordConfirm']:
            return {'data': "Password and Confirm Password aren't equal"},400
        #name= username[0],lastname= username[1],address= body['ownerAddress'],phone= body['ownerPhone'],email= body['ownerEmail'],password= body['ownerPassword'],isChild= False,parent= None
        user = User( name=username[0],lastname= username[1],address= body['ownerAddress'],phone= body['ownerPhone'],email= body['ownerEmail'],password= Hash().encryt(body['ownerPassword']),isChild= False,parent= None)
        user.name =username[0]
        user.lastname = username[1]
        user.address =body['ownerAddress']
        user.phone = body['ownerPhone']
        user.email = body['ownerEmail']

        user.isChild = False
        user.parent = None

        session.add(user)
        session.flush()

        business = Business(businessName= body['businessName'],businessAddress= body['businessAddress'],businessPhone= body['businessPhone'],ownerId= user.id)
        business.businessName = body['businessName']
        business.businessAddress = body['businessAddress']
        business.businessPhone = body['businessPhone']
        business.user_id = user.id

        session.add(business)
        session.commit()
        return {'data':Messages.getMessage(1001)},200
        #return redirect('/login',301)
    except Exception as ex:
        session.rollback()
        Log.error(message=str(ex),trace=ex.with_traceback(sys.exception().__traceback__))
        return {'data':{'error':AgendateException.getError(5000)}},500


def login():
    try:
        data = request.json
        validator = StringValidator()
        validator.validate(data['user-email'])
        email = validator.data()
        validator.validate(data['user-password'])
        password = validator.data()
        userRepository = UserRepository()
        user  = userRepository.getByEmail(email)
        print(user,email)
        if user is None:
            return {'data':AgendateException.getError(1000)},401

        hash = Hash()

        if  hash.validate(password,user.password) is False:
            return {'data':AgendateException.getError(1000)},401
        return {'data':Messages.getMessage(1000)} ,200

    except ValidatorException as ex:
        return {'data': AgendateException.getError(1001)}, 400
    except Exception as ex:
        Log.error(message=str(ex),trace=ex.with_traceback(sys.exception().__traceback__))
        return {'data':AgendateException.getError(5000)},500


def logout():
    return {'data':None}

def authorize():
    data  = request.json

    return {'data':None}