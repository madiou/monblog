
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/add/', views.add_post, name='add_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/category/', views.add_comment, name='category'),
]
