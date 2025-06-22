class AgendateException:
    def __init__(self):
        pass

    @staticmethod
    def getError(code:int):
        if code == 1000:
            return "Credentials are invalids"
        elif code == 1001:
            return "Invalid properties got, verificate data"
        elif code == 5000:
            return "Unexpected Exception, please report this error to administrator"
        else:
            return "Undefined Error"