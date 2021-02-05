from django.db import models

class Course(models.Model):

    name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)
