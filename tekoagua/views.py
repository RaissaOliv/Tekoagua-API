from rest_framework import viewsets, generics
from tekoagua.models import User, Company, Trash, TrashLocation, CompanyTrashOwner
from tekoagua.serializers import UserSerializer, CompanySerializer, CompanyTrashOwnerSerializer, TrashLocationSerializer, TrashSerializer 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class TrashViewSet(viewsets.ModelViewSet):
    queryset = Trash.objects.all()
    serializer_class = TrashSerializer

class TrashLocationViewSet(viewsets.ModelViewSet):
    queryset = TrashLocation.objects.all()
    serializer_class = TrashLocationSerializer

class CompanyTrashOwnerViewSet(generics.CreateAPIView):
    def get_queryset(self):
        queryset = CompanyTrashOwner.objects.filter(company=self.kwargs['company'])
        return queryset
    serializer_class = CompanyTrashOwnerSerializer
    
# Create your views here.
