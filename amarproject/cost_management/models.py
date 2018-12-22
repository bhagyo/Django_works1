from django.db import models

# Create your models here.


class Expenses(models.Model):
    amount = models.IntegerField()
    purpose = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.purpose
