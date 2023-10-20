from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Section(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    # We've defined a Tutorial model with three fields: title, content, and published_date.
    # __str__() method returns a string representation of the object, which is useful for debugging.