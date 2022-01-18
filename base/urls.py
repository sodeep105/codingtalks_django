from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('', views.home, name='home'),
    path('rooms/<str:pk>', views.room, name='room'),
    path('create-rooms/', views.createRoom, name='create-room'),
    path('update-rooms/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-rooms/<str:pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
]
