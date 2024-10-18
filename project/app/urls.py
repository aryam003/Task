from django.urls import path
from . import views

urlpatterns = [
    # path('a',views.fun1),
    # path('b',views.fun2),
    path('bonus/<int:a>/<int:b>',views.bonus),
    path('num/<int:e>',views.num),
    path('bill/<int:u>',views.bill),
    path('city/<str:a>',views.city),
    path('tax/<int:t>',views.tax),
    path('day/<int:a>',views.day),   
]