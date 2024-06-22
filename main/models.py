from django.db import models
from main.SlugGenerator import slug_generator,fileid
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class SharedText(models.Model):
    title=models.TextField(blank=False, null=False)
    note=models.TextField(blank=False, null=False)
    slug=models.SlugField(unique=True,blank=False)
    fileid=models.CharField(max_length=100, primary_key=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expiration_time:
            self.expiration_time = timezone.now() + timedelta(hours=24)
        super().save(*args, **kwargs)
    def is_expired(self):
        return self.expiration_time < timezone.now()