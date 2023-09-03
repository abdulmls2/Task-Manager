from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import datetime, date


# Create your models here.

class Importance(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False)
    importance = models.ForeignKey(Importance, null=True, blank=False, on_delete=models.CASCADE)
    creation_date = models.DateField(default=timezone.now)
    ending_date = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.title

    # Check if the task's ending date has passed, and if it's not marked as complete
    def is_end_date(self):
        if date.today() > self.ending_date:
            if not self.complete:
                return True
            else:
                pass
        else:
            pass

    class Meta:
        ordering = ['creation_date']
