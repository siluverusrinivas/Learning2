from django.db import models

# Create your models here.
from django.db import models

class Register(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()

    