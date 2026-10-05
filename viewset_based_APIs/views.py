from functools import partial

from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BankAccount

from viewset_based_APIs.serializers import BankAccountSerializer


# Create your views here.
class BankAccountViewSet(viewsets.ViewSet):

    def create(self,request):
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response( serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        queryset = BankAccount.objects.all()
        serializer =BankAccountSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def retrieve(self,request,pk):
        bankaccount =get_object_or_404(BankAccount,pk=pk)
        serializer = BankAccountSerializer(bankaccount)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self,request,pk):
        bankaccount =get_object_or_404(BankAccount,pk=pk)
        serializer = BankAccountSerializer(bankaccount, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        bankaccount =get_object_or_404(BankAccount, pk=pk)
        serializer = BankAccountSerializer(bankaccount, data= request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def destroy(self,request,pk):
        bankaccount =get_object_or_404(BankAccount,pk=pk)
        bankaccount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

