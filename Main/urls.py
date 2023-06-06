from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.show, name="index"),
    path('showEvents/<str:season>/', views.EventsView.as_view(), name="showEv"),
    path('showEvent/<str:title>/', views.EventView.as_view(), name="showEvent"),
    path('edit/<str:title>/', views.edit, name="editevent"),
    path('showEvents/', views.show, name="ShowEv"),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('Register/', views.RegisterUser.as_view(), name='register'),
    path('create/', views.addEvent, name='createEvent'),
]