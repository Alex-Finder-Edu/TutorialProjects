from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return f"ID: {self.id} - {self.first_name} {self.last_name}"

class Address(models.Model):
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=250)
    street_number = models.IntegerField()
    city = models.CharField(max_length=250)

    def __str__(self):
        p_fname = self.person_id.first_name
        p_lname = self.person_id.last_name
        person = f"{p_fname} {p_lname}"
        return f"{person} Addr - {self.city} {self.street_number} {self.street_name}"
