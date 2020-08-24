from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task (models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    dscription = models.CharField(null=True, blank=True, max_length=200)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self) : 
        return self.title



