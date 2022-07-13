from django.contrib import admin

from geography import models
from disaster_management import models

class UserHelpRequestAdmin(admin.TabularInline):
    model = models.UserHelpRequest

class EmergencyContactPointAdmin(admin.TabularInline):
    model = models.EmergencyContactPoint

@admin.register(models.Country)
class CountryConfig(admin.ModelAdmin):
    inlines = [UserHelpRequestAdmin,EmergencyContactPointAdmin]
    list_display = ('name','request','emergency','progress','complete')

    def request(self,obj):
        list = models.UserHelpRequest.objects.filter(country=obj).count()
        return list

    def emergency(self,obj):
        list = models.UserHelpRequest.objects.filter(country=obj).filter(is_emergency=True).count()
        return list

    def progress(self,obj):
        list = models.UserHelpRequest.objects.filter(country=obj).filter(is_progress=True).count()
        return list
    
    def complete(self,obj):
        list = models.UserHelpRequest.objects.filter(country=obj).filter(is_complete=True).count()
        return list

@admin.register(models.State)
class StateConfig(admin.ModelAdmin):
    inlines = [UserHelpRequestAdmin,EmergencyContactPointAdmin]
    list_display = ('name','request','emergency','progress','complete')

    def request(self,obj):
        list = models.UserHelpRequest.objects.filter(state=obj).count()
        return list

    def emergency(self,obj):
        list = models.UserHelpRequest.objects.filter(state=obj).filter(is_emergency=True).count()
        return list

    def progress(self,obj):
        list = models.UserHelpRequest.objects.filter(state=obj).filter(is_progress=True).count()
        return list
    
    def complete(self,obj):
        list = models.UserHelpRequest.objects.filter(state=obj).filter(is_complete=True).count()
        return list

@admin.register(models.District)
class DistrictConfig(admin.ModelAdmin):
    inlines = [UserHelpRequestAdmin,EmergencyContactPointAdmin]
    list_display = ('name','request','emergency','progress','complete')

    def request(self,obj):
        list = models.UserHelpRequest.objects.filter(district=obj).count()
        return list

    def emergency(self,obj):
        list = models.UserHelpRequest.objects.filter(district=obj).filter(is_emergency=True).count()
        return list

    def progress(self,obj):
        list = models.UserHelpRequest.objects.filter(district=obj).filter(is_progress=True).count()
        return list
    
    def complete(self,obj):
        list = models.UserHelpRequest.objects.filter(district=obj).filter(is_complete=True).count()
        return list

@admin.register(models.Area)
class AreaConfig(admin.ModelAdmin):
    inlines = [UserHelpRequestAdmin,EmergencyContactPointAdmin]
    list_display = ('name','request','emergency','progress','complete')

    def request(self,obj):
        list = models.UserHelpRequest.objects.filter(area=obj).count()
        return list

    def emergency(self,obj):
        list = models.UserHelpRequest.objects.filter(area=obj).filter(is_emergency=True).count()
        return list

    def progress(self,obj):
        list = models.UserHelpRequest.objects.filter(area=obj).filter(is_progress=True).count()
        return list
    
    def complete(self,obj):
        list = models.UserHelpRequest.objects.filter(area=obj).filter(is_complete=True).count()
        return list