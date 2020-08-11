from django.contrib import admin
from .models import User,GlobalConacts
from import_export.admin import ImportExportModelAdmin

admin.site.register(User)
@admin.register(GlobalConacts)
class GlobalConactsAdmin(ImportExportModelAdmin):
    pass
