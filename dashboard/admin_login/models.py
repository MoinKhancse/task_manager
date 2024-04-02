from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class data_add(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    catagory = models.CharField(max_length=20)
    image =models.ImageField(upload_to='image/',blank=True,null=True)
