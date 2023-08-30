from rest_framework import serializers
from .models import Auto, Owner, AutosPassport

class SerializedOwner(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class SerializedAuto(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'

class SerializedAutosPassport(serializers.ModelSerializer):
    class Meta:
        model = AutosPassport
        fields = '__all__'