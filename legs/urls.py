from django.urls import path
from . import views

# app_name = 'legs'

urlpatterns = [
    # path('hello/', views.home_view, name='hello'),
    path('', views.home_view, name='hello'),
    path('create/', views.create_view, name='create'),
    path('update_view/<int:pk>', views.update_view, name='update'),
    path('read/', views.read_view, name='read'),
    path('delete_view/<int:pk>', views.delete_view, name='delete'),
]