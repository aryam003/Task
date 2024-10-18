from admin import emp
def view_profile(user):
    print('_'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format('id','name','age','salary','place','date of birth'))
    print('-'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format(user['id'],user['name'],user['age'],user['salary'],user['place'],user['date_of_birth']))
def user_update(user):
    f4=0
    for i in emp:
        if i['id']==user['id']:
            f4=1
            name=input('enter the updatede name: ')
            age=int(input('enter your age: '))
            place=(input('enter your place: '))
            dob=(input('enter your date of birth: '))
            i['name']=name
            i['age']=age
            i['place']=place
            i['date_of_birth']=dob
            print('updated')
    if f4==0:
        print('invalid id.')              