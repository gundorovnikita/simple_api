from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('post/<str:id>',detail),
    path('parse', parse),
]