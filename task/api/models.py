from django.db import models

# Create your models here.

class FileUploader(models.Model):
    file = models.FileField(upload_to= 'files/')
    name = models.CharField(max_length=100) #name is filename without extension
    upload_date = models.DateTimeField(auto_now=True, db_index=True)
    file_type = models.CharField(max_length = 50,blank = True, null = True)
    file_path = models.CharField(max_length = 255, blank = True, null =True)