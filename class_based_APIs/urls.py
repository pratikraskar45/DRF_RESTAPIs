from django.urls import  path

from class_based_APIs import views

urlpatterns = [
    path('product/', views.ProductAPIView.as_view()),
    path('product/<int:pk>/', views.ProductDetails.as_view()),

]