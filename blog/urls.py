from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),  # New URL for registration

    path('logout/', views.log_out, name='log_out'),
    path('', views.index, name='index'),
]
