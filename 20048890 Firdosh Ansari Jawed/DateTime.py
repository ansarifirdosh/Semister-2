import datetime as dtime #library from python api


dtime = dtime.datetime.now()



def getCurrentDate() -> str: #-> str is just an annotation telling what the method should return, doesn't affect anything
    '''gets current date in string'''
    return str(dtime.date())

def getCurrentTime() -> str:
    '''gets current time in string'''
    return str(dtime.time())
