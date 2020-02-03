from django.contrib import admin

# Register your models here.
from . import models

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name_phuong','url_post','number_post','action')
    list_filter = ['id','name_phuong','url_post','number_post','action']
    search_fields = ['id','name_phuong','url_post','number_post','action'] 
 
admin.site.register(models.Customer, CustomerAdmin) 
