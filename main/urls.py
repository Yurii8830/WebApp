
from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('register/', register, name='register'),

    path('',views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts')

]
