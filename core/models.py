from django.db import models
from .validators import validate_file_extension

class file_upload(models.Model):
    proof = models.FileField(upload_to="documents/",validators =[validate_file_extension])
