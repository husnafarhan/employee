from django.urls import path
from . import views

urlpatterns = [

    path('', views.add_employee),

    path('view/', views.view_employees),

    path('single/<int:id>/', views.single_employee),

    path('update/<int:id>/', views.update_employee),

    path('delete/<int:id>/', views.delete_employee),

]