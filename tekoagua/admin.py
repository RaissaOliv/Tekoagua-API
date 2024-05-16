from django.contrib import admin
from tekoagua.models import Company

class Companies(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'cnpj')
    list_display_links = ('company_name', 'cnpj')
    search_fields = ('name',)

admin.site.register(Company, Companies)
# Register your models here.
#tekosenha