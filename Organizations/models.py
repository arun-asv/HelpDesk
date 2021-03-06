from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    