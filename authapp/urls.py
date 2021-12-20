from django.urls import path

from authapp import views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login),
    path('logout', authapp.logout)
]