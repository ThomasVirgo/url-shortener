from django.db import models

# Create your models here.


class UrlPair(models.Model):
    long_url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.long_url}'
