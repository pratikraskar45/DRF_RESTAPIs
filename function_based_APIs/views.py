from django.db.migrations import serializer
from django.db.models import Model
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee

from function_based_APIs.serializers import EmployeeSerializer


# Create your views here.

@api_view(['GET','POST'])
def employee_list(request):
    if request.method =='POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT','PATCH','DELETE'])
def employee_details(request,pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        raise Http404("Employee does not exist")

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response (serializer.data , status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


