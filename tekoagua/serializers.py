from rest_framework import serializers
from tekoagua.models import User, Person, Company, Trash, TrashLocation, CompanyTrashOwner, TrashLog
from validate_docbr import CNPJ

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
    def validate_cnpj(self, cnpj):
        is_cnpj = CNPJ()
        if not is_cnpj.validate(cnpj):
            raise serializers.ValidationError({"cnpj":"insira um cnpj válido!"})
        return cnpj


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

class TrashLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashLog
        fields = "__all__"
