from django.db import models


class Question(models.Model):
    class_name = models.CharField(null=False, blank=False, max_length=50)


class Tag(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    question = models.ManyToManyField(Question)
