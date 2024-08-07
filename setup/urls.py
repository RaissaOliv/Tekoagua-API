"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tekoagua.views import TrashLocationViewSet, TrashViewSet, UserViewSet, CompanyViewSet, CompanyTrashOwnerViewSet, TrashLogViewSet
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

router = routers.DefaultRouter()
router.register('company', CompanyViewSet, basename='Company')
router.register('trashLocation', TrashLocationViewSet, basename='TrashLocation')
router.register('trash', TrashViewSet, basename='Trash')
router.register('user', UserViewSet, basename='User')
router.register("trashLog", TrashLogViewSet, basename="TrashLog")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('company/<str:company_name>/trashOwner', CompanyTrashOwnerViewSet.as_view())
]

urlpatterns += staticfiles_urlpatterns()
