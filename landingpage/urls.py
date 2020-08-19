from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingpage,name='landingpage'),
    path('signin',views.logout,name='logout'),
]
