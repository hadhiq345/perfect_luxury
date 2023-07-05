from django.db import models


class Room(models.Model):
    room_no = models.PositiveIntegerField()
    person = models.CharField(max_length=15, null=False)
    mobile = models.CharField(max_length=10)
    bed = models.CharField(max_length=1)
