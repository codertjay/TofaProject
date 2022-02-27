from django.db import models


class PlaceHolder(models.Model):
    albumId = models.IntegerField()
    item_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    url = models.URLField()
    thumbnail_url = models.URLField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
