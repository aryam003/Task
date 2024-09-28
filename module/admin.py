emp=[{'id':1,'name':'name','age':0,'salary':0,'place':'place','dob':2/12/23,'passw':2/12/23}]
def add_emp():
    id=int(input("enter id:"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print('id exits.')
            add_emp()
    if f1==0:
        name=input("enter name:")
        age=int(input("enter age:"))
        salary=int(input("enter salary:"))
        place=input("enter place:")
        dob=input("enter dob:")
        u_passw=input("enter password:")
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob,'u_passw':u_passw})
        print('Employee added successfully')
        print(emp)
def edit_emp():
    id=int(input("enter id:"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            name=input("enter name:")
            age=int(input("enter age:"))
            salary=int(input("enter salary:"))
            place=input("enter place:")
            dob=input("enter dob:")
            u_passw=input("enter password:")
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['dob']=dob
            i['u_passw']=u_passw
    if f1==0:
        print("invalid id.")
def delete():
    id=int(input("enter id:"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            emp.remove(i)
    if f1==0:
        print("invalid id.")
def display():
        print('{:<5}{:<10}{:<5}{:<10}{:<10}{:<10}'.format('id','name','age','salary','place','dob'))
        print('_'*50)
        for i in emp:
            print('{:<5}{:<10}{:<5}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['dob']))