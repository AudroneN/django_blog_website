from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='log_out'),
    path('', views.index, name='index'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('edit/<int:pk>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete/<int:pk>/', views.delete_blog_post, name='delete_blog_post'),
]
