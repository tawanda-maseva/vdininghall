from django.contrib import admin

# Register your models here.
from vdh_app.models import Customer, CustomerInfo
admin.site.register(Customer)
admin.site.register(CustomerInfo)