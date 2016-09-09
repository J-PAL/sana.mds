''' sana.tasks.admin

:author: Sana Development Team
:version: 2.0
:copyright: Sana 2012, released under BSD New License(http://sana.mit.edu/license)
'''
from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ['version', 'version_code']
    list_filter = ['version', 'version_code']
admin.site.register(Client)

class CrashReportAdmin(admin.ModelAdmin):
    list_display = ['created', 'device']
    list_filter = ['created', 'device']
admin.site.register(CrashReport, CrashReportAdmin)
