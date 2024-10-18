from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def fun1(req):
#     return HttpResponse("fun1")

# def fun2(req):
#     return HttpResponse("fun2")

def bonus(reg,a,b):
    # a=enter salary
    # b=enter years of service
    if b>=5:
        bounes=0.05*a+a
        return HttpResponse(f"your net bounes amount: {bounes:.5}")
    else:
        return HttpResponse("you are not eligible ")
    
def num(req,e):
    # e=enter a number
    if e%3==0:
        return HttpResponse(" Divisible")
    else:
        return HttpResponse("Not divisible")  

def bill(req,u):
    # u=number of unit
    if u<=100:
        print("no charge")
    elif u<=200 and u>=100:
        fee=5*u(u-100)
        return HttpResponse(f"electricity bill:{fee}")
    else:
        fee=(u-200)*10+500
        return HttpResponse(f"electricity bill:{fee}")  

def city(req,a):
    # a=city name
    if a=="Delhi":
        return HttpResponse("Red Fort")
    elif a=="Agra":
        return HttpResponse("Taj Mahal")
    elif a=="Jaipur":
        return HttpResponse("Jal Mahal")     
    else:
        return HttpResponse("invalid city name") 

def tax(req,t):
    # a=cost price of a bike
    if t>=100000:
        Tax=t*.15
        return HttpResponse(f"road tax:{Tax}")
    elif t>=50000 and t<=100000:
        Tax=t*.10
        return HttpResponse(f"road tax:{Tax}")
    else:
        Tax=t*.05
        return HttpResponse(f"road tax:{Tax}")

def day(req,a):
    # a= number(1 to 7)
    if a==1:
        return HttpResponse("sunday")    
    elif a==2:
        return HttpResponse("Monday")  
    elif a==3:
        return HttpResponse("Tuesday")      
    elif a==4:
        return HttpResponse("Wednsday")      
    elif a==5:
        return HttpResponse("Thusday")
    elif a==6:
        return HttpResponse("Friday")
    elif a==7:
        return HttpResponse("Saturday") 
    else:
        return HttpResponse("invalid no") 