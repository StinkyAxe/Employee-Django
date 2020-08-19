from django.urls import path
from . import views

urlpatterns = [
    path('',views.extraactivity,name='extraactivity'),
]
