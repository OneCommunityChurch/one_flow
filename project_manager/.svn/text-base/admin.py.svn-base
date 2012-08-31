__author__ = 'jade'

from django.contrib import admin
from one_flow.project_manager.models import *

class personAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ['id', 'first_name', 'last_name',]
    filter_horizontal = ['children','other_relationships',]

#class TPCFAdmin(admin.ModelAdmin):
#    pass


#admin.site.register(person, personAdmin)
