from django.urls import path
from . import views

urlpatterns=[
    path('',views.create , name='create'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('createjs/', views.create_with_ajax ,name='ajax_create'),
    
]