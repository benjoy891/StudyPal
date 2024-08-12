from django.db import models

# Create your models here.
class PDFDocument(models.Model):
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.file.name