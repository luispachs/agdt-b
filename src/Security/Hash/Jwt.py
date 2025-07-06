from authlib.jose import jwt
import os
import datetime



class JWT :
    @staticmethod
    def serialize(payload:str)->str:
        certUrl = os.getenv('AGENDATE_DIR')
        cert = open(f"{certUrl}/private_agendate.pem",'rb')
        certContent = cert.read()
        PROTECTED = {'alg': 'RS256'}
        
        return jwt.encode(PROTECTED,payload,certContent)
        

    @staticmethod
    def deserialize(token:str)->list:
        certUrl = os.getenv('AGENDATE_DIR')
        cert = open(f"{certUrl}/public_agendate.pem",'rb')
        certContent = cert.read()
        PROTECTED = {'alg': 'RS256'}
        
        data = jwt.decode(bytes(token,encoding='utf-8'), certContent)
        return data

    @staticmethod
    def validate(token:str)->list:
        certUrl = os.getenv('AGENDATE_DIR')
        cert = open(f"{certUrl}/public_agendate.pem",'rb')
        certContent = cert.read() 
        data = jwt.decode(token, certContent)
        try:
            data.validate_exp(datetime.datetime.now().timestamp(),1)
            data.validate_iss()
        except Exception as e:
            return None
        return data