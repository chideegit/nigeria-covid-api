from django.urls import path 
from .views import NigeriaStateList

urlpatterns = [
    path('', NigeriaStateList, name='nigeria-list')
]