from django.contrib import admin
from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'is_man', 'activity_level', 'interested_part',
    'weekdays_start', 'weekdays_end', 'weekend_start', 'weekend_end',
    'is_push_weekdays', 'is_push_weekend')
    list_display_links = ['name']
    search_fields = ['name']
    ordering = ('name',)  # The negative sign indicate descendent order

admin.site.register(UserInfo, UserInfoAdmin)