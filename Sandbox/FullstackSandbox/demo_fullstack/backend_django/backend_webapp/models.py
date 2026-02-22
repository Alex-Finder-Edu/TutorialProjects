from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return f"ID: {self.id} - {self.first_name} {self.last_name}"
