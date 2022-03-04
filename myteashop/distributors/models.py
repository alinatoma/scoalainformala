from django.db import models

class Distributors(models.Model):

    distributor_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.distributor_name} - {self.email} - {self.phone}"
