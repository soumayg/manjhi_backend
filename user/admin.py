from django.contrib import admin
from user import models


class UserAddressDetailsAdmin(admin.TabularInline):
    model = models.UserAddressDetails

class UserFamilyDetailsAdmin(admin.TabularInline):
    model = models.UserFamilyDetails


@admin.register(models.User)
class UserConfig(admin.ModelAdmin):
    inlines = [UserAddressDetailsAdmin,UserFamilyDetailsAdmin]
    list_display = ('mobile_number','name')
