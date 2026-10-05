from django.db.models import Model
from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Order
from .serializers import OrderSerializer


# Create your views here.
class OrderAPIs(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def get(self,request):
        return  self.list(request)

    def post(self,request):
        return self.create(request)

class OrderDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self, request ,pk):
        return  self.update(request,pk)

    def patch(self, request , pk):
        return self.partial_update(request, pk)

    def delete(self, request , pk):
        return self.destroy(request, pk)

