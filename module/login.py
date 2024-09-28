
def login():
    uname=input("enter uname:")
    passw=input("enter passw:")
    f=0
    user=''
    if uname=='admin' and passw=='admin':
        f=1  
    return f,user
