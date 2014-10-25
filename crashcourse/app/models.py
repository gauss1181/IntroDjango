from django.db import models

class Task(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title
