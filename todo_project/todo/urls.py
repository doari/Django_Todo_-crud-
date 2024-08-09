from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/<int:id>/', views.detail, name='detail'),
    path('add/', views.add_todo, name='add'),
    path('edit/<int:id>/', views.edit_todo, name='edit'),
    path('delete/<int:id>/', views.delete_todo, name='delete'),
]
