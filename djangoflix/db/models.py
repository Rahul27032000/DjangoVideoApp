from django.db import models

class VideoStateOptions(models.TextChoices):
        # constant = DB_VALUE, USER_DISPLAY_VALUE
        PUBLISH = 'PU', "Published"
        DRAFT = 'DR', "Draft"
        UNLISTED = 'UN', "Unlisted"
        PRIVATE = 'PR', "Private"

