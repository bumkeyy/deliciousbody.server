from django.contrib import admin
from .models import Video
from django.utils.html import format_html


class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'thumbnail','video_name', 'level', 'main_part', 'sub_part')
    list_display_links = ['video_name']
    search_fields = ['video_name']
    list_filter = ('main_part', )
    search_fields = ('video_name', )
    ordering = ('video_id',)  # The negative sign indicate descendent order

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 50px; \
                           height: 50px"/>'.format(obj.video_thumbnail.url))

    thumbnail.short_description = 'image'
admin.site.register(Video, VideoAdmin)