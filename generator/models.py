from django.db import models
from django.utils import timezone

class PasswordGenerator(models.Model):
    site = models.CharField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    passwords = models.CharField(max_length=300)

    def __str__(self):
        return self.site
# Create your models here.
