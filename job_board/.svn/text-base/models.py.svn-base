from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.exceptions import ValidationError
import logging
from richtext.fields import AdminRichTextField

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=40)
    logo=models.FileField(upload_to="static/company_logos/" ,null=True, blank=True)
    url=models.URLField(null=True, blank=True)
    contact_name=models.CharField(max_length=80, null=True, blank=True)
    contact_phone=models.CharField(max_length=20, null=True, blank=True)
    contact_email=models.EmailField(null=True, blank=True)
    address=models.CharField(max_length=80, null=True, blank=True)
    city=models.CharField(max_length=80, null=True, blank=True)
    state=models.CharField(max_length=2, null=True, blank=True)
    zip_code=models.CharField(max_length=12, null=True, blank=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural="Companies"
    

    def __unicode__(self):
        return self.name

class Job_Post(models.Model):
    job_title=models.CharField(max_length=80, null=True, blank=True)
    company=models.ForeignKey(Company)
    job_zip_code=models.CharField(max_length=15, null=True, blank=True)
    apply_email_address=models.CharField(max_length=40, null=True, blank=True)
    job_description=AdminRichTextField()
    date_created=models.DateField(default=datetime.today())
    date_start_post=models.DateField(default=datetime.today())
    date_end_post=models.DateField(null=True, blank=True)
    is_active=models.BooleanField(default=True)

    def __unicode__(self):
        return '%s:  %s' % (self.company.name, self.job_title)

    class Meta:
        verbose_name="Job Post"
        verbose_name_plural="Job Posts"

class News_Post(models.Model):
    title=models.CharField(max_length=50)
    content=AdminRichTextField(blank=True, null=True)
    date_start_post=models.DateField(default=datetime.today())
    date_end_post=models.DateField(null=True, blank=True)
    is_active=models.BooleanField(default=True) 
     
        






