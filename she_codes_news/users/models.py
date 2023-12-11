from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_image = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    pass

    def _str_(self):
        return self.username
    

    


