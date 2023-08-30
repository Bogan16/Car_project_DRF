from rest_framework import generics
from .models import Auto, Owner, AutosPassport
from .serializers import SerializedAuto, SerializedOwner, SerializedAutosPassport

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