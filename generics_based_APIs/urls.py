from django.urls import path

from generics_based_APIs import views

urlpatterns = [
    path('student/',views.StudentAPIs.as_view()),

    path('student/<int:pk>/', views.StudentDetails.as_view())
]