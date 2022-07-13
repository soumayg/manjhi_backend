from django.contrib import admin

from disaster_management import models


admin.site.register(models.Disaster)
admin.site.register(models.EssentialService)

@admin.register(models.UserHelpRequest)
class UserHelpRequestAdmin(admin.ModelAdmin):
    search_fields = ('area__name','district__name','state__name','country__name')
    list_filter = ['is_emergency','is_progress','is_complete']
    list_display = ('user','disaster','request','is_emergency','is_progress','is_complete')