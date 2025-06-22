from src.Security.Validators import ValidatorInterface
from src.Security.Validators.ValidatorException import ValidatorException
import sys
class IntValidator(ValidatorInterface):
    __min=None
    __max=None
    __data=None
    def __init__(self,min:int=None,max:int=None):
        super().__init__()
        self.__min = min
        self.max = max

    def validate(self,data:any):
        if type(data) is not int:
            raise ValidatorException(f'Property type must be "INT" got {type(data)}').with_traceback(sys.exception().__traceback__)
        if data is None:
            raise ValidatorException(f'Data cannot be null')
        if self.__min is None and data < self.__min:
            raise ValidatorException(f'{self.__data}  is smaller than {self.__min}').with_traceback(sys.exception().__traceback__)
        if self.__max is None and data > self.__max:
            raise ValidatorException(f'{self.__data}  is granter than {self.__min}').with_traceback(sys.exception().__traceback__)
        self.__data = data

    def data(self):
        return self.__data