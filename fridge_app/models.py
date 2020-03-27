from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User    

class Item(models.Model):
    item_name = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    ts_added = models.DateTimeField(default=now)
    exp_date = models.CharField(max_length=1000, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item_img = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.item_name


