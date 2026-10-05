from django.urls import path

from mixins_generics_based_APIs import views


urlpatterns = [
    path('order/',views.OrderAPIs.as_view()),
    path('order/<int:pk>', views.OrderDetails.as_view()),


]