from django.db import models

# Create your models here.
class Document(models.Model):
    user = models.CharField(max_length=100)
    time = models.IntegerField(default=0)
    docfile = models.FileField(upload_to='files')

    def __str__(self):
        return self.user
