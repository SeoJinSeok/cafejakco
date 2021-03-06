from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from community.models import Entry

class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'user'
        authorization = DjangoAuthorization()
        list_allowed_methods =['get','post','delete']
        filtering = {
            'slug': ALL,
            'user': ALL_WITH_RELATIONS,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
