from src.Security.Validators import ValidatorInterface
from src.Security.Validators.ValidatorException import ValidatorException
import re
import sys
class StringValidator(ValidatorInterface):
    data_value:str = None
    def validate(self,data:any):
        if type(data) != str.__class__:
            raise ValidatorException(f'Property type must be "STR" got {type(data)}').with_traceback(sys.exception().__traceback__)
        if data is None:
            raise ValidatorException(f'Data cannot be null')
        self.data_value = str.strip(data)
        self.data_value =  re.sub(r'/[0-9\!\-\_\/\\\<\>\!\=]/','',string=self.data_value)


    def data(self):
        return  self.data_value