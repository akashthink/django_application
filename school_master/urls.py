from django.urls import path
from school_master import views

urlpatterns = [
   
    path('home', views.index),
    path('reg',views.login),

]