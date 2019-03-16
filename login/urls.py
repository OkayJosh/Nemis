from django.urls import path, include
from django.contrib.auth import views
from .views import MyHomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login'),
]
