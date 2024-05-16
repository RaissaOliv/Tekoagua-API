from rest_framework import viewsets, generics
from tekoagua.models import User, Company, Trash, TrashLocation, CompanyTrashOwner, Person
from tekoagua.serializers import UserSerializer, CompanySerializer, CompanyTrashOwnerSerializer, TrashLocationSerializer, TrashSerializer, PersonSerializer 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.filter(is_active=True)
    serializer_class = PersonSerializer
    
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
