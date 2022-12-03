from django.db import models

class Profile(models.Model):
  name = models.CharField(max_lenght=50, blank=True)
  contact = models.DecimalField(max_digit = 10, blank =True, null= True)

# Create your models here.
