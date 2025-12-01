from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.evento_list, name='evento_list'),
    path('evento/<int:id>/', views.evento_detail, name='evento_detail'),
    path('evento/novo/', views.evento_create, name='evento_create'),
]
