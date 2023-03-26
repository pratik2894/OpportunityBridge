from django.db import models

# Create your models here.
class Banner(models.Model):
    title=models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    bannerimage1 = models.ImageField(upload_to="media")
    bannerimage2 = models.ImageField(upload_to="media")
    bannerimage3 = models.ImageField(upload_to="media")
    bannerimage4 = models.ImageField(upload_to="media")
    bannerimage5 = models.ImageField(upload_to="media")
    bannerimage6 = models.ImageField(upload_to="media")