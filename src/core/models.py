from django.db import models

class Profile(models.Model):
  name = models.CharField(max_lenght=50, blank=True)

# Create your models here.
