from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('bank-account',views.BankAccountViewSet,basename='bank-account')

urlpatterns = [
    path('',include(router.urls))

]