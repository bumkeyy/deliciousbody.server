from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'video_name', 'level', 'main_part', 'sub_part')
    ordering = ('video_id',)  # The negative sign indicate descendent order


admin.site.register(Video, VideoAdmin)