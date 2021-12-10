from django.urls import path
from . import views

app_name = 'proj_r'

urlpatterns = [
    path('', views.recharge, name="Recharge"),
]