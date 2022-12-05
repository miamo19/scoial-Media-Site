from django.db import models

class Profile(models.Model):
  user = models.ForeighKeg(User, on_delete = models.CASCADE)
  name = models.CharField(max_lenght=50, blank=True)
  contact = models.DecimalField(max_digit = 10, blank =True, null= True)
  

# Create your models here.
