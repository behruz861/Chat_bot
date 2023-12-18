from django.urls import path, include
from chat import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('chat/', views.chat, name='chat'),
]
