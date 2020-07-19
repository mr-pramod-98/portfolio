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


class PersonalProjects(models.Model):
    class Meta:
        db_table = 'PersonalProjects'
        verbose_name_plural = 'PersonalProjects'

    title = models.CharField(max_length=40, primary_key=True)
    duration = models.CharField(max_length=20, null=False)
    tools_used = models.TextField(null=False)
    description = models.TextField(null=False)
    link = models.CharField(max_length=150, null=False)
    is_private = models.BooleanField(default=False)


class GroupProjects(models.Model):
    class Meta:
        db_table = 'GroupProjects'
        verbose_name_plural = 'GroupProjects'

    title = models.CharField(max_length=40, primary_key=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    team_size = models.IntegerField(null=False)
    role = models.CharField(max_length=40, null=False)
    tools_used = models.TextField(null=False)
    description = models.TextField(null=False)
    link = models.CharField(max_length=150, null=False)
    is_private = models.BooleanField(default=False)
