from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time

class TimeManagement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    finish_time = models.DateTimeField(default=timezone.now)
    work_time = models.FloatField(default=0)

    def __str__(self):
        return self.user + "_" + self.start_time

    def finish_work(self):
        self.finish_time = timezone.now()
        self.work_time = (self.finish_time - self.start_time).seconds / 60
        