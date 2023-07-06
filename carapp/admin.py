from django.contrib import admin
from django.db import models
from .models import CarType, Vehicle, Buyer, OrderVehicle, Description, LabGroupMember
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['email','username','shipping_address','area']
    search_fields = ['email','username']
    readonly_fields =['shipping_address','area']

class OrderVehicleAdmin(admin.ModelAdmin):
    list_display = ['buyer_username','vehicle','order_status']
    search_fields = ['buyer_username','vehicle','order_status']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['car_name','car_type','car_price','instock']

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['title','project_description','added_time']

class LabGroupMemberAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','semester', 'personal_page']


# Register your models here.
admin.site.register(CarType)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Buyer,BuyerAdmin)
admin.site.register(OrderVehicle,OrderVehicleAdmin)
admin.site.register(Description,DescriptionAdmin)
admin.site.register(LabGroupMember,LabGroupMemberAdmin)

