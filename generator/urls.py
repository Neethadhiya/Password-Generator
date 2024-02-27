from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('password/', views.password, name = 'password'),
    path('show_passwords/',views.show_passwords, name="show_passwords"),
    path('delete_password/<int:id>',views.delete_password, name="delete_password"),
    path('search_password/',views.search_password, name="search_password"),

]