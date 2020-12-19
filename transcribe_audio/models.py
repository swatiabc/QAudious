from django.db import models

# Create your models here.
class AudioModel(models.Model):
    id = models.AutoField(primary_key=True)
    transcript = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    def __str__(self):
        return self.transcript