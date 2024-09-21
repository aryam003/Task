import datetime
print(datetime.datetime.now().strftime("%x"))
user=[]
product=[]
order=[]

while True:
    print('''
1.Add products
2.View products
3.Update products
4.Remove products
5.Register uses
6.costomer
7.Search
8.Exit
''')
    choice=int(input("Enter ur choice:"))
    if choice==1:
        id=int(input("Enter product id:"))
        name=input("Enter product name:")
        price=int(input("Enter product price :"))
        B_name=input("Enter Brand Name :")
        N_weight=int(input("Enter Net Weight :"))
        B_No=int(input("Enter Batch Number :"))
        contact=int(input("Enter contact information :"))
        date=datetime.datetime.now().strftime("%x")
        product.append({'id':id,'name':name,'price':price,'B_name':B_name,'N_weight':N_weight,'B_No':B_No,'contact':contact,'date':date})

    elif choice==2:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id','name','price','B_name','N_weight','B_No','contact','date'))
        print('_'*90)
        for i in product:
                    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['price'],i['B_name'],i['N_weight'],i['B_No'],i['contact'],i['date']))

    elif choice==3:
        id=int(input("enter id:"))
        f=0
        for i in product:
            if i['id']==id:
                f=1
                while True:
                    print('''
1.Product name
2.Price
3.Brand name                                                                  
4.Net weight
5.batch No                         
6.Contact
7.Date
8.Exit                                  
''')
                    sub_ch=int(input("Enter Your Choice For Update:"))
                    if sub_ch==1:
                        new_name=input("Enter new name:")
                        i['name']==new_name

                    elif sub_ch == 2:
                        new_price = input("Enter new price: ")
                        i['price'] = new_price
                       

                    elif sub_ch == 3:
                        new_brand = input("Enter new brand name: ")
                        i['B_name'] = new_brand

                    elif sub_ch == 4:
                        new_net_weight = input("Enter new net weight: ")
                        i['N_weight'] = new_net_weight

                    elif sub_ch == 5:
                        new_batch_no = input("Enter new batch No: ")
                        i['B_no'] = new_batch_no
                      

                    elif sub_ch == 6:
                        new_contact = input("Enter new contact: ")
                        i['contact'] = new_contact
                        

                    elif sub_ch == 7:
                        new_date = input("Enter new date: ")
                        i['date'] = new_date
                        

                    elif sub_ch == 8:
                        print("Exiting.")
                        break

                    else:
                        print("Invalid choice")

    elif choice==4:
        id=int(input("enter id:"))
        f=0
        for i in product:
            if i['id']==id:
                product.remove(i)
                f=1
        if f==0:
            print('Invalid data.')

    elif choice==5:
        while True:
            print('''
1.register user
2.view user
3.exit
''')
            sub_ch=int(input("Enter ur choice:"))
            if sub_ch==1:
                id=int(input("Enter id:"))
                name=input("Enter ur name:")
                address=input("Enter ur address:")
                email=input("Enter ur email:")
                phone=int(input("enter ur phonr number:"))
                date=datetime.datetime.now().strftime("%x")
                user.append({'id':id,'name':name,'address':address,'email':email,"phone":phone,'date':date})

            elif sub_ch==2:
                print('{:<10}{:<10}{:<30}{:<10}{:<10}{:<10}'.format('id','name','address','email','phone','data')) 
                print('_'*80)
                for i in user:
                        print('{:<10}{:<10}{:<30}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['address'],i['email'],i['phone'],i['date'])) 

            elif sub_ch==3:
                print("Exiting.")
                break  
            else:
                print("invalid data") 

    elif choice==6:
        while True:
            print('''
1.ordered
2.view
3.exit
''')
            sub_ch = int(input("Enter your choice: "))
            if sub_ch == 1:
                product_id = int(input("Enter product ID: "))
                for i in product:
                    if i['id'] == product_id:
                        order.append(i)
                        print(f"Added {i['name']} to order.")
                        break
                else:
                    print("Product not found.")

            elif sub_ch == 2:
                print("Ordered products:")
                print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id', 'name', 'price', 'B_name', 'N_weight'))
                print('_' * 60)
                for i in order:
                    print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'], i['name'], i['price'], i['B_name'], i['N_weight']))
            elif sub_ch == 3:
                print("Exiting.")
                break

            else:
                print("Invalid choice.")

    elif choice == 7:
        id=int(input("Enter product ID to search: "))
        f=0
        for i in product:
            if i['id']==id:
                print(i)
                f=1
        if f==0:
            print("Product id not found.")

    elif choice == 8:
        print("Exiting.")
        break

    else:
        print("Invalid choice.")

            


            
                                    


