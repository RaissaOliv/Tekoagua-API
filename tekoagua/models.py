from django.db import models
import uuid
# Create your models here.
class Profile(models.Model):
    ROLES = (
        ('A', 'admin'),
        ('F', 'employee')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=1, choices=ROLES)

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    is_active = models.BooleanField(default=True)

class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField()
    email = models.EmailField(unique=True)
    name = models.CharField()
    company = models.ForeignKey(Company, blank=True, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

class Person(models.Model):
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class TrashLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.CharField()
    longitude = models.CharField()
    city = models.CharField()
    state = models.CharField()
    island = models.CharField()
    country = models.CharField()
    
    
class Trash(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4, editable=False)
    trash_location = models.ForeignKey(TrashLocation, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

class CompanyTrashOwner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)