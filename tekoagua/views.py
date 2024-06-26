from rest_framework import viewsets, generics
from tekoagua.models import User, Company, Trash, TrashLocation, CompanyTrashOwner, Person, TrashLog, Profile
from tekoagua.serializers import ProfileSerializer, UserSerializer, CompanySerializer, CompanyTrashOwnerSerializer, TrashLocationSerializer, TrashSerializer, PersonSerializer, TrashLogSerializer 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
            queryset = User.objects.all()
            email = self.request.query_params.get('email', None)
    
            if email is not None:
                queryset = queryset.filter(email=email)
            return queryset

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.filter(is_active=True)
    serializer_class = PersonSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter(is_active=True)
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

class TrashLogViewSet(viewsets.ModelViewSet):
    queryset = TrashLog.objects.all()
    serializer_class = TrashLogSerializer
    
# Create your views here.
