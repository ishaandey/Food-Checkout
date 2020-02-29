from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User    

class Item(models.Model):
    item_name = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    ts_added = models.TimeField(default=now)
    exp_date = models.TimeField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
