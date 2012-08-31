from django.db import models

# Create your models here.

class Ministry(models.Model):
    name=models.CharField(max_length=80)
    volunteers=models.ManyToManyField("Person")

    class Meta:
        verbose_name_plural="Ministries"

    def __unicode__(self):
        return self.name

class Relationship(models.Model):
    person1=models.ForeignKey('Person', related_name='person1')
    person2=models.ForeignKey('Person', related_name="person2")

    relationship_type=(
        (u'Spouse', u'Spouse'),
        (u'Child', u'Child'),
        (u'Parent', u'Parent'),
        (u'Sibling', u'Sibling'),
        (u'In-law', u'In-law'),
        (u'Extended Family', u'Extended Family'),
        (u'Friend', u'Friend'),
        (u'Room Mate', u'Room Mate'),
        (u'Boyfriend', u'Boyfriend'),
        (u'Girlfriend', u'Girlfriend'),
        (u'Fiancee', u'Fiancee'),
        (u'Neighbor', u'Neighbor'),
        (u'Co-Worker', u'Co-Worker'),
        (u'Classmate', u'Classmate'),
        
    )

    relationship_type=models.CharField(max_length=20, choices=relationship_type, blank=True)

    def __unicode__(self):
        return "%s is a %s of %s" % (self.person1, self.relationship_type, self.person2)

class Person(models.Model):

    marital_status_choices= (
        (u'S', u'Single'),
        (u'M', u'Married'),
        (u'D', u'Divorced'),
        (u'W', u'Widowed'),
    )

    partnership_status_choices=(
        (u'Partner', u'Partner'),
        (u'Visitor', u'Visitor'),
        (u'Prospect', u'Prospect'),
        (u'Attender', u'Attender'),

    )

    gender_choices=(
        (u'M', u'Male'),
        (u'F', u'Female')
    )

    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    birth_date=models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=2, choices=gender_choices, blank=True)
    head_of_household=models.BooleanField(default=False)
    is_primary_family_contact=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=25, blank=True)
    address_street=models.CharField(max_length=80, blank=True)
    address_other=models.CharField(max_length=80, blank=True)
    address_city=models.CharField(max_length=80, blank=True)
    address_state=models.CharField(max_length=2, blank=True)
    address_zip=models.CharField(max_length=10, blank=True)
    email_address=models.CharField(max_length=80, blank=True)
    marital_status=models.CharField(max_length=10, choices=marital_status_choices, default=u'Single')
    spouse=models.OneToOneField('self', null=True, blank=True, related_name="Spouse")
    children=models.ManyToManyField('self', null=True, blank=True, related_name='Children')
    partnership_status=models.CharField(max_length=15, choices=partnership_status_choices, null=True, default="Partner")
    partnership_date=models.DateField(blank=True, null=True)
    ministries=models.ManyToManyField('Ministry', related_name='ministry', blank=True)
    other_relationships=models.ManyToManyField(Relationship, blank=True, null=True,related_name="other_relationships")

    def __unicode__(self):
        return "%s:  %s %s" % (self.id, self.first_name, self.last_name)

    class Meta:
        verbose_name_plural="People"



