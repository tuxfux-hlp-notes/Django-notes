from tastypie.resources import ModelResource
from .models import Address_Detail

class AddressResource(ModelResource):
    class Meta:
        queryset = Address_Detail.objects.all()  # select * from address_details (ORM)
        resource_name = 'address'
        fields = ['name','email']