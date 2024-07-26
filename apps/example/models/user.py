from django.db import models


class User(models.Model):
    username = models.CharField(max_length=124, unique=True)
