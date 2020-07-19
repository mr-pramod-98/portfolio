from django.db import models


# Create your models here.
class Certifications(models.Model):
    class Meta:
        db_table = 'Certifications'
        verbose_name_plural = 'Certifications'

    title = models.CharField(max_length=40, primary_key=True)
    duration = models.CharField(max_length=50, null=False)
    provider = models.CharField(max_length=40, null=False)
    score = models.FloatField(blank=True, null=True)
