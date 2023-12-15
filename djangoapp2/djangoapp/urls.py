from django.urls import path
import views

urlpatterns = [
    path('', views.get_users),
    path('read/<str:pk>', views.get_user),
    path('update/<str:pk>', views.update_user),
    path('delete/<str:pk>', views.delete_user),
    path('create/', views.create_user),
]
