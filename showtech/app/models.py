# Create your models here.
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

