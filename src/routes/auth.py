import sys

from flask import request,jsonify
from src.Repository.Repository import Repository
from src.database.models.User import User
from src.database.models.Business import Business
from src.Security.Hash.Hash import Hash

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
        user = User( name=username[0],lastname= username[1],address= body['ownerAddress'],phone= body['ownerPhone'],email= body['ownerEmail'],password= body['ownerPassword'],isChild= False,parent= None)
        user.name =username[0]
        user.lastname = username[1]
        user.address =body['ownerAddress']
        user.phone = body['ownerPhone']
        user.email = body['ownerEmail']
        print(user.password)

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
        return {'data':body},200
    except Exception as ex:
        session.rollback()
        print(ex)
        return {'data':{'error':'Something Was Wrong - 500'}},500

