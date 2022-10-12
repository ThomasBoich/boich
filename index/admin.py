from django.contrib import admin

# Register your models here.
from index.models import Rabota, Customer, ProjectType

admin.site.register(Rabota)
admin.site.register(Customer)
admin.site.register(ProjectType)