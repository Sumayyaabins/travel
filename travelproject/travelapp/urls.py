
from django.urls import path
from . import views
urlpatterns = [
    path('',views.demo,name='demo'),

    #path('add/',views.addition,name='addition'),
    #path('contact/',views.contact,name='contact'),
    #path('home/',views.home,name='home')

]