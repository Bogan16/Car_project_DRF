from rest_framework import generics
from .models import Auto, Owner, AutosPassport
from .serializers import SerializedAuto, SerializedOwner, SerializedAutosPassport
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    
    def get(self, request):
        data = {
            "message": "Welcome to the auto project!",
        }
        return Response(data)

class OwnerListCreateView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = SerializedOwner

class OwnerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = SerializedOwner

class AutoListCreateView(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = SerializedAuto

class AutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = SerializedAuto

class AutosPassportListCreateView(generics.ListCreateAPIView):
    queryset = AutosPassport.objects.all()
    serializer_class = SerializedAutosPassport

class AutosPassportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AutosPassport.objects.all()
    serializer_class = SerializedAutosPassport