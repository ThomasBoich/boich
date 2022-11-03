from django.contrib import admin

# Register your models here.
from index.models import Rabota, Customer, ProjectType, Profile

class RabotaAdmin(admin.ModelAdmin):
    save_as = True
    # prepupulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'customer', 'slug')
    list_editable = ()
    list_display_links = ('id', 'title')
    search_fields = ('title', 'slug', 'customer')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Rabota, RabotaAdmin)
admin.site.register(Customer)
admin.site.register(ProjectType)
admin.site.register(Profile)
# admin.site.register(Vizit)