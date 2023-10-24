from django.urls import path
from .views import HomePage,StringOperations

urlpatterns = [
    path('',HomePage,name='HomePage'),
    path('stringoperation/',StringOperations,name="StringOperations"),
]