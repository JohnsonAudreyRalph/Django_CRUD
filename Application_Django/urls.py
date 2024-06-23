from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='Show'),
    path('Delete/<int:id>/', Delete, name='Delete'),
    path('Update/<str:id>', Update, name='Update')
]