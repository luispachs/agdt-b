from abc import abstractmethod
class ValidatorInterface:
    @abstractmethod
    def validate(self,data:any):
        pass

    @abstractmethod
    def data(self):
        pass