__author__ = 'jade'

from django.contrib import admin
from one_flow.one_info.models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ['id', 'first_name', 'last_name',]
    filter_horizontal=['ministries', 'children', 'other_relationships',]

class MinistryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal=["volunteers",]

admin.site.register(Person, PersonAdmin)
admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Relationship)

