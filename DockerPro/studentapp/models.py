from django.db import models
from django.utils import timezone  # ← This is the right one for Django

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    create_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name