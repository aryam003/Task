from admin import emp
def login():
    uname=input("enter uname:")
    passw=input("enter passw:")
    f=0
    user=''
    if uname=='admin' and passw=='admin':
        f=1  
    for i in emp:
        if i['id']==uname and i['passw']==passw:
            f=2
            user=i     
    return f,user
