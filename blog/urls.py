<<<<<<< HEAD
from django.urls import path 
=======
from django.urls import path
>>>>>>> 9502574 (retake)
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
<<<<<<< HEAD
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
=======
     path('post/<int:pk>/', views.post_detail, name='post_detail'),
     path('post/new/', views.post_new, name='post_new'),
>>>>>>> 9502574 (retake)
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]
