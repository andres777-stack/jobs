from django.db import models
from acceso.models import User

class Job(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    location = models.CharField(max_length=50)
    state = models.BooleanField(default = False)
    owner = models.ForeignKey(User, related_name = 'jobs', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
# Create your models here.
