from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

