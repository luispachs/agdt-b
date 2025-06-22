from src.Security.Validators.ValidatorInterface import ValidatorInterface
from src.Security.Validators.ValidatorException import ValidatorException
import re
import sys
class StringValidator(ValidatorInterface):
    data_value:str = None
    def validate(self,data:any):
        if type(data) is not str:
            print(type(data))
            raise ValidatorException(f'Property type must be "STR" got {type(data)}')
        if data is None:
            raise ValidatorException(f'Data cannot be null')
        self.data_value = str.strip(data)
        self.data_value =  re.sub(r'/[0-9\!\-\_\/\\\<\>\!\=]/','',string=self.data_value)


    def data(self):
        return  self.data_value