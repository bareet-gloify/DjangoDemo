from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import employees
from . serializers import employeeSerializer
# Create your views here.

class employeeList(APIView):

    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeeSerializer(employees1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
