from django.db import models
from django.contrib.auth.models import User
import os 
from django.conf import settings
class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)         
    file = models.FileField(upload_to='téléchargement/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


   

