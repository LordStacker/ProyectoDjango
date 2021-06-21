from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('intro/', views.index, name="Intro"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
]