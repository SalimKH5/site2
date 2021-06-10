from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Files(models.Model):
    adminupload1=models.FileField(upload_to='media')
    adminupload2=models.FileField(upload_to='media')
    relation=models.IntegerField(null=True)
    
