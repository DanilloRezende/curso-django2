from django.contrib.admin import ModelAdmin, register

from pypro.aperitivos.models import Video


@register(Video)
class VideosAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'youtube_id')
    ordering = ('creation', )
    prepopulated_fields = {'slug':('titulo',)}