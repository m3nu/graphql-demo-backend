from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=2048)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
