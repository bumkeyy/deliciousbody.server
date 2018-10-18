from django.contrib import admin
from .models import Version

class VersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'summary')
    ordering = ('-id',)  # The negative sign indicate descendent order


admin.site.register(Version, VersionAdmin)


