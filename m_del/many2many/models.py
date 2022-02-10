from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=40)

class Song(models.Model):
    singer = models.ManyToManyField(Singer)
    song_name = models.CharField(max_length=100)
    duration = models.IntegerField()

    def own_by(self):
     return ",".join([str(p) for p in self.singer.all()])