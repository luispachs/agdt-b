import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
class Hash:
    priv:str =None
    salt:bytes =None
    key:bytes =None
    def __init__(self):
        self.priv = os.getenv('APP_KEY')
        self.salt =os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=1_200_000,
        )
        temp = bytes(self.priv,encoding='utf-8')
        self.key = base64.urlsafe_b64encode(kdf.derive(temp))




    def encryt(self,data:str):
        f = Fernet(self.key)
        encrytedData = f.encrypt(bytes(data,encoding='utf-8'))
        return encrytedData.decode(encoding='utf-8')

    def decrypt(self,data:str):
        f=Fernet(self.key)
        return f.decrypt(data)

    def validate(self,strEncrypt:str,strDecryt):
        f=Fernet(self.key)
        decrytedData = f.decrypt(strEncrypt)
        if decrytedData == strDecryt:
            return True
        return False