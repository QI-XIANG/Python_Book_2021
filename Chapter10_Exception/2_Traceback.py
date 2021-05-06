def spam():
    bacon()

def bacon():
    raise Exception('This the error message') # after run this program, you can see the 'call stack' of the exception

spam()