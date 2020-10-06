from django.db import models


class Question(models.Model):
    class_name = models.CharField(null=False, blank=False, max_length=50)
    module_name = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return f"{self.module_name}.{self.class_name}"


class Tag(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return self.name
