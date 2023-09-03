from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class VideoStateOptions(models.TextChoices):
        # constant = DB_VALUE, USER_DISPLAY_VALUE
        PUBLISH = 'PU', "Published"
        DRAFT = 'DR', "Draft"
        UNLISTED = 'UN', "Unlisted"
        PRIVATE = 'PR', "Private"

# Create your models here.
class Video(models.Model):
    

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=220,unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    state = models.CharField(max_length=2,choices=VideoStateOptions.choices, default= VideoStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,null=True)


    @property
    def is_published(self):
        return self.active

    def save(self,*args, **kwargs):
        if self.state == VideoStateOptions.PUBLISH and self.publish_timestamp is None:
            self.publish_timestamp = timezone.now()
        elif self.state == VideoStateOptions.DRAFT:
            self.publish_timestamp = None
        
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        

class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'





class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'
