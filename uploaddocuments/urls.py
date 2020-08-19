from django.urls import path
from . import views

urlpatterns = [
    path('',views.uploaddocuments,name='uploaddocuments'),
]