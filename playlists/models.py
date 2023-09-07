from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from djangoflix.db.models import PublishStateOptions
from djangoflix.db.receivers import slugify_pre_save, publish_state_pre_save

class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            publish_timestamp__lte=now,
            state=PublishStateOptions.PUBLISH
            )

class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


# Create your models here.

 
class Playlist(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    state = models.CharField(max_length=2,choices=PublishStateOptions.choices, default= PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,null=True)


    objects = PlaylistManager()


    @property
    def is_published(self):
        return self.active

    # def save(self,*args, **kwargs):
        # if self.state == VideoStateOptions.PUBLISH and self.publish_timestamp is None:
        #     self.publish_timestamp = timezone.now()
        # elif self.state == VideoStateOptions.DRAFT:
        #     self.publish_timestamp = None
        
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        # super().save(*args, **kwargs)

        


pre_save.connect(publish_state_pre_save, sender=Playlist)
pre_save.connect(slugify_pre_save, sender=Playlist)

