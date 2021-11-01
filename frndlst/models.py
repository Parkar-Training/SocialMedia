from django.db import models

# Create your models here.
class frnd_list(models.Model):
    FId = models.AutoField

    FrndId = models.CharField(max_length=3)
    FuserId = models.CharField(max_length=3)
    Stat= models.CharField(max_length=3)
    #FuserId = models.CharField(max_length=3)