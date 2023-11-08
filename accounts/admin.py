from django.contrib import admin
from .models import Profile,Phones,Address




# Register your models here.


class PhonesAdmin(admin.TabularInline):
    model = Phones



class AddressAdmin(admin.TabularInline):
    model = Address



class ProfileAdmin(admin.ModelAdmin):
    pass



admin.site.register(Profile,ProfileAdmin)
admin.site.register(Phones)
admin.site.register(Address)

