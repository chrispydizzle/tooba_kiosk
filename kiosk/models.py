from django.db import models
from django.utils import timezone


class Sector(models.Model):
    sector_text = models.CharField(max_length=200)
    img_url = models.CharField('image', max_length=200, blank="True")
    created_date = models.DateTimeField('publish time', default=timezone.now)


class Project(models.Model):
    project_text = models.CharField(max_length=200)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    img_url = models.CharField('image', max_length=200, blank="True")
    created_date = models.DateTimeField('publish time', default=timezone.now)


class Artifact(models.Model):
    artifact_text = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_url = models.CharField(max_length=200)
    file_type = models.CharField(max_length=4)
    created_date = models.DateTimeField('publish time', default=timezone.now)
