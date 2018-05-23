from django.contrib import admin
from .models import Apinform
from .models import Status
from .models import Status1

class ApinformAdmin(admin.ModelAdmin):
    list_display=("ap_oid","ap_name","ap_location","ap_remarks","ap_warnsw","mailed","ap_status")
    list_filter=("ap_warnsw","mailed","ap_status")
    search_fields=("ap_oid","ap_name","ap_warnsw","ap_status")
    ordering=['ap_oid','ap_name','ap_status']

class StatusAdmin(admin.ModelAdmin):
    list_display=("ap_oid","ap_status","update_time")
    search_fields=("ap_oid","update_time")
    ordering=['ap_oid','ap_status']

class Status1Admin(admin.ModelAdmin):
    list_display=("ap_oid","ap_status","update_time")
    search_fields=("ap_oid","update_time")
    ordering=['ap_oid','ap_status']

admin.site.register(Apinform,ApinformAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(Status1,Status1Admin)
    