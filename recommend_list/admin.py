from django.contrib import admin
from .models import RecommendList
from django.utils.html import format_html

class RecommendAdmin(admin.ModelAdmin):
    list_display = ('list_id', 'thumbnail','list_name', 'time', 'part0', 'part1',
    'part2', 'part3', 'part4', 'part5', 'part6', 'part7', 'part8')
    list_display_links = ['list_name']
    search_fields = ['list_name']
    ordering = ('list_id',)  # The negative sign indicate descendent order

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 50px; \
                           height: 50px"/>'.format(obj.list_image.url))

    thumbnail.short_description = 'image'

admin.site.register(RecommendList, RecommendAdmin)