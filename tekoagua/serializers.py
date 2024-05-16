from rest_framework import serializers
from tekoagua.models import User, Person, Company, Trash, TrashLocation, CompanyTrashOwner

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class TrashSerializer(serializers.ModelSerializer):
     class Meta:
        model = Trash
        fields = "__all__"

class TrashLocationSerializer(serializers.Serializer):
     class Meta:
        model = TrashLocation
        fields = "__all__"

class CompanyTrashOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTrashOwner
        fields = "__all__"