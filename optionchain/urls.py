from django.urls import path
from . import views


app_name = "myapp"

urlpatterns = [
    path('optionchain/', views.optionchain, name='chain')
]
