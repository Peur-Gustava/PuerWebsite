from django.db import models
# from .validators import validate_file_extension

class file_upload(models.Model):
    proof = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.proof
