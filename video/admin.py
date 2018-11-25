from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id','video_thumbnail', 'video_name', 'level', 'main_part', 'sub_part')
    list_display_links = ['video_name']
    search_fields = ['video_name']
    list_filter = ('main_part', )
    search_fields = ('video_name', )
    ordering = ('video_id',)  # The negative sign indicate descendent order


admin.site.register(Video, VideoAdmin)