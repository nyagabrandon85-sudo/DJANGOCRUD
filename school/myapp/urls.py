from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_student, name='add'),
]