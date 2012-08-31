__author__ = 'jade'

from django.contrib import admin
from one_flow.job_board.models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', )
    search_fields = ['id', 'name', 'city', ]

class JobAdmin(admin.ModelAdmin):
    list_display = ("company", "job_title",)
    search_fields = ['company', 'job_title', ]
    vertical_filter=['company',]

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['slug','content',]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Job_Post, JobAdmin)
admin.site.register(News_Post, NewsAdmin)
