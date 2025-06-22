class Messages:
    def __init__(self):
        pass


    @staticmethod
    def getMessage( code:int):
        if code == 1000:
            return 'Authorize'
        elif code == 1001:
            return 'Creation successfull'
        else:
            return 'Undefined Message'
