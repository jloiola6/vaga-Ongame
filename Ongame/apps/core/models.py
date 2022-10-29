from django.db import models

from apps.user.models import User

# Create your models here.
class Historic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.CharField(max_length=100)
    object = models.IntegerField()
    date = models.DateTimeField()
    action = models.CharField(max_length=1)