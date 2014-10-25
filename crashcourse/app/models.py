from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField('date due')

    def __unicode__(self):
        return self.title
