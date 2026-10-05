from django.urls import path
from . import  views

urlpatterns = [
    path('emp/',views.employee_list),
    path('emp/<int:pk>/', views.employee_details)

]