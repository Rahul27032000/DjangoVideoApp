from django.contrib import admin
from .models import Video,VideoPublishedProxy,VideoAllProxy

# Register your models here.
class VideoAllAdmin(admin.ModelAdmin):
    list_display=['title','state','video_id','is_published']
    search_fields =['title','video_id']
    list_filter =['title','video_id','state']

    class Meta:
        model = VideoAllProxy


admin.site.register(VideoAllProxy,VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display=['title','video_id']
    search_fields =['title','video_id']
    list_filter =['title','video_id']

    class Meta:
        model = VideoPublishedProxy


    def get_queryset(self,request):
        return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoPublishedProxy,VideoPublishedProxyAdmin)

