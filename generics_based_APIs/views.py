
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
# class StudentAPIs(generics.ListAPIView,generics.CreateAPIView):
class StudentAPIs(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentDetails(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'

