from django.urls import path 
from . import views

urlpatterns = [
    path('oo',views.fnoo),
    path('home2',views.fnhome2),
    path('fb',views.fnfb)
]