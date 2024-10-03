
from login import *
from admin import *
from user import *

while True:
    print('''
1.login
2.exit
''')
    ch=int(input("enter ur choice:"))
    if ch==1:
        f,user=login()
        if f==1:
            while True:
                print('''
1.add emp
2.update emp
3.delete
4.display
5.exit.
''')
                sub_ch=int(input("enter ur choice:"))
                if sub_ch==1:
                    add_emp()
                elif sub_ch==2:
                    edit_emp()
                elif sub_ch==3:
                    delete()
                elif sub_ch==4:
                    display()
                elif sub_ch==5:
                    break
                else:
                    print("Invalid choice.")
        elif f==0:
            print("invalied uname or passw")
        elif f==2: 
            while True:
                if user['date_of_birth']==user['passw']:
                    passw=input('enter a new password')
                    user['password']=passw
                else:
                    print('''
                        1.view profile
                        2.edit profile
                        3.logout
    ''')
                    sub_ch=int(input('enter your choice: '))
                    if sub_ch==1:
                        view_profile(user)
                    elif sub_ch==2:
                        user_update(user)
                    elif sub_ch==3:
                        break 
    elif ch==2:
        break