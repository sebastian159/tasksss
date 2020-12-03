from django.db import models

# Create your models here.

class Tasks(models.Model):
    task = models.CharField(max_length=200, default="Add Task")
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.task