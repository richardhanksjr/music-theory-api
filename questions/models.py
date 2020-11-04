from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    class_name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    module_name = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return f"{self.module_name}.{self.class_name}"


class Tag(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Attempt(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)