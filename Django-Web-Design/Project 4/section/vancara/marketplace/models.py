from django.db import models

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
        # return f'{self.name} - {self.description[:20]}...'

class Type(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='vehicles')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='vehicles')
    model = models.CharField(max_length=50)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        # name not needed for the first two since they have str.
        return f'{self.make} - {self.type} - {self.model} - {self.description[:20]}...'


# related_name allows quick access to info w/o exta queries.
""""
my_make = Make.object.get(pk=1)
my_make.vehicles -> [Vehicle1, Vehicle2]
Gives you all vehicles that are pointed to it as a foreign key.
"""
