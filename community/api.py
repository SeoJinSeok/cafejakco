from django.contrib.auth.models import Group
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.resources import ModelResource
from membership.models import Group
from community.models import Entry


class EntryResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
        authentication = BasicAuthentication()
        allowed_methods =['get']
