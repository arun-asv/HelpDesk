from django.db import models
from Organizations.models import Departments

class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    departments = models.ForeignKey(Departments,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)