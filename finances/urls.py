
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path("registerPerson/", views.registerPerson, name='regPerson'),
    path('listPerson/', views.listPerson, name="listPerson"),

    path('registerCard/', views.registerCard, name='regCard'),
    path('listCard/', views.listCard, name='listCard'),

    path('registerExpense/', views.registerExpense, name='regExpense'),
    path('listExpense/', views.listExpense, name='listExpense'),
    path('alterExpense/<int:pk>/', views.alterExpense, name='alterExpense'),
    path('deleteExpense/<int:pk>/', views.deleteExpense, name='deleteExpense'),

    path('registerRevenue/', views.registerRevenue, name='regRevenue'),
    path('listRevenue/', views.listRevenue, name='listRevenue'),
    path('alterRevenue/<int:pk>', views.alterRevenue, name='alterRevenue'),
    path('deleteRevenue/<int:pk>', views.deleteRevenue, name='deleteRevenue'),


    path('registerInvestment/', views.registerInvestment, name='regInvestment'),
    path('registerInvestment/', views.listInvestiment, name='listInvestment')
]
