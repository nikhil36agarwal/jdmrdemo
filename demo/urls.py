from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name='index'),
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('register',views.register, name ='register'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(next_page="index"),name='logout')
    
]
