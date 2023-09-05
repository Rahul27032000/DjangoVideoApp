from django.utils.text import slugify
from .models import VideoStateOptions
from django.utils import timezone



def publish_state_pre_save(sender,instance,*args,**kwargs):
    is_publish = instance.state == VideoStateOptions.PUBLISH 
    is_draft = instance.state == VideoStateOptions.DRAFT 
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif is_draft:
        instance.publish_timestamp = None



def slugify_pre_save(sender,instance,*args,**kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)