def TokenExtract(token:str)->str:
    if token is None:
        return ''
    formatedToken = str(token).replace('Bearer ','')

    return formatedToken
