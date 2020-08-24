from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.getalltasks, name='getalltasks'),
    path('view/', views.viewTask, name='viewtask'),
    path('create/', views.createtask, name='create'),
    path('update/', views.updateTask, name='update'),
    path('login/', views.loginUser, name='login')
]